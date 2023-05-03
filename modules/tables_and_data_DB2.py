import sqlite3
import csv

#import openpyxl


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

# id, year, month, date, invoice_value, VAT_presentage
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
    type_of_data=int(input("what data you want to add (Phone bills(enter 1), internal transport expenses (enter 2))"))
    input_method=int(input("How you prefer to enter data? (Manually(enter 1)/ With excel file (enter2): "))
    db = sqlite3.connect('expenses_account.db')
    cur = db.cursor()
    print(type_of_data , input_method)
    if type_of_data==2:
        if  input_method==1:
            data= input("Add  year, month, date, location, distance_km, price_per_km, total_price_euro in correct order and seperate with ',' : ")
            list_data=data.split(",") 
            cur.execute("INSERT INTO local_transport (year, month, date, location, distance_km, price_per_km, total_price_euro) VALUES (?,?,?,?,?,?,?)", 
                (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4],list_data[5], int(list_data[5])*int(list_data[4]) ))
       
    elif type_of_data==1:
        if input_method==1:
            data= input("Add  year, month, date, invoice_value, VAT_presentage in correct order and seperate with ',' : ")
            list_data=data.split(",") 
            cur.execute("INSERT INTO phonebills (year, month, date, invoice_value, VAT_presentage) VALUES (?,?,?,?,?)", 
                (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] ))
        
        elif input_method==2:
            file_name= input("File name")
            upload_csv_data(file_name)
    
    else:
        print('your details are not valid to execute')
    
    print("endQQQ")
    db.commit()
    db.close()

#insert_values()

def upload_csv_data(file_name):
    with open(file_name, 'r') as csv_file:
        db = sqlite3.connect('expenses_account.db')
        cur = db.cursor()
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        
        for row in reader: 
            list_data=row[0].split(",")
            cur.execute("INSERT INTO phonebills (year, month, date, invoice_value, VAT_presentage) VALUES (?,?,?,?,?)", 
                (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] ))
        
        db.commit()
        db.close()
          


    
    ### Here goes how you read file data and upload :::
    
    


"""
cur.execute('SELECT * from local_transport')
rows = cur.fetchall()
for row in rows:
    print(row)
"""
db.commit()
db.close()

