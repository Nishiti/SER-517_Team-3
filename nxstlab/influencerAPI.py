from flask_restful import Resource
from flask import jsonify,request, make_response
from flask_api import status
from nxstlab.models import Influencer
from nxstlab.user import User


class InfluencerSignUpAPI(Resource):
    def post(self):
        data = request.get_json()
        print('data = ', data)
        if Influencer.objects(email=data['email']):
            print("Influencer Signup - Exists!")
            return make_response(jsonify(role='influencer', message='Influencer already exists in the database'),
                                 status.HTTP_409_CONFLICT)
        else:
            print("Influencer Signup!")
            influencer = Influencer()
            for key in data:
                influencer[key] = data[key]
            influencer.save()
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='influencer'
            ).save()

            return make_response(jsonify(role='influencer', message='Influencer added to the database'),
                                 status.HTTP_201_CREATED)