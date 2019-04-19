from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField, IntField
from passlib.hash import pbkdf2_sha256 as sha256

class Admin(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=160, required=True)
    # confirm_password = StringField(max_length=160, required=True)
    authenticated=BooleanField(default=False)

    def is_authenticated(self):
        return self.authenticated

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
