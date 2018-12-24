import sqlite3
import random

with sqlite3.connect('rand.db') as connection:
    c = connection.cursor()

    #c.execute("""CREATE TABLE rand (num INT)""")

    rands = []
    for i in range(1, 101):
        rands.append((random.randint(1,101),))
        
    print(rands)
    c.executemany("INSERT INTO rand VALUES(?)", rands)
    #c.execute("DELETE FROM rand")