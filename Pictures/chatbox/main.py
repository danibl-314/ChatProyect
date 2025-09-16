from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index1():
    return "HOLA MUNDO"

@app.route("/index")
def index():
    return render_template('Templates/index.html')

app.run(host='0.0.0.0', port=81, debug=True)