from flask import Flask, jsonify, request

app = Flask(__name__)

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
def signup():
  influencers.append(request.get_json())
  #write to database table  - influeners
  return '', 204
  
