from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField

class Brand(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=60, required=True)
    website = StringField(max_length=120)
    instagram_handel = StringField(max_length=60)
    need_help_with = StringField(max_length=50000)
    brand_growth_option1 = BooleanField(null=False, default=False)
    brand_growth_option2 = BooleanField(null=False, default=False)
    brand_growth_option3 = BooleanField(null=False, default=False)
    isapproved = BooleanField(null=False, default=False)