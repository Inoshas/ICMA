from flask import Flask,render_template, request
from modules import insert_data

database_type=""
method_d=""
adding_method =""
table_name =""
data_input=""


app = Flask(__name__)

@app.route('/')
def main_fun_html():
    return render_template('index.html')

@app.route('/DB_select/', methods=["POST"])
def step_2():
    database_type=request.form.getlist('db_type')[0]
    if database_type== "expenses":
        return render_template('expenses.html', db_type=database_type)
    elif database_type== "products":
        return render_template('products.html', db_type=database_type)


@app.route('/table_names/', methods=["POST"])
def step_3():
    database_type=request.form.getlist('db_type')[0]
    table_need = request.form.getlist('table_n')[0]
    return render_template('method.html', db_type=database_type, table=table_need)


@app.route('/method_t/', methods=["POST"])
def step_4():
    database_type=request.form.getlist('db_type')[0]
    table_need = request.form.getlist('table_n')[0]
    method_data=request.form.getlist('sel_f')[0]
   
    if method_data== "manually":
        enter_name= " Type inside the square brackets [] with comma (",") seperation in correct order"
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
        database_type=f"db/{database_type}";
        connec_db = insert_data.cre_tab('db/companydata.db')
        connec_db.add_table_val(method_data, table_need, data_ent)
        
        """
        if database_type=="expenses.db":
            first=connec_db.summary_expe()
            res = 0
            for i in first:
                res += i
            return render_template('more_tasks.html', cs=  first[0], pb=first[1],
                                lt=first[2],itc=first[3], sc=first[4], cd=first[5], 
                                tot=res)
        """
        
        return render_template('more_tasks.html', cs=  "check", pb="check",
                                lt="check",itc="check", sc="check", cd="check", 
                                tot="check")
        
    elif confirm_status== "Restart": 
        return render_template('index.html')
       
 
   
   
if __name__=="__main__":
    app.run(debug=True)
