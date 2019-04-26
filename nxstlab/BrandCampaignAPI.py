from flask import jsonify, make_response
from flask_api import status
from flask_restful import Resource, reqparse
from nxstlab.BrandCampaign import BrandCampaign
from nxstlab.brand import Brand

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
    parser.add_argument('gift_campaign', type=bool)
    parser.add_argument('gift_code', type=bool)
    # parser.add_argument('website_social_media_handles', type=str)
    parser.add_argument('campaign_info_rqmts',
                        type=str,
                        required=True,
                        help='This field cannot be blank.')

    def post(self):
        data = BrandCampaignRequestAPI.parser.parse_args()
        if BrandCampaign.objects(email=data['email'],
                                 campaign_name=data['campaign_name']):
            return make_response(jsonify(role='brand', message='Campaign: ' + data['campaign_name'] + ' already exists!'),
                                 status.HTTP_409_CONFLICT)
        else:
            BrandCampaign(
                campaign_name=data['campaign_name'],
                email=data['email'],
                # website_social_media_handles=data[
                #                                 'website_social_media_handles'
                #                                 ],
                gift_campaign=data['gift_campaign'],
                gift_code=data['gift_code'],
                campaign_information_requirements=data[
                                                    'campaign_info_rqmts']
                ).save()
            if 'requested_influencers' in data:
                BrandCampaign.save(requested_influencers=data['requested_influencers'])
            return make_response(jsonify(role='brand', message='Campaign: ' + data['campaign_name'] + ' request successfully created!'),
                                 status.HTTP_201_CREATED)

    def get(self):
        brand_campaign = [brand_campaign
                          for brand_campaign in BrandCampaign.objects(isApproved=False, isDenied=False)]
        result = []
        for campaign in brand_campaign:
            associated_brand = Brand.objects(email=campaign.email).first()
            data = dict()
            data['campaign_name'] = campaign.campaign_name
            data['email'] = campaign.email
            data['campaign_info_rqmts'] = campaign.campaign_information_requirements
            data['isApproved'] = campaign.isApproved
            data['requested_influencers'] = campaign.requested_influencers
            data['image'] = campaign.image
            result.append(data)
        if not result:
            return make_response(jsonify(role='admin', message='No campaign requests left to be approved/denied'),
                                 status.HTTP_204_NO_CONTENT)
        return jsonify(result)

# api.add_resource(BrandCampaignRequestAPI, '/brandcampaignrequest')
# app.run(port=5000, debug=True)
