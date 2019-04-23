from flask import Flask, jsonify
from flask_restful import Api
import unittest
import index
import json
from mongoengine import connect
from flask_mongoengine import MongoEngine

class TestInfluencer(unittest.TestCase):

	def setUp(self):
		connect('test_ser517', host = 'mongodb://localhost/test_ser517')
		index.app.config['TESTING'] = True
		index.app.config["MONGODB_DB"] = 'test_ser517'
		self.app = index.app.test_client()


	def test_signup_correct(self):

		#tests the addition of new user to the database
		res = self.app.post('/influencer/signup', data = json.dumps({"first_name":"first",
													"last_name":"first",
													"email":"zux@mail.com",
													"password":"abcdefgh",
													"confirm_password":"abcdefgh"}), content_type = 'application/json')

		self.assertEqual(res.status_code, 201)
		
	def test_signup_incorrect(self):

		#tests addition of an already existing user
		res = self.app.post('/influencer/signup', data = json.dumps({"first_name":"first",
													"last_name":"first",
													"email":"zux@mail.com",
													"password":"abcdefgh",
													"confirm_password":"abcdefgh"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 409)

if __name__ == "__main__":
    unittest.main()
