from flask_restful import Resource, Api
from flask import Flask, jsonify, request, json, url_for, render_template, app, make_response
from admin import Admin
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect


class AdminSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

    @app.route('/adminlogin', methods=['GET', 'POST'])
    def login(self):
        # TODO if admin is authenticated
        data = request.get_json(force=True)
        if request.method == 'POST':
            check_user = Admin.objects(email=data['email']).first()
            if check_user:
                if check_password_hash(check_user['password'], data['password']):
                    return redirect(url_for('AdminLandingPage'))
        return render_template('adminlogin.html')

