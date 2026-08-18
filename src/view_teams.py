import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT
        team_id,
        team_name,
        short_name
    FROM teams
    ORDER BY team_id
    """
)


teams = cursor.fetchall()


print()
print("=" * 70)
print("IPL TEAMS")
print("=" * 70)

for team in teams:

    team_id = team[0]
    team_name = team[1]
    short_name = team[2]

    print(
        f"{team_id:<5} "
        f"{short_name:<6} "
        f"{team_name}"
    )


print("=" * 70)
print(f"Total Teams: {len(teams)}")
print("=" * 70)


connection.close()