from flask_restful import Resource
from flask import request, app
from flask_restful.representations import json
from models import Influencer

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
                category=data['category'],
                youtube=data['youtube'],
                IGStoryViews=data['IGStoryViews'],
                followers=data['followers'],
                AvgLikes=data['AvgLikes'],
                AvgComments=data['AvgComments'],
                Gender=data['Gender'],
                email=data['email'],
                website=data['website'],
                social_media_handles=data['instagram_handle']
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