from flask import Flask,render_template, request
from modules import create_table
import configparser

""" 
cfg = configparser.ConfigParser()
cfg.read('config.ini')
CONFIG = cfg.sections()
"""
my_db=""
method_d=""
adding_method =""
table_name =""
data_input=""

#file_name=f"{CONFIG['FILES_DIR']}phone_bills.csv"
#list_data=['2005', '5', '6', 'gtsss00222', '24']

app = Flask(__name__)

def read_db(database):
    pass

def read_table(database, table_name):
    pass

@app.route('/')
def main_fun_html():
    return render_template('index.html')


@app.route('/DB_select/', methods=["POST"])
def step_2():
    database_type=request.form.getlist('db_type')[0]
   # my_db = read_db(database=database_type)
    if database_type== "expenses":
        #db_type = read_db(database=database_type)
        return render_template('expenses.html', db_type=database_type)
    elif database_type== "products":
        #db_type = read_db(database=database_type)
        return render_template('products.html', db_type=database_type)

    
    
    #return render_template('step2.html', db_type=database_type)

@app.route('/table_names/', methods=["POST"])
def step_3():
    database_type=request.form.getlist('db_type')[0]
    table_need = request.form.getlist('table_n')[0]
   # data = read_table(database=database_type, table_name=table)
    return render_template('method.html', db_type=database_type, table=table_need)


@app.route('/method_t/', methods=["POST"])
def step_4():
    database_type=request.form.getlist('db_type')[0]
    table_need = request.form.getlist('table_n')[0]
    method_data=request.form.getlist('sel_f')[0]
   # data = read_table(database=database_type, table_name=table)
    return render_template('method.html', db_type=database_type, table=table_need, method_d=method_data)


if __name__=="__main__":
    app.run(debug=True)
    #(identify_DB(type,adding_method, table_name, file_name,list_data))
