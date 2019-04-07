from flask_restful import Resource
from flask import jsonify, request, url_for, render_template, make_response, session
from flask_api import status
from app.admin import Admin

class AdminSignoutAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        admin = Admin.objects(email=data['email']).first()
        if not admin.is_authenticated():
            print('user never logged in!')
            return make_response(jsonify(role='admin', message='user never logged in'),
                                 status.HTTP_200_OK)
        else:
            if admin:
                admin.authenticated = False
                admin.save()
                return make_response(jsonify(role='admin', message='logged out'),
                                     status.HTTP_200_OK)
            else:
                return make_response(jsonify(role='admin', message='Incorrect user email address!'),
                                     status.HTTP_401_UNAUTHORIZED)