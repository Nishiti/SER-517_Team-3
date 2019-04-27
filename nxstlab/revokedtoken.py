from mongoengine import Document
from mongoengine import StringField, IntField

from nxstlab.admin import Admin


class RevokedToken(Document):
    id = IntField(primary_key=True)
    jti = StringField(max_length=120)


    @classmethod
    def is_jti_blacklisted(self, jti):
        print('###################is_jti_blacklisted...', jti)
        print('###RT objects = ', RevokedToken.objects())
        query = RevokedToken.objects(jti=jti).first()
        print('query = ', query)
        return True if query else False
