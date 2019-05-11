from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_name = "Home")

app.run(debug=True,host='0.0.0.0',port='80')
