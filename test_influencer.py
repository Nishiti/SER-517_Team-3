import unittest
import index
import json
from mongoengine import connect


class TestInfluencer(unittest.TestCase):

    def setUp(self):
        connect('test_ser517', host='mongodb://localhost/test_ser517')
        index.app.config['TESTING'] = True
        index.app.config["MONGODB_DB"] = 'test_ser517'
        self.app = index.app.test_client()

# Tests the addition of new user to the database
    def test_signup_correct(self):

        res = self.app.post('/influencer/signup', data=json.dumps({
                                                    "first_name": "first",
                                                    "last_name": "first",
                                                    "email": "zux@mail.com",
                                                    "password": "abcdefgh",
                                                    "confirm_password":
                                                    "abcdefgh"}),
                            content_type='application/json')

        self.assertEqual(res.status_code, 201)

# Tests addition of an already existing user
    def test_signup_incorrect(self):

        res = self.app.post('/influencer/signup', data=json.dumps({
                                                    "first_name": "first",
                                                    "last_name": "first",
                                                    "email": "zux@mail.com",
                                                    "password": "abcdefgh",
                                                    "confirm_password":
                                                    "abcdefgh"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)

# Tests whether the influencers with name as filter
# are fetched from the database
    def test_get_influencer_filter(self):

        res = self.app.post('/admin/getInfluencers', data=json.dumps({
                                                        "name": "k"}),
                            content_type='application/json')
        # print("here=", json.loads(res.data)['data'])
        self.assertEqual(res.status_code, 200)

# Tests that the influencers that satisfy multiple filters
# are fetched from the database
    def test_get_all_influencers(self):

        res = self.app.post('/admin/getAllInfluencer', data=json.dumps({
                                                       "first_name": "first"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests the removal of an invalid influencer from database, by the admin
    def test_remove_influencer_invalid(self):

        res = self.app.post('/admin/removeInfluencers', data=json.dumps({
                                                        "email": "first"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the removal of an valid influencer from database, by the admin
    def test_remove_influencer_valid(self):

        res = self.app.post('/admin/removeInfluencers', data=json.dumps({
                                                    "email": "zux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests the updation of invalid influencer profile
    def test_incorrect_influencer_update(self):

        res = self.app.put('/influencer/updateprofile', data=json.dumps({
                                                        "email": "first"}),
                           content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the updation of valid influencer profile
    def test_correct_influencer_update(self):

        res = self.app.put('/influencer/updateprofile', data=json.dumps({
                                                        "email":
                                                        "zux@mail.com"}),
                           content_type='application/json')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
