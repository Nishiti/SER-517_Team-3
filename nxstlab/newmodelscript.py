from newmodel import NewModel
from mongoengine import connect

connect("new_db")

data = [{"title":"Sports", "image":"/static/uploads/influencer_profile/default.png" },
		{"title":"Fashion", "image":"/static/uploads/influencer_profile/default.png" },
		{"title":"Beauty", "image":"/static/uploads/influencer_profile/default.png" },
		{"title":"Travel", "image":"/static/uploads/influencer_profile/default.png" },
		{"title":"Food", "image":"/static/uploads/influencer_profile/default.png" }]

for x in data:
	NewModel(areas_of_interest = x["title"], image = x["image"]).save()