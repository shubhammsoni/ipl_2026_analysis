import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"

connection = sqlite3.connect(DATABASE_PATH)
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

demo_players = [
    (
        "Demo Batter",
        "Batter",
        "India",
        9,
        "Right-Handed",
        "Right-Arm Fast"
    ),
    (
        "Demo Bowler",
        "Bowler",
        "India",
        9,
        "Left-Handed",
        "Left-Arm Spin"
    ),
    (
        "Demo All-Rounder",
        "All-Rounder",
        "India",
        6,
        "Right-Handed",
        "Right-Arm Medium"
    ),
]

cursor.executemany(
    """
    INSERT INTO players (
        player_name,
        role,
        nationality,
        team_id,
        batting_style,
        bowling_style
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    demo_players
)

connection.commit()

print("Demo players inserted successfully.")

connection.close()