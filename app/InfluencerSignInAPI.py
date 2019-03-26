from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
app.secret_key = 'vihar'
api = Api(app)

users = [
	{
		'email':'bob',
		'password':'abc'
	}
]

class InfluencerSignIn(Resource):

	def post(self):

	data = InfluencerSignIn.parser.parse_args()

	for user in users:
		if user['email'] == data['email']:
			if user['password'] == data['password']:
				return {"message":"Login Successfull."}
			else:
				return {"message":"The email id and password combination is invalid."}
		else:
			{"message":"The given username doesn't exist."}


api.add_resource(InfluencerSignIn, '/influencersignin')
app.run(port=5000, debug=True)

