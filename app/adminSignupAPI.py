from flask_restful import Resource
from flask import jsonify, request, make_response
from app.admin import Admin
from flask_api import status
from werkzeug.security import generate_password_hash, check_password_hash


class AdminSignupAPI(Resource):
    def post(self):

      data = request.get_json(force=True)

      if Admin.objects(email=data['email']):
        return make_response(jsonify(role='admin', message='Email Address: ' + data['email'] + ' already exists!'),
                             status.HTTP_409_CONFLICT)

      else:

        admin = Admin(
          first_name = data['first_name'],
          last_name = data['last_name'],
          email = data['email'],
          password=generate_password_hash(data['password'])
        ).save()
        return make_response(jsonify(role='admin', message='admin added successfully in database'),
                             status.HTTP_201_CREATED)