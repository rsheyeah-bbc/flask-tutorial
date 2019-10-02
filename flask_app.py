from flask import Flask,jsonify,request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! Does Flask auto-update? Do you need to reload the server? It updated"


@app.route("/api", methods=["POST","GET"])
def helloapi():
    if request.method == "GET":
        print("inside get method")
        studentData = {
            'name': ['Tig', 'Tac', 'Toe'],
            'age': [1, 2, 3],
            'city': ['Disney', 'Cbeebies', 'CartoonNetwork']
        }

        dataframe_object = pd.DataFrame(studentData)
        return dataframe_object.to_json(orient='records')

    elif request.method == "POST":

        print("inside post method")
        return request.json
