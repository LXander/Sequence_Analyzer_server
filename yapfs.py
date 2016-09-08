import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash,jsonify
import comparision
import json

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/get_quality',methods=['GET','POST'])
def get_quality():
    if request.method=='POST':

        print (request.json)
        str = request.json
        print (str.keys())
        quality = comparision.comparision(request.json)

        return jsonify(quality)
    else:
        return "hello post"


if __name__ == '__main__':
    app.run(debug=True,port=8388)
