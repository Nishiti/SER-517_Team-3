from flask_restful import Resource
from flask import request, app
from flask_restful.representations import json
from app.models import Influencer

class InfluencerSignUpAPI(Resource):
    def post(self):
        data = request.get_json()
        if Influencer.objects(email=data['email']):
            data = {
                "role": "influencer",
                "message": "Influencer already exists in database!"
            }
            response = app.response_class(
                response=json.dumps(data),
                status=409,
                mimetype='application/json'
            )
        else:
            influencer = Influencer(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                confirm_password=data['confirm_password'],
                big_deal_on_option1=data['big_deal_on_option1'],
                big_deal_on_option2=data['big_deal_on_option2'],
                big_deal_on_option3=data['big_deal_on_option3'],
                big_deal_on_option4=data['big_deal_on_option4'],
                big_deal_on_option5=data['big_deal_on_option5'],
                website_social_media_handles=data['website'],
                followers=data['followers']
            ).save()
            data = {
                "role": "influencer",
                "message": "Influencer added in database!"
            }
            response = app.response_class(
                response=json.dumps(data),
                status=201,
                mimetype='application/json'
            )
        return response