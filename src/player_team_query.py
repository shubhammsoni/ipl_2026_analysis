import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"


# Connect to database
connection = sqlite3.connect(DATABASE_PATH)

# Enable foreign key support
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()


# Join players with their respective teams
cursor.execute(
    """
    SELECT
        players.player_id,
        players.player_name,
        players.role,
        teams.short_name,
        teams.team_name
    FROM players
    INNER JOIN teams
        ON players.team_id = teams.team_id
    ORDER BY players.player_name;
    """
)


results = cursor.fetchall()


print()
print("=" * 100)
print("IPL PLAYERS AND TEAMS")
print("=" * 100)

print(
    f"{'ID':<6}"
    f"{'PLAYER':<25}"
    f"{'ROLE':<20}"
    f"{'TEAM':<8}"
    f"{'TEAM NAME'}"
)

print("-" * 100)


for row in results:
    player_id = row[0]
    player_name = row[1]
    role = row[2]
    short_name = row[3]
    team_name = row[4]

    print(
        f"{player_id:<6}"
        f"{player_name:<25}"
        f"{role:<20}"
        f"{short_name:<8}"
        f"{team_name}"
    )


print("-" * 100)
print(f"Total Players: {len(results)}")
print("=" * 100)


connection.close()