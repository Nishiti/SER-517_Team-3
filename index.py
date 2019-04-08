from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from flask_login import LoginManager
from mongoengine import connect
from nxstlab.adminSignupAPI import AdminSignupAPI
from nxstlab.adminSignInAPI import AdminSignInAPI
from nxstlab.brandAPI import BrandAPI
from nxstlab.adminAPIs import AdminDeactivateBrandAPI
from nxstlab.adminAPIs import AdminApproveBrandSignupAPI
from nxstlab.adminAPIs import AdminRemoveBrandAPI
#from brandAPI import BrandSignInAPI
from nxstlab.influencerAPI import InfluencerSignUpAPI
from nxstlab.adminAPIs import AdminGetBrandsWithFilterAPI
from nxstlab.adminAPIs import AdminGetInfluencersWithFilterAPI
from nxstlab.BrandCampaignAPI import BrandCampaignRequestAPI
from nxstlab.AdminSignoutAPI import AdminSignoutAPI
from flask_cors import CORS
import os

app = Flask(__name__)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)

connect('ser517', host='mongodb://localhost/ser517')



'''@app.route('/brand/signin', methods=['POST'])
def signinbrands():
  data = (request.get_json())
  if not Brand.objects(email=data['email']):
    data = {
      "role": "brand",
      "message": "brand is not found in database"
    }
    response = app.response_class(
      response=json.dumps(data),
      status=404,
      mimetype='application/json'
    )

  else:
    if not Brand.objects(email=data['email'],password=data['password']):
      data = {
        "role": "brand",
        "message": "brand is found in database but password is not matching"
      }
      response = app.response_class(
        response=json.dumps(data),
        status=401,
        mimetype='application/json'
      )
    else:
      data = {
        "role": "brand",
        "message": "brand is found in database"
      }
      response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
      )
  return response'''




api.add_resource(BrandAPI, '/brand')
api.add_resource(AdminSignInAPI, '/admin/signin')
api.add_resource(AdminSignupAPI, '/admin/signup')
api.add_resource(AdminRemoveBrandAPI, '/admin/removebrand')
api.add_resource(AdminDeactivateBrandAPI, '/admin/deactivatebrand')
api.add_resource(AdminApproveBrandSignupAPI, '/admin/approve/brandsingup')
api.add_resource(AdminGetBrandsWithFilterAPI, '/admin/getBrands')
api.add_resource(AdminGetInfluencersWithFilterAPI, '/admin/getInfluencers')
api.add_resource(InfluencerSignUpAPI, '/influencer/signup')
api.add_resource(BrandCampaignRequestAPI, '/brandcampaignrequest')
#api.add_resource(AdminSignoutAPI, '/admin/signout')

if __name__ == '__main__':
    app.secret_key = os.urandom(16)
    app.run(port=5000)

