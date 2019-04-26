from flask import Flask, jsonify, request, make_response
from flask_api import status
from flask_restful import Resource, Api, reqparse
from nxstlab.BrandCampaign import BrandCampaign
from mongoengine import connect


class BrandCampaignRequestApproveAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('campaign_name', type=str, required=True, help='This field cannot be blank.')
	parser.add_argument('email', type=str, required=True, help='This field cannot be blank.')
	parser.add_argument('status', type=bool, required=True, help='This field cannot be blank.')

	def post(self):
		data = BrandCampaignRequestApproveAPI.parser.parse_args()
		campaign = BrandCampaign.objects(email=data['email'], campaign_name=data['campaign_name']).first()
		if data['status'] == True:
			campaign.isApproved = True
			campaign.isDenied = False
			campaign.save()
			return make_response(jsonify(role='admin', message='Campaign: ' + data['campaign_name'] + ' request approved!'),
                                 status.HTTP_201_CREATED)
		else:
			campaign.isApproved = False
			campaign.isDenied = True
			campaign.save()
			return make_response(jsonify(role='admin', message='Campaign: ' + data['campaign_name'] + ' request denied!'),
                                 status.HTTP_201_CREATED)

	