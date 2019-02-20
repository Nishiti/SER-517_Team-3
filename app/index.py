from flask import Flask, jsonify, request, render_template
from mongoengine import connect

app = Flask(__name__)

#connect('ser517', host='mongodb://localhost/ser517')


influencers = [
  { 'name': 'john', 'email': 'john@example.com' }
]

brands = [{'name' : 'Brand1', 'email' : 'brand1@email.com'}, 
		  {'name' : 'Brand2', 'email' : 'brand2@email.com'}, 
]

@app.route('/influencers')
def get_influencers():
  return jsonify(influencers)

@app.route('/influencers', methods=['POST'])
def signup():
  influencers.append(request.get_json())
  #write to database table  - influeners
  return '', 204
  
@app.route('/brands')
def get_brands():
  return jsonify(brands)

@app.route('/brands', methods=['POST'])
def signupbrands():
  influencers.append(request.get_json())
  #write to database table  - influeners
  return '', 204

@app.route('/', methods=['GET'])
def home():
  render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)