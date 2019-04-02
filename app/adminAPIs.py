from flask_restful import Resource
from flask import jsonify, request, make_response
from app.brand import Brand
from flask_api import status
from app.models import Influencer

class AdminRemoveBrandAPI(Resource):
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

        brands = [brand for brand in Brand.objects(__raw__=data)]
        res = []
        for brand in brands:
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            temp['isapproved'] = brand.isapproved
            temp['isactive'] = brand.isactive
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)