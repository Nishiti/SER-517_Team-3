from flask_restful import Resource
from flask import jsonify,request, make_response
from flask_api import status
from nxstlab.models import Influencer
from nxstlab.user import User


class InfluencerSignUpAPI(Resource):
    def post(self):
        print("Influencer Signup - Exists!")
        data = request.get_json()
        print('data = ', data)
        if Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer already exists in the database'),
                                 status.HTTP_409_CONFLICT)
        else:
            print("Influencer Signup!")
            influencer = Influencer()
            for key in data:
                influencer[key] = data[key]
            influencer.save()
            '''influencer = Influencer(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                confirm_password=data['confirm_password']
            ).save()
            if 'big_deal_on_option1' in data:
                influencer.save(big_deal_on_option1=data['big_deal_on_option1'])
            if 'big_deal_on_option2' in data:
                influencer.save(big_deal_on_option2=data['big_deal_on_option2'])
            if 'big_deal_on_option3' in data:
                influencer.save(big_deal_on_option3=data['big_deal_on_option3'])
            if 'big_deal_on_option4' in data:
                influencer.save(big_deal_on_option4=data['big_deal_on_option4'])
            if 'big_deal_on_option5' in data:
                influencer.save(big_deal_on_option5=data['big_deal_on_option5'])

            if 'website_social_media_handles' in data:
                influencer.save(website_social_media_handles=data['website_social_media_handles'])
            if 'followers' in data:
                influencer.save(followers=data['followers'])
            if 'areas_of_interest' in data:
                influencer.save(areas_of_interest=data['areas_of_interest'])'''
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='influencer'
            ).save()

            return make_response(jsonify(role='influencer', message='Influencer added to the database'),
                                 status.HTTP_201_CREATED)