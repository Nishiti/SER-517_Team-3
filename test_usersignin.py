from flask import Flask, jsonify
from flask_restful import Api
import unittest
import index
import json
from mongoengine import connect
from flask_mongoengine import MongoEngine

class TestUserSignin(unittest.TestCase):

	def setUp(self):
		connect('test_ser517', host = 'mongodb://localhost/test_ser517')
		index.app.config['TESTING'] = True
		index.app.config["MONGODB_DB"] = 'test_ser517'
		self.app = index.app.test_client()


	def test_signin_correct(self):

		#test signin using correct email and password
		res = self.app.post('/user/signin', data = json.dumps({
													"email":"zux@mail.com",
													"password":"abcdefgh"}), content_type = 'application/json')

		self.assertEqual(res.status_code, 200)
		
	def test_signin_incorrect_password(self):

		#tests signin using incorrect password
		res = self.app.post('/user/signin', data = json.dumps({
													"email":"zux@mail.com",
													"password":"abcdefghi"
													}), content_type = 'application/json')
		self.assertEqual(res.status_code, 401)

	def test_signin_incorrect_email(self):

		#tests signin using incorrect password
		res = self.app.post('/user/signin', data = json.dumps({
													"email":"bux@mail.com",
													"password":"abcdefgh"
													}), content_type = 'application/json')
		self.assertEqual(res.status_code, 401)

if __name__ == "__main__":
    unittest.main()
