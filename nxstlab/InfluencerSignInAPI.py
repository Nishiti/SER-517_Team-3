'''from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

class InfluencerSignIn(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank.')

    @jwt_required
    def post(self):

        data = InfluencerSignIn.parser.parse_args()

        user = next(filter(lambda x: x['email'] == data['email'], users),None)
        if user and user['password'] == data['password']:

            return {"message":"Login Successfull."}

        return {"message":"Invalid credentials."}'''


        # for user in users:
        #     if user['email'] == data['email']:
        #         if user['password'] == data['password']:
        #             return {"message":"Login Successfull."}
        #         else:
        #             return {"message":"The email id and password combination is invalid."}
        #     else:
        #         {"message":"The given username doesn't exist."}



