from flask_restful.representations import json

from nxstlab.models import Influencer
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_api import status

class InfluencerUpdateProfile(Resource):
    def put(self):
        data = request.get_json(force=True)
        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            influencer = Influencer.objects(email=data['email']).first()
            data = request.get_json()
            for key in data:
                if key == 'image':
                    file = request.files['image']
                    # extension = os.path.splitext(file.filename)[1]
                    #influencer['image'] = imagefile.read()
                    influencer.image.put(file)
                else:
                    influencer[key] = data[key]
            influencer.save()
            return make_response(jsonify(role='influencer', message='Influencer details updated successfully in database'),
                                 status.HTTP_200_OK)


    def get(self, id):
        influencers = [influencer for influencer in Influencer.objects()]
        res = []
        for influencer in influencers:
            temp = dict()
            temp['first_name'] = influencer.first_name
            temp['last_name'] = influencer.last_name
            temp['email'] = influencer.email
            temp['website_social_media_handles'] = influencer.website_social_media_handles
            temp['followers'] = influencer.followers
            temp['areas_of_interest'] = influencer.areas_of_interest
            temp['image'] = influencer.image
            print('image retreived')
            # temp['image'] = json.loads(temp['image'].data.decode('utf-8'))
            temp['image'] = temp['image'].data.decode('utf-8')
            print('image decoded')
            res.append(temp)
        return make_response(jsonify(data=res, role='influencer', message='Influencer profile details'),
                             status.HTTP_200_OK)
