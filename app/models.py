from mongoengine import Document
from mongoengine import StringField, EmailField


class Influencer(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    # big_deal_on =
    website = StringField(max_length=120)
    social_media_handles=StringField(max_length=60)
