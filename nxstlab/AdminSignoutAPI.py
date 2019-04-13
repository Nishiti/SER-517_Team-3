from flask_jwt_extended import jwt_required, get_raw_jwt, jwt_refresh_token_required
from flask_restful import Resource
from flask import jsonify, request, url_for, render_template, make_response, session
from flask_api import status
from nxstlab.admin import Admin
from nxstlab.revokedtoken import RevokedToken


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

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return make_response(jsonify(role='admin', message='Access token has been revoked!'),
                                 status.HTTP_200_OK)
        except:
            return make_response(jsonify(role='admin', message='Something went wrong!'),
                                 status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return make_response(jsonify(role='admin', message='Refresh token has been revoked!'),
                                 status.HTTP_200_OK)
        except:
            return make_response(jsonify(role='admin', message='Something went wrong!'),
                                 status.HTTP_500_INTERNAL_SERVER_ERROR)
