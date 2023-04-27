
from flask import Flask,render_template, request
from modules import create_table
import configparser
"""
cfg = configparser.ConfigParser()
cfg.read('config.ini')
CONFIG = cfg.sections()
"""
database=""
adding_method =""
table_name =""
data_input=""

#file_name=f"{CONFIG['FILES_DIR']}phone_bills.csv"
list_data=['2005', '5', '6', 'gtsss00222', '24']

app = Flask(__name__)

def read_db(database):
    pass

def read_table(database, table_name):
    pass

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/step1', methods=["POST"])
def step_1():
    return render_template('step1.html')

@app.route('/DB_select/', methods=["POST"])
def step_2():
    database_type=request.form.getlist('db_type')[0]
    if database_type== "option1":
        db_type = read_db(database=database_type)
        return render_template('expenses.html', db_type=database_type)
    elif database_type== "option2":
        db_type = read_db(database=database_type)
        return render_template('products.html', db_type=database_type)


@app.route('/table_names/', methods=["POST"])
def step_3():
    table_name=request.form.getlist('db_type')[0]
    if database_type== "option1":
        tables = read_db(database=database_type)
        return render_template('expenses.html')
    elif database_type== "option2":
        tables = read_db(database=database_type)
        return render_template('products.html')
  
    return render_template('step2.html', db_type=database_type, tables=tables)

@app.route('/step2', methods=["POST"])
def step_3():
    database_type=request.form.getlist('db_type')[0]
    table = request.form.getlist('table')[0]
    data = read_table(database=database_type, table_name=table)
    return render_template('step3.html', db_type=database_type, table=table, data=data)






""" 
type = ""
adding_method =""
table_name =""
data_input=""
func1=""

file_name="phone_bills.csv"#input('file_name?')
list_data=['2005', '5', '6', 'gtsss00222', '24']#input('list_data?')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select_fun/", methods=["POST"])
def select_func(): 
    global func1
    func1 = (request.form.getlist('sel_f'))[0]
    return render_template("index.html", first=f"You are generating reports")

@app.route("/DB_select/", methods=["POST"])
def select_db(): 
    global type if func1== "option1":
        return render_template('expenses.html')
    elif func1== "option2":
        return render_template('products.html')

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

@app.route("/enter_Data/", methods=["POST"])
def enter_values():
    global type
    global table_name
    global adding_method
    global data_input
    company_name = request.form['company_name']


""" 
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
    
    
    
