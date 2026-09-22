from src.db_config import get_connection


connection = get_connection()

print("Connected to MySQL successfully!")
print("Database:", connection.database)
print("MySQL version:", connection.server_info)

connection.close()