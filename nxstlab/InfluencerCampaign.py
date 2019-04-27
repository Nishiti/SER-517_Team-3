from nxstlab.models import Influencer
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_api import status
from werkzeug.utils import secure_filename
import os
from nxstlab.user import User


class InfluencerCampaign(Resource):
    # API for influencers to update/upload campaign pictures
    def post(self):
        data = dict()
        for key in request.form:
            data[key] = request.form[key]
        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            influencer = Influencer.objects(email=data['email']).first()
            file = request.files['file']
            filename = secure_filename(file.filename)
            fileLocation = os.path.join('static/uploads/influencer_campaign/', filename)
            file.save(fileLocation)
            influencer.campaignImages = '/' + fileLocation

            for key in data:
                if key == 'campaignImages':
                    continue
                else:
                    influencer[key] = data[key]
            influencer.save()
            if 'password' in data:
                User(
                    email=data['email'],
                    password=User.generate_hash(data['password']),
                    role='influencer'
                ).save()
            return make_response(jsonify(role='influencer', message='Influencer Campaign details updated successfully in database'),
                                 status.HTTP_200_OK)
