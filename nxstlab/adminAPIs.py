from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import jsonify, request, make_response
from nxstlab.brand import Brand
from flask_api import status
from nxstlab.models import Influencer

class AdminRemoveBrandAPI(Resource):
    @jwt_required
    def post(self):
        data = request.get_json(force=True)
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            brand.delete()
            return make_response(jsonify(role='brand', message='brand has been removed from database'),
                                 status.HTTP_200_OK)

class AdminDeactivateBrandAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email']).first()
            brand['isactive'] = False
            brand.save()

            return make_response(jsonify(role='admin', message='brand has been deactivated'), status.HTTP_200_OK)


class AdminRemoveInfluencerAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='influencer does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            user = Influencer.objects(email=data['email']).first()
            user.delete()
            return make_response(jsonify(role='admin', message='influencer has been removed from database'),
                                 status.HTTP_200_OK)


class AdminDeactivateBrandAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='Influencer does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            user = Influencer.objects(email=data['email']).first()
            user['isactive'] = False
            user.save()

            return make_response(jsonify(role='admin', message='Influencer has been deactivated'), status.HTTP_200_OK)


class AdminApproveBrandSignupAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email']).first()
            if not brand['isapproved']:
                brand.isapproved = True
                brand.isactive = True
                brand.save()
                return make_response(jsonify(role='admin', message='brand is approved'), status.HTTP_200_OK)
            else:
                return make_response(jsonify(role='admin', message='brand is already approved'), status.HTTP_200_OK)

class AdminGetBrandsWithFilterAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        name = data['company_name']
        brands = [brand for brand in Brand.objects(company_name__contains=name)]
        res = []
        for brand in brands:
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)


class AdminGetInfluencersWithFilterAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        name = data['name']
        print('name = ', name)
        influencers = [influencer for influencer in Influencer.objects(first_name__contains=name)]
        print('influencers = ', influencers)
        influencers.extend([influencer for influencer in Influencer.objects(last_name__contains=name)])
        res = []
        for user in influencers:
            temp = dict()
            temp['first_name'] = user.first_name
            temp['last_name'] = user.last_name
            temp['email'] = user.email
            temp['website_social_media_handles'] = user.website_social_media_handles
            temp['big_deal_on_option1'] = user.big_deal_on_option1
            temp['big_deal_on_option2'] = user.big_deal_on_option2
            temp['big_deal_on_option3'] = user.big_deal_on_option3
            temp['big_deal_on_option4'] = user.big_deal_on_option4
            temp['big_deal_on_option5'] = user.big_deal_on_option5
            temp['followers'] = user.followers
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of influencers for given filter'),
                             status.HTTP_200_OK)