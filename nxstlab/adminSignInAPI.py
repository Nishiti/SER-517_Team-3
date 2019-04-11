from flask_restful import Resource
from flask import jsonify, request, url_for, render_template, make_response, session
from flask_api import status
from nxstlab.admin import Admin
from flask_login import current_user, login_user
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect


class AdminSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        admin = Admin.objects(email=data['email']).first()
        print('password in db = ', data['password'])
        print('password received = ', admin['password'])
        if admin:
            if Admin.verify_hash(data['password'], admin['password']):
                print('password match!')
                admin.authenticated=True
                print('saving ..')
                admin.save()
                access_token = create_access_token(identity=data['email'])
                refresh_token = create_refresh_token(identity=data['email'])
                return make_response(jsonify(role='admin', message='login successful!', access_token=access_token,
                                                 refresh_token=refresh_token, email=data['email']), status.HTTP_200_OK)
            else:
                print('Password mismatch!')
                return make_response(jsonify(role='admin', message='Incorrect password!'),
                                        status.HTTP_401_UNAUTHORIZED)
        else:
            return make_response(jsonify(role='admin', message='Incorrect user email address!'),
                                     status.HTTP_401_UNAUTHORIZED)

# Example resource protected by JWT, to be removed later
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return make_response(jsonify(answer='100'), status.HTTP_200_OK)

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return make_response(jsonify(access_token=access_token))