# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:48:54 2020

@author: uib02367
"""
import random, json
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

"""
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    language=request.args.get('language')
    return render_template('about.html', language=language)
    #return language

@app.route('/About_1')
def about_1():
    #language=request.arg.get('language')
    return "<h1> Hello <h1>"
"""

@app.route('/', methods=['POST','GET'] )
def form_Name():
    if request.method=='POST':
        firstName=request.form["firstname"]
        BACKEND_URL = "http://backend-service/users"
        PARAMS={"firstName":firstName}
        
        r=requests.get(url=BACKEND_URL,params=PARAMS)
        #bool_1=json.loads(r.json()['data'])['Found']
        #return(r.encode())
        #return str(r.status_code)
        if r.status_code==200:
            fName=r.json()['firstName']
            if fName.lower()==firstName.lower():
                lastName=r.json()['lastName']
                return '''
                       <p>Name found!</p>
                       <p>Welcome {} {} </p>
                       '''.format(firstName,lastName)
            else:
                return '''
                       <p>Wrong name fetched from the database</p>
                       <p>Firstname requested: {} </p>
                       <p>Firstname from database: {} </p>
                       '''.format(firstName,fName)
        elif r.status_code==201:
            return '<p>Name not found in the database :(</p>'
        elif r.status_code==500:
            return '<p>ERROR: Check the backend!</p>'
        else:
            return '<p>ERROR: Check your code!</p>'
        #except Exception as e:
        #print(e)
    return '''<form method="POST">
              <h3> Please enter the firstname to be fetched</h3>
              Firstname <input type="text" name="firstname">
              <input type="submit">
              </form>
              '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
