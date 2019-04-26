import unittest
import index
import json
from mongoengine import connect


class TestUserSignin(unittest.TestCase):

    def setUp(self):
        connect('test_ser517', host='mongodb://localhost/test_ser517')
        index.app.config['TESTING'] = True
        index.app.config["MONGODB_DB"] = 'test_ser517'
        self.app = index.app.test_client()

# Test signin using correct email and password
    def test_signin_correct(self):

        res = self.app.post('/user/signin', data=json.dumps({
                                                    "email": "zux@mail.com",
                                                    "password": "abcdefgh"}),
                            content_type='application/json')

        self.assertEqual(res.status_code, 200)

# Tests signin using incorrect password
    def test_signin_incorrect_password(self):

        res = self.app.post('/user/signin', data=json.dumps({
                                                    "email": "zux@mail.com",
                                                    "password": "abcdefghi"
                                                    }),
                            content_type='application/json')
        self.assertEqual(res.status_code, 401)


# Tests signin using incorrect email
    def test_signin_incorrect_email(self):

        res = self.app.post('/user/signin', data=json.dumps({
                                                    "email": "bux@mail.com",
                                                    "password": "abcdefgh"
                                                    }),
                            content_type='application/json')
        self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
    unittest.main()
