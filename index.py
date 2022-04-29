from db_model import BarChart
from flask import Flask, jsonify
from flask_cors import CORS
from functions import getBarChart

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home():
    return 'home!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<id>/<num>')
def show_post(id, num):
    result = "아이디:{id} , 번호: {num}"
    return jsonify(result)

@app.route('/test')
def testAPI():
    stmt = getBarChart()
    return jsonify(stmt)
