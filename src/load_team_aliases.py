import json
from pathlib import Path

from src.db_config import get_connection
from src.data_cleaning import clean_team_name


JSON_FOLDER = Path("data/raw/ipl_json")


# ============================================================
# EXTRACT RAW TEAM NAMES
# ============================================================

def extract_raw_teams():

    raw_teams = set()

    for file_path in JSON_FOLDER.glob("*.json"):

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        info = data["info"]

        for team_name in info.get("teams", []):

            if team_name:
                raw_teams.add(team_name.strip())

    return raw_teams


# ============================================================
# LOAD TEAM ALIASES
# ============================================================

def load_team_aliases(raw_teams):

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        # Get canonical teams already stored in MySQL
        cursor.execute("""
            SELECT team_id, team_name
            FROM teams
        """)

        team_lookup = {
            team_name: team_id
            for team_id, team_name in cursor.fetchall()
        }

        inserted_count = 0

        for raw_team_name in sorted(raw_teams):

            # Convert raw name to canonical name
            canonical_name = clean_team_name(raw_team_name)

            # Find canonical team ID
            team_id = team_lookup.get(canonical_name)

            if team_id is None:
                print(
                    f"WARNING: Canonical team not found: "
                    f"{raw_team_name} -> {canonical_name}"
                )
                continue

            cursor.execute(
                """
                INSERT INTO team_aliases (
                    team_id,
                    alias_name
                )
                VALUES (%s, %s)
                """,
                (
                    team_id,
                    raw_team_name
                )
            )

            inserted_count += 1

            print(
                f"{raw_team_name} "
                f"-> {canonical_name} "
                f"(team_id={team_id})"
            )

        connection.commit()

        print("\n----------------------------------------")
        print(f"Team aliases inserted: {inserted_count}")
        print("----------------------------------------")

    except Exception as error:

        print("\nERROR while loading team aliases:")
        print(error)

        if connection:
            connection.rollback()

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

        print("\nMySQL connection closed.")


# ============================================================
# MAIN
# ============================================================

def main():

    raw_teams = extract_raw_teams()

    print(f"Raw team names found: {len(raw_teams)}")
    print()

    load_team_aliases(raw_teams)


if __name__ == "__main__":
    main()