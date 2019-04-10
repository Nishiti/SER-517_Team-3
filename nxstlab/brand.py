from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField
from flask_login import UserMixin, login_manager


class Brand(UserMixin, Document):
    company_name = StringField(max_length=60, required=True)
    address = StringField(max_length=120, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=60, required=True)

    phone = StringField(max_length=13)
    website = StringField(max_length=120)
    instagram_handel = StringField(max_length=60)
    brand_growth_option1 = BooleanField(null=False, default=False)
    brand_growth_option2 = BooleanField(null=False, default=False)
    brand_growth_option3 = BooleanField(null=False, default=False)
    isapproved = BooleanField(null=False, default=False)
    isactive = BooleanField(null=False, default=False)

# @login_manager.user_loader
# def load_user(user_id):
#     return Brand.objects(pk=user_id).first()