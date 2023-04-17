import sqlite3


db = sqlite3.connect('Inventory_and_price.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    cost REAL NOT NULL,
    product_id TEXT,
    size TEXT,
    quantitie INTEGER
    color TEXT
)
""")
            
cst=int(input("type cost"))


cur.execute("")


cur.execute("INSERT INTO Inventory (cost, product_id) VALUES (?,?)", (cst,'IB-',))

#cur.execute("INSERT INTO Inventory (product_id) VALUES(?)", ('IB-',)); product ids, sizes, quantities of each size, colors

cur.execute("UPDATE Inventory SET product_id = product_id || id");



cur.execute('SELECT * from Inventory')
rows = cur.fetchall()
for row in rows:
    print(row)

db.commit()
db.close()
print("end")
