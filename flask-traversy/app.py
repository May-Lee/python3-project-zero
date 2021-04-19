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

# Create a class (model)
class ExtensionURI(db.Model):
    '''
    This class definition uses vocabulary from Tahoe-LAFS but is not functionally
    similar. I use these terms to begin an inner dialogue with myself in this example.
    In Tahoe-LAFS, the URI extension is a collection of metadata about a share.
    '''
    id = db.Column(db.Integer, primary_key=True)
    codec_name = db.Column(db.String(100))
    codec_params = db.Column(db.String(100))
    crypttext_hash = db.Column(db.String(100), unique=True)
    crypttext_root_hash = db.Column(db.String(100), unique=True)
    needed_shares = db.Column(db.Integer)
    num_segments = db.Column(db.Integer)
    segment_size = db.Column(db.Integer)
    share_root_hash = db.Column(db.String(100), unique=True)
    size = db.Column(db.Integer)
    tail_codec_params = db.Column(db.String(100))
    # TODO: learn to use None for absent parameters
    def __ini__(self, codec_name, codec_params, crypttext_hash, crypttext_root_hash,
                needed_shares, num_segments, segment_size, share_root_hash, size, 
                tail_codec_params):
        self.codec_name = codec_name
        self.codec_params = codec_params
        self.crypttext_hash = crypttext_hash
        self.crypttext_root_hash = crypttext_root_hash
        self.needed_shares = needed_shares
        self.num_segments = num_segments
        self.segment_size = segment_size
        self.share_root_hash = share_root_hash
        self.size = size
        self.tail_codec_params = tail_codec_params

# Extension Schema
class ExtensionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'codec_name', 'codec_params', 'crypttext_hash', 'crypttext_root_hash',
                  'needed_shares', 'num_segments', 'segment_size', 'share_root_hash', 'size'
                  'tail_codec_params')
# Init schema
extension_schema = ExtensionSchema()
extensions_schema = ExtensionSchema(many=True)

# Run server
if __name__ == '__main__':
    app.run(debug=True) # debug for development
