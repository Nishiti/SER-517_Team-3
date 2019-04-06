from flask import jsonify
from flask_restful import Resource, reqparse
from app.BrandCampaign import BrandCampaign

# app = Flask(__name__)
# api = Api(app)
# connect('BrandCampaign')


class BrandCampaignRequestAPI(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('campaign_name', type=str,
                        required=True,
                        help='This field cannot be blank.')
    parser.add_argument('email', type=str,
                        required=True,
                        help='This field cannot be blank.')
    parser.add_argument('website_social_media_handles', type=str)
    parser.add_argument('campaign_info_rqmts',
                        type=str,
                        required=True,
                        help='This field cannot be blank.')

    def post(self):
        data = BrandCampaignRequestAPI.parser.parse_args()
        if BrandCampaign.objects(email=data['email'],
                                 campaign_name=data['campaign_name']):
            return {"message": "A campaign with this name already exists."}
        else:
            BrandCampaign(
                campaign_name=data['campaign_name'],
                email=data['email'],
                website_social_media_handles=data[
                                                'website_social_media_handles'
                                                ],
                campaign_information_requirements=data[
                                                    'campaign_info_rqmts']
                ).save()
            return {"message": "Campaign successfully added to the database."}

    def get(self):
        brand_campaign = [brand_campaign
                          for brand_campaign in BrandCampaign.objects()]
        result = []
        for campaign in brand_campaign:
            data = dict()
            data['campaign_name'] = campaign.campaign_name
            data['email'] = campaign.email
            data['gift_campaign'] = campaign.gift_campaign
            data['gift_code'] = campaign.gift_code
            data[
                'web_social_media_handle'
                ] = campaign.website_social_media_handles
            data[
                'campaign_info_rqmts'
                ] = campaign.campaign_information_requirements
            data['isApproved'] = campaign.isApproved
            data['isDenied'] = campaign.isDenied
            result.append(data)
        return jsonify({"list": result})


# api.add_resource(BrandCampaignRequestAPI, '/brandcampaignrequest')
# app.run(port=5000, debug=True)
