from mongoengine import Document, BooleanField, IntField
from mongoengine import StringField, EmailField

CATEGORY = (('Atheletes','Musicians','Lifestyle','Comedy','Tech','Deals','Travelers'))
GENDER = (('M','F','NA'))
class Influencer(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    category = StringField(max_length=60, required=True, choices = CATEGORY)
    youtube = BooleanField()
    IGStoryViews = IntField()
    followers = IntField()
    AvgLikes = IntField()
    AvgComments = IntField()
    Gender = StringField(max_length=2, required=True, choices = GENDER)
    email = EmailField(required=True, unique=True)
    # big_deal_on =
    website = StringField(max_length=120)
    social_media_handles=StringField(max_length=60)
