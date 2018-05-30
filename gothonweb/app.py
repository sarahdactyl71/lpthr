from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello')
def index():
    #these are like params in url if none are there it will say
    #"Hello nobody", if you have something like http://localhost:5000/hello?name=Frank
    # It will say "Hello Frank"
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hello')

    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
