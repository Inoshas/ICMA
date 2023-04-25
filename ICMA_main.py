from flask import Flask,render_template, request
import create_table
##import sqlite3

type = ""
adding_method =""
table_name =""
data_input=""

file_name="phone_bills.csv"#input('file_name?')
list_data=['2005', '5', '6', 'gtsss00222', '24']#input('list_data?')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DB_select/", methods=["POST"])
def select_db(): 
    global type
    type = (request.form.getlist('db_type'))[0]
    return render_template("index.html", first=f"You are going to update your {type} DB")

@app.route("/table_names/", methods=["POST"])
def select_table():
    global type
    global table_name  
    table_name = (request.form.getlist('table_n'))[0]
    return  render_template("index.html", second=f"You are going to update {type} database {table_name} table")

@app.route("/method/", methods=["POST"])
def select_method():
    global adding_method  
    adding_method= (request.form.getlist('adding_methods'))[0]
    return   render_template("index.html", third=f"Now ready to update {table_name} table in your {type} DB. Add data {adding_method}")

def enter_values():
    global type
    global table_name
    global adding_method
    global data_input


""" 
def identify_DB(type,adding_method, table_name, file_name,list_data):
    if type== "products":
        connec_db = create_table.cre_tab('Inventory_and_price.db')
        connec_db.add_table_val(adding_method, table_name, file_name,list_data)
        return type
        
        
    elif type=="expenses":
        print(type)
        connec_db = create_table.cre_tab('expenses_account.db')
        connec_db.add_table_val(adding_method, table_name, file_name,list_data)
        return type
"""

print('start here')
#print(identify_DB(type,adding_method, table_name, file_name,list_data))




""" 
def read_csvfile(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        
        for row in reader: 
            list_data=row[0]
            create_table.add_data(list_data)
            
def add_data(data, table_name):
    ## This will define which data to which table and how.....
    list_data=data.split(",") 
    create_table.identify_DB(type)
    if table_name== "phone_bills":
        cur.execute("INSERT INTO phonebills (year, month, date, invoice_value, VAT_presentage) VALUES (?,?,?,?,?)", 
            (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4] ))
        
    elif table_name=="transport":
        cur.execute("INSERT INTO local_transport (year, month, date, location, distance_km, price_per_km, total_price_euro) VALUES (?,?,?,?,?,?,?)", 
            (list_data[0],list_data[1],list_data[2],list_data[3],list_data[4],list_data[5], int(list_data[5])*int(list_data[4]) ))

    def add_table_val(self,table_name, adding_method):
        if adding_method =="file":
            self.read_csvfile(file_name="")
        elif adding_method=="manually":
            self.add_data()
  """             
    
            


'''
import tables_and_data_DB2

tables_and_data_DB2.insert_values()
print("done")
'''









if __name__=="__main__":
    app.run(debug=True)
    #(identify_DB(type,adding_method, table_name, file_name,list_data))
    
    
    
