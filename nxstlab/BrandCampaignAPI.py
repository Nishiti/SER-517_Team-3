import os

from flask import jsonify, make_response
from flask_api import status
from flask_restful import Resource, reqparse
from flask import jsonify, request, make_response
from werkzeug.utils import secure_filename

from nxstlab.BrandCampaign import BrandCampaign
from nxstlab.models import Influencer
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


class BrandGetInfluencerWithFilterAPIAll(Resource):
    def post(self):
        data = request.get_json(force=True)
        #users = [user for user in Influencer.objects(__raw__=data)]
        #users = Influencer.objects(Q(__raw__=data) | Q(areas_of_interest__contains='fashion'))
        print('data = ', data)
        newdata = {}
        interestList = []
        finalList = []
        for key in data:
            print('key = ', key)
            if key == 'areas_of_interest':
                continue
            else:
                newdata[key] = data[key]
        print('newdata = ', newdata)
        if newdata:
            users = [user for user in Influencer.objects(__raw__=newdata)]
            for u in users:
                print('u = ', u.first_name)
            finalList += users
        if 'areas_of_interest' in data:
            for interest in data['areas_of_interest']:
                # temp1 = Influencer.objects(Q(areas_of_interest__contains=interest)).select_related()
                temp1 = Influencer.objects(areas_of_interest=interest)
                interestList += temp1
            print('interestlist = ', interestList)
            finalList += interestList

        '''for f in interestList:
            print('f = ', f.first_name)
        for final in finalList:
            print('final = ', final.first_name)'''
        res = []
        #for user in users:
        for user in finalList:
            temp = dict()
            temp['first_name'] = user.first_name
            temp['last_name'] = user.last_name
            temp['email'] = user.email
            temp['big_deal_on_option1'] = user.big_deal_on_option1
            temp['big_deal_on_option2'] = user.big_deal_on_option2
            temp['big_deal_on_option3'] = user.big_deal_on_option3
            temp['big_deal_on_option4'] = user.big_deal_on_option4
            temp['big_deal_on_option5'] = user.big_deal_on_option5
            temp['website_social_media_handles'] = user.website_social_media_handles
            temp['followers'] = user.followers
            temp['dob'] = user.dob
            temp['gender'] = user.gender
            temp['image'] = user.image
            temp['campaignImage'] = user.image

            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)

class UpdateCampaignImage(Resource):
    def post(self):
        print('Campaign Profile Update!')
        data = dict()
        for key in request.form:
            data[key] = request.form[key]
        if not BrandCampaign.objects(email=data['email'], campaign_name=data['campaign_name']):
            return make_response(jsonify(role='brand', message='Brand Campaign does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            file1 = None
            brandCampaign = BrandCampaign.objects(email=data['email'], campaign_name=data['campaign_name']).first()
            if 'file1' in request.files:
                file1 = request.files['file1']
            if file1:
                filename = secure_filename(file1.filename)
                fileLocation = os.path.join('static/uploads/campaign_profile/', filename)
                file1.save(fileLocation)
                brandCampaign.image = '/' + fileLocation
                brandCampaign.save()

            return make_response(
                jsonify(role='brand', message='Brand Campaign Image updated successfully in database'),
                status.HTTP_200_OK)
