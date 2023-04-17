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
#VAT, import/export tax, shipping cost, purchase price, other expenses,          
cur.execute("""
CREATE TABLE IF NOT EXISTS unit_price (
    id INTEGER PRIMARY KEY,
    VAT REAL ,
    custom_tax REAL,
    shipping_cost REAL,
    purchase_price REAL,
    other_expenses REAL
    
)
""")

            
cst=int(input("type cost"))
cur.execute("")
cur.execute("INSERT INTO Inventory (cost, product_id) VALUES (?,?)", (cst,'IB-',))
#cur.execute("INSERT INTO Inventory (product_id) VALUES(?)", ('IB-',)); product ids, sizes, quantities of each size, colors
cur.execute("UPDATE Inventory SET product_id = product_id || id");



cur.execute("INSERT INTO unit_price(VAT, custom_tax) VALUES (?,?)", (cst/2,'None',))

#print(Inventory.product_id)

cur.execute('SELECT * from Inventory')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute('SELECT * from unit_price')
rows1 = cur.fetchall()
for row1 in rows1:
    print(row1)

db.commit()
db.close()
print("end")
