from flask import Flask

print( "running")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
