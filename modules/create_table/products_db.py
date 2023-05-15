import sqlite3



db = sqlite3.connect('db/products.db')
cur = db.cursor()


#### Create table here:: 
### Table: local_transport
## Columns: id, year, month, date, location, distance_km, price_per_km, total_price
cur.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,
    prod_id TEXT NOT NULL, 
    name TEXT NOT NULL,
    size TEXT NOT NULL,
    color TEXT NOT NULL,
    quantity TEXT NOT NULL,
    damage_quantity INTEGER NOT NULL,
    instock_quantity INTEGER NOT NULL,
    sales_quantity INTEGER NOT NULL
)
""")

# id, year, month, date, invoice_value, VAT_presentage
cur.execute("""
CREATE TABLE IF NOT EXISTS unitprice (
    id INTEGER PRIMARY KEY,
    prod_id TEXT NOT NULL, 
    unit_id TEXT NOT NULL,
    QR_code Text NOT NULL,
    cost REAL NOT NULL,
    VAT_pres REAL NOT NULL,
    marginal_price REAL NOT NULL,
    selling_price_defined REAL NOT NULL,
    actual_selling_price REAL NOT NULL,
    status TEXT NOT NULL
)
""")

''' 
### if you want to add more colums to table use this
cur.execute(""" ALTER TABLE [Tabl_name]
    ADD COLUMN [column_name] INTEGER """)
'''

db.commit()
db.close()

