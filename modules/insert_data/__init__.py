import sqlite3
import csv

class cre_tab:
    db = None
    cur = None
    db_file = None
   
    data_format1=[];
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
    def add_table_val(self, adding_method, table_name, data_format):
        if adding_method =="file":
            file_link=f"files/{data_format}"
            self.read_csvfile(table_name,file_link)
        elif adding_method=="manually":
            array_data=(eval(data_format))
            self.add_data(table_name,array_data)
                
    
    def read_csvfile(self,table_name, data_format):
        with open(data_format, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader) 
            for row in reader: 
                list_data=row[0].split(",")
                print(list_data)
                self.add_data(table_name,list_data)
           
        
    def add_data(self, table_name,data_format):
        
        
        """def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
        """
      ## This will define which data to which table and how.....   
        if table_name== "phonebills":
            insert_sql=f""" INSERT INTO phonebills (year, month, date, invoice_value, VAT_presentage, comment) VALUES (?,?,?,?,?,?)"""
            self.cur.execute(insert_sql, (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],data_format[5]  ))
         
          #  (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] )) """          
        elif table_name=="transport":
            insert_sql=f"""INSERT INTO local_transport (year, month, date, location, distance_km, price_per_km, total_price_euro) VALUES (?,?,?,?,?,?,?) """
            self.cur.execute(insert_sql, (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],data_format[5], int(data_format[5])*int(data_format[4]) ))

        ##### Here need to add all files and its entities......
        self.commit()
        
