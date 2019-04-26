import unittest
import index
import json
from mongoengine import connect


class TestAdmin(unittest.TestCase):

    def setUp(self):
        connect('test_ser517', host='mongodb://localhost/test_ser517')
        index.app.config['TESTING'] = True
        index.app.config["MONGODB_DB"] = 'test_ser517'
        self.app = index.app.test_client()


# Tests the addition of new admin to the database
    def test_signup_correct(self):

        res = self.app.post('/admin/signup', data=json.dumps({
                                                    "email": "admin@mail.com",
                                                    "password": "abcadmin"}),
                            content_type='application/json')

        self.assertEqual(res.status_code, 201)

# Tests addition of an already existing admin
    def test_signup_incorrect(self):

        res = self.app.post('/admin/signup', data=json.dumps({
                                                    "email": "admin@mail.com",
                                                    "password": "abcadmin1"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)

# Tests the removal of nonexisting brand from the database
    def test_remove_invalid_brand(self):

        res = self.app.post('/admin/removebrand', data=json.dumps({
                                                         "email":
                                                         "ruffle@mail"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the removal of a brand by an admin, that already exists in the database
    def test_remove_valid_brand(self):

        res = self.app.post('/admin/removebrand', data=json.dumps({
                                                        "email":
                                                        "ruffles@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests the deactivation of a brand that does not exist in the database,
# by admin
    def test_incorrect_brand_deactivate(self):

        res = self.app.post('/admin/deactivatebrand', data=json.dumps({
                                                        "email":
                                                        "lux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the deactivation of a valid brand
    def test_correct_brand_deactivate(self):

        res = self.app.post('/admin/deactivatebrand', data=json.dumps({
                                                        "email":
                                                        "lays@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests the approval of a brand that does not exist in the database,
# by the admin
    def test_invalid_brand_approve(self):

        res = self.app.post('/admin/approve/brandsingup', data=json.dumps({
                                                        "email":
                                                        "lay@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the approval of a brand that is in the database
    def test_valid_brand_approve(self):

        res = self.app.post('/admin/approve/brandsingup', data=json.dumps({
                                                        "email":
                                                        "lays@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests whether the brands with company name as filter,
# are fetched from the database
    def test_get_brand_filter(self):

        res = self.app.post('/admin/getBrands', data=json.dumps({
                                                "company_name": "lays"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Tests that brands that satisfy multiple filters are fetched from the database
    def test_get_all_brands(self):

        res = self.app.post('/admin/getAllBrands', data=json.dumps({
                                                    "email":
                                                    "ruffles@mail.com"}),
                            content_type='application/json')
        print("here=", json.loads(res.data)['data'])
        self.assertEqual(res.status_code, 200)

# Tests the deactivation of an influencer that does not exist in the database,
# by admin
    def test_incorrect_influencer_deactivate(self):

        res = self.app.post('/admin/deactivateinf', data=json.dumps({
                                                        "email":
                                                        "lax@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

# Tests the deactivation of a valid influencer
    def test_correct_influencer_deactivate(self):

        res = self.app.post('/admin/deactivateinf', data=json.dumps({
                                                        "email":
                                                        "zux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
