from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField
from flask_login import UserMixin, login_manager

class GiftingCampaignAPI(Resource):
	campaign_name = StringField(max_length=60, required=True)
	campaign_type_gifting = BooleanField(null=False, default=False)
	campaign_type_normal = BooleanField(null=False, default=False)
	gift_code = BooleanField(null=False, default=False)
	campaing_info = StringField(max_length=300, required=True)

	