import sqlite3

connection = sqlite3.connect("new.db")

cursor = connection.cursor()

try:
    tablename = "populations"
    cursor.execute(f"INSERT INTO {tablename} VALUES('New York City', 'NY', 8400000)")
    cursor.execute(f"INSERT INTO {tablename} VALUES('San Francisco', 'CA', 8000000)")

    connection.commit()

except sqlite3.OperationalError:
    print(f"Oops! Table {tablename} not found.")

connection.close()
