from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField, ListField


class BrandCampaign(Document):
    campaign_name = StringField(max_length=50, required=True)
    email = EmailField(required=True)
    gift_campaign = BooleanField(null=False, default=False)
    gift_code = BooleanField(null=False, default=False)
    # website_social_media_handles = StringField(max_length=150)
    campaign_information_requirements = StringField(max_length=500,
                                                    required=True)
    isApproved = BooleanField(null=False, default=False)
    isDenied = BooleanField(null=False, default=False)
    requested_influencers = ListField(StringField())
    image = StringField(required=False, default='/static/uploads/campaign_profile/default.jpg')
