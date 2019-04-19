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
              company_address=data['company_address'],
              email=data['email'],
              password=data['password']
            ).save()
            User(
                email=data['email'],
                password=User.generate_hash(data['password']),
                role='influencer'
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
            temp['isactive'] = brand.isactive
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands'),
                             status.HTTP_200_OK)


class BrandSignInAPI(Resource):
    def post(self):

        data = request.get_json(force=True)
        session['email'] = data['email']
        brand = Brand.objects(email=data['email']).first()
        if brand.is_authenticated:
            return redirect(url_for('BrandHomePage'))
        if brand:
            if check_password_hash(brand['password'], data['password']):
                return redirect(url_for('BrandHomePage'))
            else:
                return make_response(jsonify(role='brand', message='brand exists, but password is not matching'),
                                     status.HTTP_401_UNAUTHORIZED)
        else:
            return make_response(jsonify(role='brand', message='brand not found in database, check email again'),
                                 status.HTTP_404_NOT_FOUND)
    def get(self):
        render_template('adminlogin.html')

        data = request.get_json(force=True)
        if request.method == 'POST':
            session['email'] = request.form['email']
            check_user = Admin.objects(email=data['email']).first()
            if check_user.is_authenticated:
                return redirect(url_for('AdminLandingPage'))
            if check_user:
                if check_password_hash(check_user['password'], data['password']):
                    return redirect(url_for('AdminLandingPage'))
                else:
                    return make_response(jsonify(role='admin', message='Incorrect password!'),
                                         status.HTTP_401_UNAUTHORIZED)
            else:
                return make_response(jsonify(role='admin', message='Incorrect user email address!'),
                                     status.HTTP_401_UNAUTHORIZED)
        return render_template('adminlogin.html')