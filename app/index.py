from flask import Flask, jsonify, request, json
from mongoengine import connect
from brand import Brand

app = Flask(__name__)

connect('ser517', host='mongodb://localhost/ser517')


influencers = [
  { 'name': 'john', 'email': 'john@example.com' }
]


@app.route('/influencers')
def get_influencers():
  return jsonify(influencers)

@app.route('/influencers', methods=['POST'])
def signup():
  influencers.append(request.get_json())
  #write to database table  - influeners
  return '', 204

@app.route('/brands/signup', methods=['POST'])
def signupbrands():
  data = (request.get_json())
  if Brand.objects(email=data['email']):
    data = {
      "role": "brand",
      "message": "brand already exists in database"
    }
    response = app.response_class(
      response=json.dumps(data),
      status=409,
      mimetype='application/json'
    )

  else:
    user = Brand(
      first_name=data['first_name'],
      last_name = data['last_name'],
      email = data['email'],
      password = data['password'],
      website = data['website'],
      instagram_handel = data['instagram_handel'],
      need_help_with = data['need_help_with'],
      brand_growth_option1 = data['brand_growth_option1'],
      brand_growth_option2=data['brand_growth_option2'],
      brand_growth_option3=data['brand_growth_option3']
    ).save()

    data = {
      "role": "brand",
      "message": "new brand is added in database"
    }
    response = app.response_class(
      response=json.dumps(data),
      status=201,
      mimetype='application/json'
    )

  return response

@app.route('/brands/signin', methods=['POST'])
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


# @app.route('/', methods=['GET'])
# def home():
#   render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)