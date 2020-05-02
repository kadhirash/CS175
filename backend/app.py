from flask import Flask, request
from pymongo import MongoClient
from keys import mongo_uri
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient(mongo_uri)
db = client['readit']
users = db['users']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return {"hello": "World"}

@app.route('/api', methods=['GET', 'POST'])
def api():
    return {"hello": "World"}

@app.route('/api/login', methods=['GET','POST'])
def login():
    
    if request.method == "POST":
        data = request.get_json()
        if data == None:
            return {"message": "Error occured. POST body empty"}

        user = users.find_one({"email": data['email']})    
        if user == None:
            return {"message":"That user does not exist"}
        
        if check_password_hash(user.password_hash,data['password']):
            return {"message":"Login Successful"}
        

    return {"message": "You probably did not send the right type of request."}

@app.route('/api/signup', methods=['GET','POST'])
def signup():

    if request.method == "POST":

        data = request.get_json()
        if data == None:
            return {"message": "Error occured. POST body empty"}

        data['password_hash'] = generate_password_hash(data['password'])
        del data['password']
        # users.insert_one(data)
        return {"message":"Signup Successful"}

    return {"message": "You probably submitted the wrong type of request."}

 


if __name__ == "__main__":
    app.run(debug=True)