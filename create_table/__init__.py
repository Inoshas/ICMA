import sqlite3
import csv

class cre_tab:
    db = None
    cur = None
    db_file = None
    file_name=None
    list_data=None
    
    #def __init__(self, db_file=":memory:"):
    def __init__(self, db_file):
        self.db_file=db_file
        self.db = sqlite3.connect(db_file)
        self.cur = self.db.cursor()
    
    def __del__(self):
        self.db.close()

    def commit(self):
        self.db.commit()


    # identify DB based on the requirement 
    # add values to table based on the table name and method    
    def add_table_val(self, adding_method, table_name, file_name,list_data):
        if adding_method =="file":
            self.read_csvfile(table_name,file_name)
        elif adding_method=="manually":
            self.add_data(table_name,list_data)
                
    
    def read_csvfile(self,table_name, file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader) 
            for row in reader: 
                list_data=row[0]
                self.add_data(table_name,list_data)
           
        
    def add_data(self, table_name,list_data):
      ## This will define which data to which table and how.....   
        if table_name== "phone_bills":
            insert_sql=f""" INSERT INTO phonebills (year, month, date, invoice_value, VAT_presentage) VALUES (?,?,?,?,?)"""
            self.cur.execute(insert_sql, (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] ))
          #  (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] )) """
                
        elif table_name=="transport":
            insert_sql=f"""INSERT INTO local_transport (year, month, date, location, distance_km, price_per_km, total_price_euro) VALUES (?,?,?,?,?,?,?) """
            self.cur.execute(insert_sql, (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4],list_data[5], int(list_data[5])*int(list_data[4]) ))

        ##### Here need to add all files and its entities......
        
        self.commit()
        
