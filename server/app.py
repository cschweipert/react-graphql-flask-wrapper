from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from models import connect_db
from schema import schema

app = Flask(__name__)
CORS(app)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///forage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
connect_db(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # GraphiQL interface
    )
)

@app.route('/', methods=['GET', 'POST']) # define methods to avoid 405
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    