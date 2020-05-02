from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return {"hello": "World"}
    
@app.route('/api', methods=['GET', 'POST'])
def api():
    return {"hello": "World"}

@app.route('/api/login', methods=['GET','POST'])
def login():

    return {"message": "Login Success"}

@app.route('/api/signup', methods=['GET','POST'])
def signup():

    return {"message": "Signup Success"}

 


if __name__ == "__main__":
    app.run(debug=True)