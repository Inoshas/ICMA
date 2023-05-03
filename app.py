from flask import Flask,render_template, request
from modules import create_table
import configparser



database_type=""
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
   
    if method_data== "manually":
        enter_name= "Enter data in the correct order with ',' seperation"
    elif method_data== "file" :
        enter_name= "Enter csv file name "
    
    return render_template('data_enter.html',  ent_name=enter_name,  db_type=database_type, table=table_need, method_d=method_data)


@app.route('/update_d/', methods=["POST"])
def step_5():
    database_type=request.form.getlist('db_type')[0]
    table_need = request.form.getlist('table_n')[0]
    method_data=request.form.getlist('method_d')[0]
    data_ent=request.form.getlist('data_f')[0]
    
    return render_template('more_tasks.html',   db_type=database_type, table=table_need, method_d=method_data, data_f=data_ent)


@app.route('/finalize_d/', methods=["POST"])
def step_6():
    confirm_status= request.form.getlist('status_n')[0]
 
    if confirm_status== "Enter":
        database_type=request.form.getlist('db_type')[0] +".db"
        table_need = request.form.getlist('table_n')[0]
        method_data=request.form.getlist('method_d')[0]
        data_ent=request.form.getlist('data_f')[0]
        connec_db = create_table.cre_tab(database_type)
        connec_db.add_table_val(method_data, table_need, data_ent)
        #db_type=database_type, table=table_need, method_d=method_data, data_set=data_ent)
        return render_template('more_tasks.html', first=  database_type)
   
    elif confirm_status== "Restart": 
        return render_template('index.html')
       
   
    
if __name__=="__main__":
    app.run(debug=True)