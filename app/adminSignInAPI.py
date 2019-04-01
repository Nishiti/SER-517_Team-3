from flask_restful import Resource
from flask import jsonify, request, url_for, render_template, make_response, session
from flask_api import status
from app.admin import Admin
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect


class AdminSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        admin = Admin.objects(email=data['email']).first()
        if admin.is_authenticated():
            print('user already logged in!')
            #return redirect(url_for('admin.html'))
        else:
            print('not logged in!')
            if admin:
                if check_password_hash(admin['password'], data['password']):
                    print('password match!Success')
                    admin.authenticated=True
                    print('saving ..')
                    admin.save()
                    # session['email'] = admin['email']
                    # return redirect(url_for('admin.html'))
                else:
                    print('Password mismatch!')
                    return make_response(jsonify(role='admin', message='Incorrect password!'),
                                        status.HTTP_401_UNAUTHORIZED)
            else:
                return make_response(jsonify(role='admin', message='Incorrect user email address!'),
                                     status.HTTP_401_UNAUTHORIZED)
        #return render_template('adminlogin.html')


