from flask_restful.representations import json
from nxstlab.models import Influencer
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_api import status
from werkzeug.utils import secure_filename
import os

from nxstlab.user import User


class UploadProfileImage(Resource):
    # post method to upload profile image
    def post(self):
        data = dict()
        data['email'] = request.form['email']

        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            influencer = Influencer.objects(email=data['email']).first()
            file = request.files['file']
            filename = secure_filename(file.filename)
            fileLocation = os.path.join('static/uploads/influencer_profile_pictures/', filename)
            file.save(fileLocation)
            influencer.image = '/' + fileLocation
            influencer.save()
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='influencer'
            ).save()
            return make_response(jsonify(role='influencer', message='Influencer details updated successfully in database'),
                                 status.HTTP_200_OK)