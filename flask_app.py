from flask import Flask,jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! Does Flask auto-update? Do you need to reload the server? It updated"


@app.route("/api")
def helloapi():
    data_dict = {'Colorado':'Rockies',
            'Boston': 'RedSox'}

    studentData = {
        'name': ['Tig', 'Tac', 'Toe'],
        'age': [1, 2, 3],
        'city': ['Disney', 'Cbeebies', 'CartoonNetwork']
    }

    json_data = jsonify(data_dict)

    dataframe_object = pd.DataFrame(studentData)


    #return json_data
    return dataframe_object.to_json(orient='records')