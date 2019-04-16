from mongoengine import Document
from mongoengine import StringField, IntField

from nxstlab.admin import Admin


class RevokedToken(Document):
    id = IntField(primary_key=True)
    jti = StringField(max_length=120)

    '''def add(self):
        print('add')'''

    @classmethod
    def is_jti_blacklisted(jti):
        query = Admin.objects(jti=jti).first()
        print('query = ', query)
        return True if query else False
