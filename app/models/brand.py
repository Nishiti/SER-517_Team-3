from mongoengine import Document
from mongoengine import StringField, EmailField

Growth = (('A','B','C'))

class Brand(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    website = StringField(max_length=120)
    instagram_handel = StringField(max_length=60)
    need_help_with = StringField(max_length=60, required=True)
    grow_brand_via = StringField(max_length=2, required=True, choices = Growth)