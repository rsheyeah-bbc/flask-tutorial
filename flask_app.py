from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! Does Flask auto-update? Do you need to reload the server? It updated"