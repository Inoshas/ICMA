import sqlite3
import csv


class create_table:
    # identify DB based on the requirement
    def identify_DB(type):
        if type== "products":
            db = sqlite3.connect('Inventory_and_price.db')
            cur = db.cursor()
            
        elif type=="expenses":
            db = sqlite3.connect('expenses_account.db')
            cur = db.cursor()
            
        # add values to table based on the table name and method    
    def add_table_val(table_name, adding_method):
        if adding_method =="file":
            create_table.read_csvfile(file_name=="")
            create_table.add_data(data_array="")
        elif adding_method=="manually":
            create_table.add_data()
                
    
    def read_csvfile(file_name):
        with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        
        for row in reader: 
            list_data=row[0].split(",")
            return list_data
        
    def add_data():
        r=3
        