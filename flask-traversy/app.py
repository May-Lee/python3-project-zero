from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) # create file path

# Create a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Init DB and Marshmallow (serialization, deserialization, validation etc.)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Run server
if __name__ == '__main__':
    app.run(debug=True) # debug for development
