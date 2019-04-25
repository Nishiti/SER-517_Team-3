from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_api import status

from nxstlab.brand import Brand
from nxstlab.models import Influencer
from nxstlab.user import User
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity)


class UserSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        user = User.objects(email=data['email']).first()
        print('password in db = ', data['password'])
        if user:
            print('password received = ', user['password'])
            if User.verify_hash(data['password'], user['password']):
                print('password match!')
                user.authenticated=True
                print('saving ..')
                user.save()
                access_token = create_access_token(identity=data['email'])
                refresh_token = create_refresh_token(identity=data['email'])
                if user['role'] == 'influencer':
                    influencer = Influencer.objects(email=data['email']).first()
                    temp = {}
                    temp['first_name'] = influencer.first_name
                    temp['last_name'] = influencer.last_name
                    temp['email'] = influencer.email
                    temp['big_deal_on_option1'] = influencer.big_deal_on_option1
                    temp['big_deal_on_option2'] = influencer.big_deal_on_option2
                    temp['big_deal_on_option3'] = influencer.big_deal_on_option3
                    temp['big_deal_on_option4'] = influencer.big_deal_on_option4
                    temp['big_deal_on_option5'] = influencer.big_deal_on_option5
                    temp['website_social_media_handles'] = influencer.website_social_media_handles
                    temp['followers'] = influencer.followers
                    temp['areas_of_interest'] = influencer.areas_of_interest
                    temp['gender'] = influencer.gender
                elif user['role'] == 'brand':
                    brand = Brand.objects(email=data['email']).first()
                    temp = {}
                    temp['company_name'] = brand.company_name
                    temp['email'] = brand.email
                    temp['address'] = brand.address
                    temp['isapproved'] = brand.isapproved
                    temp['isactive'] = brand.isactive

                return make_response(jsonify(role=user['role'], influencerobject=temp, message='login successful!', access_token=access_token,
                                                 refresh_token=refresh_token), status.HTTP_200_OK)
            else:
                print('Password mismatch!')
                return make_response(jsonify(role=user['role'], message='Incorrect password!'),
                                        status.HTTP_401_UNAUTHORIZED)
        else:
            return make_response(jsonify(message='Incorrect user email address!'),
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