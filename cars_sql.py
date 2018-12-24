import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT inventory.make, inventory.model, 
    inventory.quantity, orders.date FROM inventory, orders 
    WHERE inventory.make = orders.make""")

    rows = c.fetchall()

    for r in rows:
        print(f"{r[0]} {r[1]}")
        print(f"Quantity: {r[2]}")
        print(f"Date: {r[3]}")
        print("")