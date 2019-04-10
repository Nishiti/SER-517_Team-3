from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField

class Admin(Document):
    first_name = StringField(max_length=60, required=True)
    last_name = StringField(max_length=60, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=160, required=True)
    authenticated=BooleanField(default=False)

    def is_authenticated(self):
        return self.authenticated

