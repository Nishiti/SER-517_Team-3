from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from flask_login import LoginManager
from mongoengine import connect
from brand import Brand
from models import Influencer
from adminSignupAPI import AdminSignupAPI
from brandAPI import BrandAPI
#from adminSignInAPI import AdminSignInAPI

app = Flask(__name__)
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

connect('ser517', host='mongodb://localhost/ser517')


influencers = [
  { 'name': 'john', 'email': 'john@example.com' }
]


@app.route('/influencers')
def get_influencers():
    influencers = Influencer.objects()
    if influencers is None:
        data = {
        "role": "influencer",
        "message": "No influencer data found in database!"
        }
        response = app.response_class(
        response=json.dumps(data),
        status=401,
        mimetype='application/json'
        )
    else:
        '''data = {
            "role": "influencer",
            "message": "Influencer data is found in database!"
        }'''
        response = app.response_class(
        response=json.dumps(influencers),
        status=200,
        mimetype='application/json'
        )
    return response

@app.route('/influencers/signup', methods=['POST'])
def signupInfluencers():
  data = (request.get_json())
  if Influencer.objects(email=data['email']):
    data = {
      "role": "influencer",
      "message": "influencer already exists in database"
    }
    response = app.response_class(
      response=json.dumps(data),
      status=409,
      mimetype='application/json'
    )

  else:
    influencer = Brand(
        first_name=data['first_name'],
        last_name=data['last_name'],
        category=data['category'],
        youtube=data['youtube'],
        IGStoryViews=data['IGStoryViews'],
        followers=data['followers'],
        AvgLikes=data['AvgLikes'],
        AvgComments=data['AvgComments'],
        Gender=data['Gender'],
        email=data['email'],
        website=data['website'],
        social_media_handles=data['instagram_handle'],
    ).save()

    data = {
      "role": "influencer",
      "message": "new influencer is added in database"
    }
    response = app.response_class(
      response=json.dumps(data),
      status=201,
      mimetype='application/json'
    )

  return response


# @app.route('/brand/signup', methods=['POST'])
# def signupbrands():
#   data = (request.get_json())
#   if Brand.objects(email=data['email']):
#     data = {
#       "role": "brand",
#       "message": "brand already exists in database"
#     }
#     response = app.response_class(
#       response=json.dumps(data),
#       status=409,
#       mimetype='application/json'
#     )
#
#   else:
#     user = Brand(
#       first_name=data['first_name'],
#       last_name = data['last_name'],
#       email = data['email'],
#       password = data['password'],
#       website = data['website']
#     ).save()
#
#     data = {
#       "role": "brand",
#       "message": "new brand is added in database"
#     }
#     response = app.response_class(
#       response=json.dumps(data),
#       status=201,
#       mimetype='application/json'
#     )
#
#   return response

# @app.route('/brand/update', methods=['POST'])
# def updatebrands():
#   data = (request.get_json())
#   # handle case when email is not found
#   brand = Brand.objects(email=data['email'])
#   if not brand:
#     data = {
#       "role": "brand",
#       "message": "brand does not exists in database"
#     }
#     response = app.response_class(
#       response=json.dumps(data),
#       status=404,
#       mimetype='application/json'
#     )
#   else:
#     brand = brand[0]
#     data = request.get_json()
#     for key in data:
#       brand[key] = data[key]
#     brand.save()
#
#     data = {
#       "role": "brand",
#       "message": "brand updated in database"
#     }
#     response = app.response_class(
#       response=json.dumps(data),
#       status=200,
#       mimetype='application/json'
#     )
#
#   return response

@app.route('/brand/signin', methods=['POST'])
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
  return response

@app.route('/admin/approve/brandsingup', methods=['POST'])
def admin_approve_brand_singup():
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
    brand = Brand.objects(email=data['email'])
    brand = brand[0]
    if brand['isapproved'] == False:
      brand.isapproved = True
      brand.save()
      data = {
        "role": "admin",
        "message": "brand is approved and updated in database"
      }
      response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
      )
    else:
      data = {
        "role": "admin",
        "message": "brand is already approved in database"
      }
      response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
      )
  return response



api.add_resource(BrandAPI, '/brand')
api.add_resource(AdminSignupAPI, '/admin/signup')
#api.add_resource(AdminSignInAPI, '/admin/signin')

# @app.route('/', methods=['GET'])
# def home():
#   render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)