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

@app.route('/form_name', methods=['POST','GET'] )
def form_Name():
    if request.method=='POST':
        firstName=request.form["firstname"]
        r=requests.post('http://httpbin.org/post?'+"firstname="+firstName, json={'Found':random.choice([True, False]), 'LastName':'Doe'})
        bool_1=json.loads(r.json()['data'])['Found']
       
        if bool_1:
            lastName=json.loads(r.json()['data'])['LastName']
            return '''
                   <p>Name found!</p>
                   <p>Welcome {} {} </p>
                   '''.format(firstName,lastName)
        else:
            return '<p>Name not found :(</p>'
    return '''<form method="POST">
              <h3> Please enter the firstname to be fetched</h3>
              Firstname <input type="text" name="firstname">
              <input type="submit">
              </form>
              '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
