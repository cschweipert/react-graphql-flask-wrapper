from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView

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

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query)

app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # GraphiQL interface
    )
)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    