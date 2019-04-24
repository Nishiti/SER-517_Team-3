from flask import Flask, send_file, request, make_response, jsonify
from flask_restful import Api
from mongoengine import connect
from flask_cors import CORS
from flask_api import status
import os
from werkzeug.utils import secure_filename

from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField, ListField, FileField

class Influencer(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=6, required=True)
    confirm_password = StringField(min_length=6, required=True)
    big_deal_on_option1 = BooleanField(null=False, default=False)

    big_deal_on_option2 = BooleanField(null=False, default=False)
    big_deal_on_option3 = BooleanField(null=False, default=False)
    big_deal_on_option4 = BooleanField(null=False, default=False)
    big_deal_on_option5 = BooleanField(null=False, default=False)
    website_social_media_handles = StringField(max_length=120)
    followers = StringField(max_length=60)
    areas_of_interest = ListField(StringField())
    image = FileField()

connect("ser517", host="mongodb://localhost/ser517")
app = Flask(__name__)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return send_file('index.html')

@app.route('/file/upload', methods = ['POST'])
def hello3():

    influencer = Influencer.objects(email="inf1@gmail.com").first()

    data = request.get_json()

    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                fileLocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(fileLocation)
                influencer.image = fileLocation
                influencer.save()

    return make_response(jsonify(role='influencer', message='Influencer added to the database'),
                                 status.HTTP_200_OK)


@app.route('/file/get', methods = ['GET'])
def hello2():
    data = request.data
    user = Influencer.objects(email="inf1@gmail.com").first()
    temp = dict()

    temp['image'] = user.image

    return make_response(jsonify(data=temp, role='influencer', message='Influencer added to the database'),
                                 status.HTTP_200_OK)


if __name__ == '__main__':
    app.secret_key = os.urandom(16)
    app.debug = True
    app.run(port=5000)
