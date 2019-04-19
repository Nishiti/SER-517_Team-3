from mongoengine import Document
from mongoengine import StringField, EmailField
from flask_login import UserMixin


class Brand(UserMixin, Document):
    company_name = StringField(max_length=60, required=True)
    company_address = StringField(max_length=120, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=6, max_length=60, required=True)
    confirm_password = StringField(min_length=6, max_length=60, required=True)

