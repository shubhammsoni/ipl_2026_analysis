import json
from pathlib import Path

from src.db_config import get_connection
from src.data_cleaning import clean_team_name


# ============================================================
# CONFIGURATION
# ============================================================

JSON_FOLDER = Path("data/raw/ipl_json")


# ============================================================
# EXTRACT CANONICAL TEAMS
# ============================================================

def extract_teams():

    teams = set()

    json_files = list(JSON_FOLDER.glob("*.json"))

    print(f"JSON files found: {len(json_files)}")

    for file_path in json_files:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        info = data["info"]

        for raw_team_name in info.get("teams", []):

            clean_team = clean_team_name(raw_team_name)

            if clean_team:
                teams.add(clean_team)

    return teams


# ============================================================
# LOAD TEAMS INTO MYSQL
# ============================================================

def load_teams(teams):

    connection = None
    cursor = None

    try:

        # Connect to MySQL
        connection = get_connection()

        cursor = connection.cursor()

        # Parameterized SQL
        sql = """
            INSERT INTO teams (team_name)
            VALUES (%s)
        """

        inserted_count = 0

        for team_name in sorted(teams):

            cursor.execute(
                sql,
                (team_name,)
            )

            inserted_count += 1

            print(f"Inserted: {team_name}")

        # Save changes permanently
        connection.commit()

        print("\n----------------------------------------")
        print(f"Teams inserted successfully: {inserted_count}")
        print("----------------------------------------")

    except Exception as error:

        print("\nERROR while loading teams:")
        print(error)

        # Undo uncommitted changes if something fails
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

    print("\nExtracting canonical teams...\n")

    teams = extract_teams()

    print(f"\nCanonical teams found: {len(teams)}")

    print("\nTeams to be loaded:")
    print("----------------------------------------")

    for team in sorted(teams):
        print(team)

    print("\nLoading teams into MySQL...\n")

    load_teams(teams)


if __name__ == "__main__":
    main()