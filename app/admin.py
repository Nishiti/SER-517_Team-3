from mongoengine import Document
from mongoengine import StringField, EmailField

class Admin(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=60, required=True)