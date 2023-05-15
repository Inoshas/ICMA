import sqlite3

#What is DB name??
db_name='products.db'
#What is your table name??
table_name='inventory' 
db = sqlite3.connect(db_name)
cur = db.cursor()
# id is the primary key for the table: 
# you can change if necessary.
# change Column_2 and rest according to your requiremenst
# change data type accordingly (REAL ,TEXT, INTEGER)
# if it shouln't be empty marked with 'NOT NULL' as below.

cur.execute("""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY,
    column_2 REAL NOT NULL,
    column_3 TEXT,
    column_4 TEXT,
    column_5 INTEGER
    column_6 TEXT
)
""")

db.commit()
db.close()


'''            
cst=int(input("type cost"))
cur.execute("")
cur.execute("INSERT INTO Inventory (cost, product_id) VALUES (?,?)", (cst,'IB-',))


cur.execute("UPDATE Inventory SET product_id = product_id || id WHERE id = (SELECT MAX(id) FROM Inventory)")



cur.execute("INSERT INTO unit_price(VAT, custom_tax) VALUES (?,?)", (cst/2,'None'))

#cur.execute("SELECT [product_id] FROM Inventory WHERE [Taxes Paid] = (SELECT MAX([Taxes Paid]) FROM data);")
cur.execute("UPDATE unit_price SET P_id = (SELECT product_id FROM Inventory WHERE Inventory.id = unit_price.id)")


cur.execute('SELECT * from Inventory')
rows = cur.fetchall()
for row in rows:
    
    print(row)
    
print("Table 2")

cur.execute('SELECT * from unit_price')
rows1 = cur.fetchall()

for row1 in rows1:
    print(row1)
'''


