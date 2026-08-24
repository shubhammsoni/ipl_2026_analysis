import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(
    """
    DELETE FROM players
    WHERE player_name LIKE 'Demo %'
    """
)

deleted_rows = cursor.rowcount

connection.commit()
connection.close()

print(f"Demo players deleted: {deleted_rows}")