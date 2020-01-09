# IMPORTS
from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello_handler():
    return 'world of python'

# $env:FLASK_APP="index.py";flask run
# export FLASK_APP=index.py && flask run
