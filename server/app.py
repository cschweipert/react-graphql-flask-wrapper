from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.debug = True

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    