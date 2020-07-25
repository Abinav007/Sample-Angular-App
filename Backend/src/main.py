from flask import Flask, request, jsonify
from user import User
from config import config
from strings import Strings

app = Flask(__name__)
user = User()
strings = Strings()

@app.route('/health')
def health():
    return 'Python Flask server running on localhost:5000'

@app.route('/user', methods=['GET'])
def getUser():
    firstName = request.args.get('firstName', '').strip()
    if firstName is "":
        return jsonify({'success':True}), 400

    isFound, userData = user.get_user(firstName.strip())

    if not isFound:
        return jsonify({'success':True}), 201
    
    return jsonify(userData)

@app.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    if "firstName" not in data.keys() or "lastName" not in data.keys():
        return jsonify({'success':True}), 400
    return user.add_user(data["firstName"], data["lastName"])

if __name__ == '__main__':
   app.run(host=config["host"], port=config["port"], debug=config["debug"])
