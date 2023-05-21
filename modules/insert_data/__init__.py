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
    
        print(self.db_file)
            # id , year, month, date,invoice_value,VAT_presentage,comment
        if table_name== "phonebills":
            print(table_name)
            insert_sql=f""" INSERT INTO phonebills (year, month, date,invoice_value,VAT_presentage,comment) VALUES (?,?,?,?,?,?)"""
            self.cur.execute(insert_sql, (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],data_format[5]  ))    
    
        # id ,year ,month, date ,to_location ,from_location , turns , total_distance ,price_per_unit_dis, total_price
        elif table_name=="transport":
            insert_sql=f"""INSERT INTO transport (year ,month, date ,to_location ,from_location , turns , total_distance ,price_per_unit_dis, total_price) VALUES (?,?,?,?,?,?,?,?,?) """
            self.cur.execute(insert_sql, (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],data_format[5],
                                        data_format[6],data_format[7],int(data_format[7])*int(data_format[6])*int(data_format[5]) ))

        # id ,year,month ,date , item ,quantity ,invoice_value,VAT_presentage , payment_stage , comment  
        elif table_name=="capitalcost":
            insert_sql=f"""INSERT INTO capitalcost (year,month ,date , item ,quantity ,invoice_value,VAT_presentage , payment_stage , comment) VALUES (?,?,?,?,?,?,?,?,?) """
            self.cur.execute(insert_sql, (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],data_format[5],
                                        data_format[6],data_format[7], data_format[8]))  
        
        # id , year , month , date , invoice_no , item ,   quantity , price_in_foreigncurency ,
        # exchange_rate ,price_in_localcurency,  VAT_presentage,  shiping_cost ,
        # shiping_invoice_number ,  custom_duty , custom_reference_number,  payment_date , comment 
    
        elif table_name=="importeditems":
            insert_sql=f"""INSERT INTO importeditems 
            (year , month , date , invoice_no , item ,   quantity , price_in_foreigncurency ,exchange_rate ,price_in_localcurency,  VAT_presentage,  shiping_cost ,shiping_invoice_number ,  custom_duty , custom_reference_number,  payment_date , comment )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            self.cur.execute(insert_sql, 
                            (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],
                            data_format[5],data_format[6],data_format[7], data_format[8], data_format[9],
                            data_format[10],data_format[11],data_format[12],data_format[13], data_format[14] ,data_format[15]))
        self.commit()   
            
    
        if table_name=="inventory":
            insert_sql=f"""INSERT INTO inventory 
            (category, prod_id,  name , size,  color,  quantity,  damage_quantity , instock_quantity , sales_quantity )
            VALUES (?,?,?,?,?,?,?,?,?)
            """
            self.cur.execute(insert_sql, 
                            (data_format[0],data_format[1],data_format[2],data_format[3],data_format[4],
                            data_format[5],data_format[6],data_format[7], data_format[8]))
        
        
        #    id ,prod_id ,  unit_id ,QR_code ,cost ,VAT_pres ,marginal_price ,selling_price_defined ,actual_selling_price , status 
        
        elif table_name=="unitprice":
            print(table_name)
            insert_sql=f"""INSERT INTO unitprice
            (prod_id, unit_id,
            QR_code,cost,VAT_pres ,marginal_price,
            selling_price_defined ,actual_selling_price , status )
            VALUES (?,?,?,?,?,?,?,?,?)
            """
            
            self.cur.execute('SELECT MAX(id) FROM unitprice')
            dummy_code_id = self.cur.fetchone()
            dummy_code_id='{:05}'.format(dummy_code_id[0]+1)
            dummy_prod_id= f'IB-{dummy_code_id}'
            print(dummy_prod_id)
            
            self.cur.execute(insert_sql, 
                            (dummy_prod_id,data_format[0],data_format[1],data_format[2],data_format[3],
                            data_format[2]*(data_format[3]+100)/(100),data_format[4], 0, "Available"))
            
            #self.cur.execute("UPDATE unitprice SET product_id = product_id || id WHERE id = (SELECT MAX(id) FROM unitprice)")
        
        self.commit() 
        #self.close()  
            
    def summary_expe(self):
        if self.db_file=="db/expenses.db":
            insert_sql= f"""SELECT 
        (SELECT SUM(c2.invoice_value) from capitalcost c2)  as tot_capita,
        (Select SUM(p2.invoice_value) from phonebills p2 )as tot_phone,  
        (select SUM(t2.total_price) from transport t2 ) as tot_trans,
        (select SUM(i2.price_in_localcurency) from importeditems i2 )as tot_itempric,
        (select SUM(i3.shiping_cost) from importeditems i3 )as tot_shipping,
        (select SUM(i4.custom_duty) from importeditems i4 ) as tot_cusduty
        FROM capitalcost c, phonebills p, transport t, importeditems i limit 1"""
        
     
            self.cur.execute(insert_sql)
            dummy_results=self.cur.fetchall()
            self.commit()
            return dummy_results[0]
            
   # id ,category, prod_id,  name , size,  color,  quantity,  damage_quantity , instock_quantity , sales_quantity ,


        
          
        
