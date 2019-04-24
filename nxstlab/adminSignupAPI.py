from flask_restful import Resource
from flask import jsonify, request, make_response
from nxstlab.admin import Admin
from flask_api import status
from flask_jwt_extended import create_access_token, create_refresh_token
from nxstlab.user import User


class AdminSignupAPI(Resource):
    def post(self):
      print('AdminSignup!')
      data = request.get_json(force=True)
      if Admin.objects(email=data['email']):
        return make_response(jsonify(role='admin', message='Email Address: ' + data['email'] + ' already exists!'),
                             status.HTTP_409_CONFLICT)
      else:

        admin = Admin(
          email = data['email'],
          password=Admin.generate_hash(data['password'])
        ).save()
        User(
            email=data['email'],
            password=User.generate_hash(data['password']),
            role='admin'
        ).save()
        try:
            #access_token = create_access_token(identity=data['email'])
            #refresh_token = create_refresh_token(identity=data['email'])
            #return make_response(jsonify(role='admin', message='admin added successfully in database', access_token=access_token,
            #                             refresh_token=refresh_token, email=data['email']), status.HTTP_201_CREATED)
            return make_response(
                jsonify(role='admin', message='admin added successfully in database', email=data['email']),
                status.HTTP_201_CREATED)
        except:
            return make_response(jsonify(role='admin', message='Admin registration failed!'),
                           status.HTTP_500_INTERNAL_SERVER_ERROR)
