import unittest
import index
import json
from mongoengine import connect


class TestBrands(unittest.TestCase):

    def setUp(self):
        connect('test_ser517', host='mongodb://localhost/test_ser517')
        index.app.config['TESTING'] = True
        index.app.config["MONGODB_DB"] = 'test_ser517'
        self.app = index.app.test_client()


# Tests the addition of new brand to the database
    def test_signup_correct(self):

        res = self.app.post('/brand', data=json.dumps({
                                                    "company_name": "ruffles",
                                                    "address": "mumbai",
                                                    "email":
                                                    "ruffles@mail.com",
                                                    "password": "abc12345",
                                                    "confirm_password":
                                                    "abc12345"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

# Tests addition of an already existing brand
    def test_signup_incorrect(self):

        res = self.app.post('/brand', data=json.dumps({
                                                    "company_name": "ruffles",
                                                    "address": "mumbai",
                                                    "email":
                                                    "ruffles@mail.com",
                                                    "password": "abc12345",
                                                    "confirm_password":
                                                    "abc12345"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)

# Tests the brand campaign request which is not already in the database
    def test_correct_brand_campaign_request(self):

        res = self.app.post('/brandcampaignrequest', data=json.dumps({
                                                    "campaign_name": "chips",
                                                    "email":
                                                    "ruffles@mail.com",
                                                    "gift_campaign": False,
                                                    "gift_code": False,
                                                    "campaign_info_rqmts":
                                                    "campaign for chips"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

# Tests the brand campaign request which is already in the database
    def test_incorrect_brand_campaign_request(self):

        res = self.app.post('/brandcampaignrequest', data=json.dumps({
                                                    "campaign_name": "chips",
                                                    "email":
                                                    "ruffles@mail.com",
                                                    "gift_campaign": False,
                                                    "gift_code": False,
                                                    "campaign_info_rqmts":
                                                    "campaign for chips"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)

# Tests the approval of brand campaign request which is already in the database
    def test_request_approve(self):

        res = self.app.get('/brandcampaignrequestapprove', data=json.dumps({
                                                    "campaign_name": "chips",
                                                    "email":
                                                    "ruffles@mail.com",
                                                    "status": False}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
