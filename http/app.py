from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_name = "Home")

app.run(debug=True,host='0.0.0.0',port='80')
