import sqlite3
#import csv

db = sqlite3.connect('expenses_account.db')
cur = db.cursor()


#### Create table here:: 
### Table: local_transport
## Columns: id, year, month, date, location, distance_km, price_per_km, total_price
cur.execute("""
CREATE TABLE IF NOT EXISTS local_transport (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    location TEXT NOT NULL,
    distance_km REAL NOT NULL,
    price_per_km REAL NOT NULL,
    total_price_euro REAL 
)
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS phonebills (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    invoice_value REAL NOT NULL,
    VAT_presentage REAL NOT NULL
)
""")


#### Insert colums if something missing: 
''' 
cur.execute(""" ALTER TABLE local_transport
    ADD COLUMN month Integer """)
'''

def insert_values():
    data_input=input("what data you want to add (Phone bills(P), )")
    db = sqlite3.connect('expenses_account.db')
    cur = db.cursor()
    data= input("Add  year, month, date, location, distance_km, price_per_km, total_price_euro in correct order and seperate with ',' : ")
    list_data=data.split(",") 
    cur.execute("INSERT INTO local_transport (year, month, date, location, distance_km, price_per_km, total_price_euro) VALUES (?,?,?,?,?,?,?)", 
                (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4],list_data[5], int(list_data[5])*int(list_data[4]) ))
    print("endQQQ")
    db.commit()
    db.close()

#insert_values()


"""
cur.execute('SELECT * from local_transport')
rows = cur.fetchall()
for row in rows:
    print(row)
"""
db.commit()
db.close()

