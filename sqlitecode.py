import sqlite3
import sys

def execute_query(cursor, query, conn):
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            conn.commit()
            print(f"Query executed successfully: {query}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python sqliteterminal.py <database_file>")
        sys.exit(1)

    database_file = sys.argv[1]
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    print(f"Connected to SQLite database: {database_file}")
    print("Enter your SQL commands (type 'exit' to quit):")

    while True:
        query = input("sqlite> ")
        if query.lower() == "exit":
            break
        execute_query(cursor, query, conn)

    cursor.close()
    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()