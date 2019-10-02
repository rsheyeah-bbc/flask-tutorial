from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! Does Flask auto-update? Do you need to reload the server? It updated"


@app.route("/api")
def helloapi():
    data = {'Colorado':'Rockies',
            'Boston': 'RedSox'}
    json_data = jsonify(data)

    return json_data