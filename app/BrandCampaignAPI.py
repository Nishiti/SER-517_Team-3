from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from BrandCampaign import BrandCampaign
from mongoengine import connect

app = Flask(__name__)
api = Api(app)
connect('BrandCampaign')

class BrandCampaignRequestAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('campaign_name', type=str, required=True, help='This field cannot be blank.')
	parser.add_argument('email', type=str, required=True, help='This field cannot be blank.')
	parser.add_argument('website_social_media_handles', type=str)
	parser.add_argument('campaign_information_requirements', type=str, required=True, help='This field cannot be blank.')

	def post(self):
		data = BrandCampaignRequest.parser.parse_args()
		if BrandCampaign.objects(email=data['email'], campaign_name=data['campaign_name']):
			return {"message":"A campaign with this name already exists."}
		else:
			BrandCampaign(
				campaign_name = data['campaign_name'],
				email = data['email'],
				website_social_media_handles = data['website_social_media_handles'],
				campaign_information_requirements = data['campaign_information_requirements']
				).save()
			return {"message":"Campaign successfully added to the database."}


api.add_resource(BrandCampaignRequest, '/brandcampaignrequest')
app.run(port=5000, debug=True)