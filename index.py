from flask import Flask, send_file
from flask_restful import Api
from flask_login import LoginManager
from mongoengine import connect
from nxstlab.InfluencerCampaign import InfluencerCampaign
from nxstlab.InfluencerUpdateProfile import InfluencerProfile
from nxstlab.InfluencerUpdateProfile import InfluencerUpdateProfile
from nxstlab.UploadProfileImage import UploadProfileImage
from nxstlab.adminSignupAPI import AdminSignupAPI
from nxstlab.UserSignInAPI import UserSignInAPI, SecretResource
from nxstlab.brandAPI import BrandAPI, BrandGetProfileDetails
from nxstlab.adminAPIs import AdminDeactivateBrandAPI
from nxstlab.adminAPIs import AdminApproveBrandSignupAPI
from nxstlab.adminAPIs import AdminRemoveBrandAPI
from nxstlab.adminAPIs import AdminRemoveInfluencerAPI
from nxstlab.influencerAPI import InfluencerSignUpAPI
from nxstlab.adminAPIs import AdminGetBrandsWithFilterAPIAll
from nxstlab.adminAPIs import AdminGetInfluencerWithFilterAPIAll
from nxstlab.adminAPIs import AdminGetBrandsWithFilterAPI
from nxstlab.adminAPIs import AdminGetInfluencersWithFilterAPI
from nxstlab.BrandCampaignAPI import BrandCampaignRequestAPI, UpdateCampaignImage
from nxstlab.BrandCampaignRequestApprove import BrandCampaignRequestApproveAPI
from nxstlab.adminAPIs import AdminDeactivateInfluencerAPI
from nxstlab.BrandCampaignAPI import BrandGetInfluencerWithFilterAPIAll
from nxstlab.adminAPIs import AdminGetBrandCampaignsWithFilterAPI
from nxstlab.AdminSignoutAPI import UserLogoutAccess, UserLogoutRefresh
from flask_jwt_extended import JWTManager
from nxstlab.models import Influencer
from nxstlab.revokedtoken import RevokedToken
from flask_cors import CORS
import os
from nxstlab.admin import Admin
from nxstlab.user import User
app = Flask(__name__)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)

configFile = open("config.txt")
config = dict()
for line in configFile:
    arr = line[:-1].split("=")
    config[arr[0]] = arr[1]
configFile.close()
connect(config['dbname'], host=config['host'])
defaultAdminEmail = "nxstadmin@gmail.com"
defaultAdminPassword = "password"

if not Admin.objects(email=defaultAdminEmail):
    Admin(email=defaultAdminEmail,password=Admin.generate_hash(defaultAdminPassword)).save()
    User(email=defaultAdminEmail,password=User.generate_hash(defaultAdminPassword),role='admin').save()

@app.route("/")
def hello():
    return send_file('templates/index.html')

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    print('In check_if_token_in_blacklist...', decrypted_token['jti'])
    jti = decrypted_token['jti']
    return RevokedToken.is_jti_blacklisted(jti)

api.add_resource(BrandAPI, '/brand')
api.add_resource(BrandGetProfileDetails, '/brand/getProfileDetails')
api.add_resource(UserSignInAPI, '/user/signin')
api.add_resource(AdminSignupAPI, '/admin/signup')
api.add_resource(AdminRemoveBrandAPI, '/admin/removebrand')
api.add_resource(AdminDeactivateBrandAPI, '/admin/deactivatebrand')
api.add_resource(AdminDeactivateInfluencerAPI, '/admin/deactivateinf')
api.add_resource(AdminApproveBrandSignupAPI, '/admin/approve/brandsingup')

# Brand Search name and all
api.add_resource(AdminGetBrandsWithFilterAPI, '/admin/getBrands')
api.add_resource(AdminGetBrandsWithFilterAPIAll, '/admin/getAllBrands')

# Influencer search - name and all
api.add_resource(AdminGetInfluencerWithFilterAPIAll, '/admin/getAllInfluencer')
api.add_resource(AdminGetInfluencersWithFilterAPI, '/admin/getInfluencers')
api.add_resource(AdminRemoveInfluencerAPI, '/admin/removeInfluencers')
api.add_resource(InfluencerSignUpAPI, '/influencer/signup')
api.add_resource(BrandCampaignRequestAPI, '/brandcampaignrequest')
api.add_resource(BrandCampaignRequestApproveAPI, '/brandcampaignrequestapprove')
api.add_resource(AdminGetBrandCampaignsWithFilterAPI, '/approvecamp')
api.add_resource(UserLogoutAccess, '/admin/signoutaccess')
api.add_resource(UserLogoutRefresh, '/admin/signoutrefresh')
api.add_resource(InfluencerUpdateProfile, '/influencer/updateprofile')
api.add_resource(UploadProfileImage, '/influencer/uploadProfileImage')
api.add_resource(InfluencerProfile, '/influencer/profile')
api.add_resource(InfluencerCampaign, '/influencer/updatecampaign')
api.add_resource(BrandGetInfluencerWithFilterAPIAll, '/brand/brandGetInfluencers')
api.add_resource(UpdateCampaignImage, '/brand/updatecampaignimage')

# Test Resource
api.add_resource(SecretResource, '/admin/secret')

if __name__ == '__main__':
    app.secret_key = os.urandom(16)
    app.debug = True
    app.run(port=5000)

