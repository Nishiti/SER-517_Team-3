from flask import Flask, jsonify, request

app = Flask(__name__)

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