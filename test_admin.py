from flask import Flask, jsonify
from flask_restful import Api
import unittest
import index
import json
from mongoengine import connect
from flask_mongoengine import MongoEngine

class TestAdmin(unittest.TestCase):

	def setUp(self):
		connect('test_ser517', host = 'mongodb://localhost/test_ser517')
		index.app.config['TESTING'] = True
		index.app.config["MONGODB_DB"] = 'test_ser517'
		self.app = index.app.test_client()


#tests the addition of new user to the database
	def test_signup_correct(self):

		res = self.app.post('/admin/signup', data = json.dumps({
													"email":"admin@mail.com",
													"password":"abcadmin"}), content_type = 'application/json')

		self.assertEqual(res.status_code, 201)
		
#tests addition of an already existing user
	def test_signup_incorrect(self):

		res = self.app.post('/admin/signup', data = json.dumps({
													"email":"admin@mail.com",
													"password":"abcadmin1"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 409)

#tests the removal of brand from the database
	def test_remove_invalid_brand(self):

		res = self.app.post('/admin/removebrand', data = json.dumps({"email":"ruffle@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 404)

#tests the removal of a brand by an admin, that already exists in the database
	def test_remove_valid_brand(self):

		res = self.app.post('/admin/removebrand', data = json.dumps({"email":"ruffles@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 200)

#tests the deactivation of a brand that does not exist in the database, by admin
	def test_incorrect_brand_deactivate(self):

		res = self.app.post('/admin/deactivatebrand', data = json.dumps({"email":"lux@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 404)

#tests the deactivation of a valid brand
	def test_correct_brand_deactivate(self):

		res = self.app.post('/admin/deactivatebrand', data = json.dumps({"email":"lays@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 200)

#tests the approval of a brand that does not exist in the database, by the admin
	def test_invalid_brand_approve(self):

		res = self.app.post('/admin/approve/brandsingup', data = json.dumps({"email":"lay@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 404)

#tests the approval of a brand that is in the database
	def test_valid_brand_approve(self):

		res = self.app.post('/admin/approve/brandsingup', data = json.dumps({"email":"lays@mail.com"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 200)

#tests whether the brands with certain filters are fetched from the database
	def test_get_brand_filter(self):

		res = self.app.post('/admin/getBrands', data = json.dumps({"company_name":"z"}), content_type = 'application/json')
		self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
