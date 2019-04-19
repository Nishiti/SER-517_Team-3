from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField
from passlib.hash import pbkdf2_sha256 as sha256

class User(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=160, required=True)
    role = StringField(max_length=30)
    authenticated=BooleanField(default=False)

    def is_authenticated(self):
        return self.authenticated

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
