from flask_restful import Resource, Api
from flask import Flask, jsonify, request, json

class AdminSignInAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
