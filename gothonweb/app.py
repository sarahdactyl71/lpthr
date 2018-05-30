from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World"
    return redner_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
