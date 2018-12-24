import sqlite3
import sys

with sqlite3.connect('rand.db') as connection:
    c = connection.cursor()

    func = input("What function would you like to apply? ")

    sql_executions = {"average": "SELECT avg(num) FROM rand",
    "maximum": "SELECT max(num) FROM rand",
    "minimum": "SELECT min(num) FROM rand",
    "sum": "SELECT sum(num) FROM rand"}

    if func == "average" or func == "maximum" or func == "minimum" or func == "sum":
        c.execute(sql_executions[func])
        row = c.fetchone()
        print(f"The {func} is: {row[0]}.")
    else:
        print("Function with that name not available. Closing program.")
        sys.exit()