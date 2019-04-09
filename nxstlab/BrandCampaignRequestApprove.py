from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from BrandCampaign import BrandCampaign
from mongoengine import connect

app = Flask(__name__)
api = Api(app)
connect('BrandCampaign')

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
			return {"message":"Campaign request approved"}
		else:
			campaign.isApproved = False
			campaign.isDenied = True
			campaign.save()
			return {"message":"Campaign request denied"}

	
api.add_resource(BrandCampaignRequestApproveAPI, '/brandcampaignrequestapprove')
app.run(port=5000, debug=True)