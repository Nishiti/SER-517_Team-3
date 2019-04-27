import os
from flask_restful import Resource
from flask import jsonify, request, make_response, session, url_for
from nxstlab.brand import Brand
from flask_api import status
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect, secure_filename
from nxstlab.user import User


class BrandAPI(Resource):

    # Performs sign up for the brands
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
                role="brand"
            ).save()

            return make_response(jsonify(role='brand', message='brand added successfully in database'),
                             status.HTTP_201_CREATED)

    # Performs updation of brand profile
    def put(self):
        data = dict()
        for key in request.form:
            data[key] = request.form[key]
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            file = request.files['file']
            filename = secure_filename(file.filename)
            fileLocation = os.path.join('static/uploads/brand_profile/', filename)
            file.save(fileLocation)
            brand.image = '/' + fileLocation

            for key in data:
                if key == 'image':
                    continue
                else:
                    brand[key] = data[key]
            brand.save()
            if 'password' in data:
                user = User.objects(email=data['email']).first()
                user.password = User.generate_hash(data['password'])
                user.save()
            return make_response(jsonify(role='brand', message='brand details updated successfully in database'),
                                 status.HTTP_200_OK)

    # Used to retrieve all the brands from the database
    def get(self):
        brands = [brand for brand in Brand.objects()]
        res = []
        for brand in brands:
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            temp['isapproved'] = brand.isapproved
            temp['image'] = brand.image
            res.append(temp)
        make_response(jsonify(data=res, role='admin', message='list of brands'), status.HTTP_200_OK)
        if not res:
            return make_response(jsonify(role='admin', message='No brand requests left to be approved/denied'),
                                 status.HTTP_204_NO_CONTENT)
        return jsonify(res)


class BrandGetProfileDetails(Resource):

    # Used to get the brand profile details
    def post(self):
        data = request.get_json(force=True)
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            temp['isapproved'] = brand.isapproved
            temp['image'] = brand.image
        return make_response(jsonify(data=temp, role='brand', message='Brand details'), status.HTTP_200_OK)
