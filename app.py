
from flask import Flask,render_template, request
import sqlite3

app = Flask(__name__)


def get_amount_tax_paid(company_name):
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    sql="""
    SELECT tax_paid FROM companies WHERE name=?
    """
    result = cur.execute(sql, (company_name,)).fetchone()
    print(result)
    db.close()
    return result[0]

def total_tax_payment():
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    sql="""
    SELECT SUM(tax_paid) FROM companies 
    """
    total_tax_paid = cur.execute(sql).fetchone()
    print(total_tax_paid)
    db.close()
    return total_tax_paid[0]

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def find_info():
    company_name = request.form['company_name']
    result = get_amount_tax_paid(company_name=company_name)
    total_tax_paid= total_tax_payment()
    # print(total_tax_paid)
    return render_template('index.html', result=result, total_tax_paid=total_tax_paid)
   

if __name__=="__main__":
    app.run(debug=True)