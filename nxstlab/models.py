from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField, ListField

CATEGORY = (('Atheletes','Musicians','Lifestyle',''))
GENDER = (('M','F','NA'))
class Influencer(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=8, required=True)
    confirm_password = StringField(min_length=8, required=True)
    big_deal_on_option1 = BooleanField(null=False, default=False)
    big_deal_on_option2 = BooleanField(null=False, default=False)
    big_deal_on_option3 = BooleanField(null=False, default=False)
    big_deal_on_option4 = BooleanField(null=False, default=False)
    big_deal_on_option5 = BooleanField(null=False, default=False)
    website_social_media_handles = StringField(max_length=120)
    followers = StringField(max_length=60)
    areas_of_interest = ListField(StringField())
