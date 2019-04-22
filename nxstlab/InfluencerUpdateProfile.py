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
                    imagefile = request.files['imagefile.jpg']
                    #influencer['image'] = imagefile.read()
                    influencer.image.put(imagefile)
                else:
                    influencer[key] = data[key]
            influencer.save()
            return make_response(jsonify(role='infuencer', message='Influencer details updated successfully in database'),
                                 status.HTTP_200_OK)