#from flask import Flask,render_template, request


import tables_and_data_DB2

tables_and_data_DB2.insert_values()
print("done")

''' 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forward/", methods=["POST"])
def move_forward():
    forward_message = "Moving Forward..."
    return render_template("index.html", forward_message=forward_message)



if __name__=="__main__":
    app.run(debug=True)
    
'''