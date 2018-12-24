import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    #c.execute("""CREATE TABLE orders (make TEXT, model TEXT, date DATE)""")

    orders = [
        ('Ford', 'Fusion', '2018-01-01'),
        ('Ford', 'Fusion', '2018-01-11'),
        ('Ford', 'Fusion', '2018-01-21'),
        ('Ford', 'F250', '2018-02-01'),
        ('Ford', 'F250', '2018-02-12'),
        ('Ford', 'F250', '2018-02-24'),
        ('Ford', 'Expedition', '2018-03-01'),
        ('Ford', 'Expedition', '2018-03-13'),
        ('Ford', 'Expedition', '2018-03-26'),
        ('Honda', 'Accord', '2018-04-01'),
        ('Honda', 'Accord', '2018-04-15'),
        ('Honda', 'Accord', '2018-04-30'),
        ('Honda', 'Civic', '2018-05-01'),
        ('Honda', 'Civic', '2018-05-02'),
        ('Honda', 'Civic', '2018-05-03')
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)", orders)

    c.execute("SELECT * FROM orders ORDER BY date DESC")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])

