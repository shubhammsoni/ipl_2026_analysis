import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "ipl_2026.db"

SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"


def create_database():

    DATABASE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    print("=" * 50)
    print("IPL 2026 Analytics")
    print("=" * 50)

    print("Connected to database.")

    # Read SQL commands from schema.sql
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Run the SQL commands
    connection.executescript(sql_script)

    connection.commit()

    print("Database tables created successfully!")

    connection.close()

    print("Database connection closed.")


if __name__ == "__main__":
    create_database()