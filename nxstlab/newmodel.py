from mongoengine import Document
from mongoengine import StringField

class NewModel(Document):
    areas_of_interest = StringField()
    image = StringField(required=False, default='/static/uploads/influencer_profile/default.png')