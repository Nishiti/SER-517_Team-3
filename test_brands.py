from flask import Flask, jsonify
from flask_restful import Api
import unittest
import index
import json
from mongoengine import connect
from flask_mongoengine import MongoEngine

class TestBrands(unittest.TestCase):

	def setUp(self):
		connect('test_ser517', host = 'mongodb://localhost/test_ser517')
		index.app.config['TESTING'] = True
		index.app.config["MONGODB_DB"] = 'test_ser517'
		self.app = index.app.test_client()


#tests the addition of new user to the database
	def test_signup_correct(self):

		res = self.app.post('/brand', data = json.dumps({"company_name":"ruffles",
													"address":"mumbai",
													"email":"ruffles@mail.com",
													"password":"abc12345",
													"confirm_password":"abc12345"}), content_type = 'application/json')

		self.assertEqual(res.status_code, 201)
		
#tests addition of an already existing user
	def test_signup_incorrect(self):

		res = self.app.post('/brand', data = json.dumps({"company_name":"ruffles",
													"address":"mumbai",
													"email":"ruffles@mail.com",
													"password":"abc12345",
													"confirm_password":"abc12345"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 409)

if __name__ == "__main__":
    unittest.main()
