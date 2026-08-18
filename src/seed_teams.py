import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"


teams = [
    ("Chennai Super Kings", "CSK"),
    ("Delhi Capitals", "DC"),
    ("Gujarat Titans", "GT"),
    ("Kolkata Knight Riders", "KKR"),
    ("Lucknow Super Giants", "LSG"),
    ("Mumbai Indians", "MI"),
    ("Punjab Kings", "PBKS"),
    ("Rajasthan Royals", "RR"),
    ("Royal Challengers Bengaluru", "RCB"),
    ("Sunrisers Hyderabad", "SRH")
]


def insert_teams():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.executemany(
        """
        INSERT OR IGNORE INTO teams
        (team_name, short_name)
        VALUES (?, ?)
        """,
        teams
    )

    connection.commit()

    print("IPL teams inserted successfully!")

    connection.close()


if __name__ == "__main__":
    insert_teams()