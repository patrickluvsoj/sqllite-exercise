import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT DISTINCT orders.make, orders.model, inventory.quantity FROM orders, inventory WHERE orders.model=inventory.model GROUP BY orders.model")

    rows = c.fetchall()

    for r in rows:
        make = (r[0],)
        model = (r[1],)
        quantity = (r[2],)
        c.execute("SELECT count(model) FROM orders WHERE model=?", model)
        order_count = c.fetchone()
        print(f"{make[0]} {model[0]}")
        print(f"Quantity: {quantity[0]}")
        print(f"Order count: {order_count[0]}\n")
        

    