# Getting started with Flask, graphQL, and Postgres
## Command line
- python3 -m venv venv
- source venv/bin/activate
- pip install flask flask-graphql flask-migrate sqlalchemy graphene graphene-sqlalchemy psycopg2-binary flask-cors
- pip freeze > requirements.txt (Note: check error messages for incompatible versions and change versions accordingly)
- pip install -r requirements.txt

### app.py:
```
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

## Command line
python app.py (or flask run)

## Browser
localhost:5000

## App
- create generator/users.csv
- create seed.py

### app.py: Connect db and write user model
```
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///forage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '' % self.id

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

## Command line
- python seed.py

## Browser
localhost:5000/graphql-api

### get all users:
```
{
  allUsers{
    edges{
      node{
        username
        email
      }
    }
  }
}
```

### add user:
```
mutation {
  addUser(
    username:"testuser2",
    email:"testuser2@test.com"){
    user{
      username
      email
    }
  }
}
```

## git tag
```
git tag -a <tagname> -m '<message>'
git push origin --tags  or git push origin <tag>
```