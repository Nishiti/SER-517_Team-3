from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
app.secret_key = 'vihar'
api = Api(app)

class InfluencerSignIn(Resource):

	def post(self):



api.add_resource(InfluencerSignIn, '/influencersignin')
app.run(port=5000, debug=True)

