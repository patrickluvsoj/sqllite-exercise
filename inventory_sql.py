import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("INSERT INTO inventory VALUES('Ford', 'F250', 10)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Fusion', 6)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Expedition', 6)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 12)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 25)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'CRV',8)")

