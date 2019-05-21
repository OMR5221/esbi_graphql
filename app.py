# Create the GraphQL endpoint using FLASK
from flask import Flask
from flask_graphql import GraphQLView

# Local imports:
# Get our session to query db
from database import db_session
# from models import *
# get graphql schema that maps our db models:
from schema import schema


app = Flask(__name__)
# Move to config file:
app.debug = True

"""
plant_data = db_session.query(PlantModel).limit(50)
tags_data = db_session.query(TagsModel).limit(50)


for rec in tags_data:
    print(rec.__dict__)
"""

app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql',
                                                schema=schema,
                                                graphiql=True,
                                                context={'session': db_session}))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(port=5005)
