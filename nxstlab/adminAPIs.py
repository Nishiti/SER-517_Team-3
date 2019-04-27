from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import jsonify, request, make_response
from nxstlab.BrandCampaign import BrandCampaign

from nxstlab.brand import Brand

from flask_api import status
from nxstlab.models import Influencer
from nxstlab.user import User


class AdminRemoveBrandAPI(Resource):
    # post method to remove brand by admin
    @jwt_required
    def post(self):
        data = request.get_json(force=True)
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            brand.delete()
            user = User.objects(email=data['email']).first()
            user.delete()

            return make_response(jsonify(role='brand', message='brand has been removed from database'),
                                 status.HTTP_200_OK)

class AdminDeactivateBrandAPI(Resource):
    # post method to deactivate brand by admin
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email']).first()
            brand['isactive'] = False
            brand.save()

            return make_response(jsonify(role='admin', message='brand has been deactivated'), status.HTTP_200_OK)


class AdminRemoveInfluencerAPI(Resource):
    # post method to remove influencer by admin
    def post(self):
        data = request.get_json(force=True)
        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='influencer does not exist in database'),
                                 status.HTTP_404_NOT_FOUND)
        else:
            user = Influencer.objects(email=data['email']).first()
            user.delete()
            user = User.objects(email=data['email']).first()
            user.delete()
            return make_response(jsonify(role='admin', message='influencer has been removed from database'),
                                 status.HTTP_200_OK)


class AdminDeactivateInfluencerAPI(Resource):
    # post method to deactivate influencer by admin
    def post(self):
        data = request.get_json(force=True)

        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='Influencer does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            user = Influencer.objects(email=data['email']).first()
            user['isactive'] = False
            user.save()

            return make_response(jsonify(role='admin', message='Influencer has been deactivated'), status.HTTP_200_OK)


class AdminApproveBrandSignupAPI(Resource):
    #post method to approve brand signup by admin
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email']).first()
            if not brand['isapproved']:
                brand.isapproved = True
                brand.isactive = True
                brand.save()
                return make_response(jsonify(role='admin', message='brand is approved'), status.HTTP_200_OK)
            else:
                return make_response(jsonify(role='admin', message='brand is already approved'), status.HTTP_200_OK)

class AdminGetBrandsWithFilterAPI(Resource):
    # post method to get brands by company name
    def post(self):
        data = request.get_json(force=True)
        name = data['company_name']
        brands = [brand for brand in Brand.objects(company_name__contains=name)]
        res = []
        for brand in brands:
            if brand.isapproved == False:
                continue
            else:
                temp = dict()
                temp['company_name'] = brand.company_name
                temp['address'] = brand.address
                temp['email'] = brand.email
            res.append(temp)
            print(res)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)

class AdminGetBrandsWithFilterAPIAll(Resource):
    # post method to get brands by all filters
    def post(self):
        data = request.get_json(force=True)
        brands = [brand for brand in Brand.objects(__raw__ = data)]
        res = []
        for brand in brands:
            temp = dict()
            temp['company_name'] = brand.company_name
            temp['address'] = brand.address
            temp['email'] = brand.email
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)
class AdminGetInfluencerWithFilterAPIAll(Resource):
    # post method to get influencers for certain criteria
    def post(self):
        data = request.get_json(force=True)
        newdata = {}
        interestList = []
        finalList = []
        startage = endage = 0
        for key in data:
            print('key = ', key)
            if key == 'areas_of_interest':
                continue
            elif key == 'startage':
                startage = data[key]
            elif key == 'endage':
                endage = data[key]
            else:
                newdata[key] = data[key]

        if newdata:
            users = [user for user in Influencer.objects(__raw__=newdata)]
            for u in users:
                print('u = ', u.first_name)
            finalList = users
        if 'areas_of_interest' in data:
            for interest in data['areas_of_interest']:
                temp1 = Influencer.objects(areas_of_interest=interest)
                interestList += temp1
            finalList += interestList
        finalList = list(set(finalList))

        res = []
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
            temp['campaignImages'] = user.campaignImages
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands for given filter'),
                             status.HTTP_200_OK)


class AdminGetInfluencersWithFilterAPI(Resource):
    # post method to get influencers with name filter
    def post(self):
        data = request.get_json(force=True)
        name = data['name']
        influencers = [influencer for influencer in Influencer.objects(first_name__contains=name)]
        influencers.extend([influencer for influencer in Influencer.objects(last_name__contains=name)])
        res = []
        for user in influencers:
            temp = dict()
            temp['first_name'] = user.first_name
            temp['last_name'] = user.last_name
            temp['email'] = user.email
            temp['website_social_media_handles'] = user.website_social_media_handles
            temp['big_deal_on_option1'] = user.big_deal_on_option1
            temp['big_deal_on_option2'] = user.big_deal_on_option2
            temp['big_deal_on_option3'] = user.big_deal_on_option3
            temp['big_deal_on_option4'] = user.big_deal_on_option4
            temp['big_deal_on_option5'] = user.big_deal_on_option5
            temp['followers'] = user.followers
            temp['gender'] = user.gender
            temp['dob'] = user.dob
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of influencers for given filter'),
                             status.HTTP_200_OK)


class AdminGetBrandCampaignsWithFilterAPI(Resource):
    # get method to get brand campaign details with certain refresh
    def get(self):
        brandCampaigns = [brand for brand in BrandCampaign.objects()]
        print('brand campaigns = ', brandCampaigns)
        res = []
        for brandCampaign in brandCampaigns:
            if brandCampaign.isApproved == False:
                continue
            else:
                temp = dict()
                temp['campaign_name'] = brandCampaign.campaign_name
                temp['email'] = brandCampaign.email
                temp['gift_campaign'] = brandCampaign.gift_campaign
                temp['gift_code'] = brandCampaign.gift_code
                temp['campaign_information_requirements'] = brandCampaign.campaign_information_requirements
                temp['requested_influencers'] = brandCampaign.requested_influencers
                temp['image'] = brandCampaign.image
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of campaign for given filter'),
                             status.HTTP_200_OK)
