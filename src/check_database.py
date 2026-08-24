import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ipl_2026.db"


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
    """
)

tables = cursor.fetchall()


print("\nTables currently available:")
print("-" * 40)

for table in tables:
    print(table[0])


connection.close()