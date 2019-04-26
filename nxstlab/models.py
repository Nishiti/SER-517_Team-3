from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField, ListField, FileField, IntField

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
    gender = StringField(required=True)
    dob = StringField()
    image = StringField(required=False, default='/static/uploads/influencer_profile/default.png')
    campaignImages = ListField(StringField())