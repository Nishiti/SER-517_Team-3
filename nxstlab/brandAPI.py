from flask_restful import Resource
from flask import jsonify, request, make_response, session, url_for
from nxstlab.brand import Brand
from flask_api import status
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from nxstlab.user import User


class BrandAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        if Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand already exists in database'),
                             status.HTTP_409_CONFLICT)
        else:
            Brand(
              company_name=data['company_name'],
              address=data['address'],
              email=data['email'],
              password=data['password'],
              confirm_password=data['confirm_password']
            ).save()
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='brand'
            ).save()
            return make_response(jsonify(role='brand', message='brand added successfully in database'),
                             status.HTTP_201_CREATED)

    def put(self):
        data = request.get_json(force=True)
        # handle case for invalid request
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            data = request.get_json()
            for key in data:
                brand[key] = data[key]
            brand.save()
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='brand'
            ).save()
            return make_response(jsonify(role='brand', message='brand details updated successfully in database'),
                                 status.HTTP_200_OK)

    def get(self):
        brands = [brand for brand in Brand.objects()]
        res = []
        for brand in brands:
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            temp['isapproved'] = brand.isapproved
            res.append(temp)
        make_response(jsonify(data=res, role='admin', message='list of brands'), status.HTTP_200_OK)
        if not res:
            return make_response(jsonify(role='admin', message='No brand requests left to be approved/denied'),
                                 status.HTTP_204_NO_CONTENT)
        return jsonify(res)
