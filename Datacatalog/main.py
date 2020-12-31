from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from jinja2 import Environment, FileSystemLoader
from util import *


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def layout():
    return render_template('layout.html', username=get_username())

@app.route('/datacatalog')
def datacatalog():
    return render_template('datacatalog.html', username=get_username())

@app.route('/dynamodb')
def dynamodb():
    return render_template('dynamodb.html', username=get_username())

@app.route('/s3')
def s3():
    return render_template('s3.html', username=get_username())

if __name__ == '__main__':
    app.run(debug=True)
