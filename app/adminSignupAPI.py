from flask_restful import Resource
from flask import jsonify, request, make_response
from app.admin import Admin
from flask_api import status

class AdminSignupAPI(Resource):
    def post(self):

      data = request.get_json(force=True)

      if Admin.objects(email=data['email']):
        return make_response(jsonify(role='admin', message='admin already exists in database'),
                             status.HTTP_409_CONFLICT)

      else:
        admin = Admin(
          first_name = data['first_name'],
          last_name = data['last_name'],
          email = data['email'],
          password = data['password']
        ).save()

        return make_response(jsonify(role='admin', message='admin added successfully in database'),
                             status.HTTP_201_CREATED)