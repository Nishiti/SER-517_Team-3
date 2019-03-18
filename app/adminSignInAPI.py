from flask_restful import Resource, Api
from flask import Flask, jsonify, request, json, url_for, render_template, app, make_response, session
from flask_api import status
from admin import Admin
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect


class AdminSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

    @app.route('/adminlogin', methods=['GET', 'POST'])
    def login(self):
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

