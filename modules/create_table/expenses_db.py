import sqlite3
#import csv

#import openpyxl


db = sqlite3.connect('db/expenses.db')
cur = db.cursor()


#### Create table here:: 
### Table: local_transport
## Columns: id, year, month, date, location, distance_km, price_per_km, total_price
cur.execute("""
CREATE TABLE IF NOT EXISTS transport (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    to_location TEXT NOT NULL,
    from_location Text NOT NULL,
    turns INTEGER NOT NULL,
    total_distance REAL NOT NULL,
    price_per_unit_dis REAL NOT NULL,
    total_price REAL NOT NULL
)
""")

# id, year, month, date, invoice_value, VAT_presentage
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebills (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    invoice_value REAL NOT NULL,
    VAT_presentage REAL NOT NULL,
    comment TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS capitalcost (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    item TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    invoice_value REAL NOT NULL,
    VAT_presentage REAL NOT NULL,
    payment_stage TEXT NOT NULL, 
    comment TEXT 
)
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS importeditems (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    invoice_no TEXT NOT NULL, 
    item TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price_in_foreigncurency REAL NOT NULL,
    exchange_rate REAL NOT NULL,
    price_in_localcurency REAL NOT NULL,
    VAT_presentage REAL NOT NULL,
    shiping_cost REAL NOT NULL,
    shiping_invoice_number TEXT NOT NULL,
    custom_duty REAL NOT NULL,
    custom_reference_number TEXT NOT NULL, 
    payment_date TEXT NOT NULL,
    comment TEXT 
)
""")


db.commit()
db.close()

