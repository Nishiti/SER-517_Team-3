import csv
from pymongo import MongoClient

#CSV to JSON Conversion

csvfile = open(
            'C://Users//vihar//Desktop//VJB//Arizona State University//Spring 2019//Software Factory//nxstlab - Full Talent List.csv',
            'r')
reader = csv.DictReader(csvfile)

mongo_client = MongoClient()
db = mongo_client.influencer_db
db.coll.drop()
header = ["Influencer",
          "Instagram Story Views (avg)",
          "Followers",
          "Average Likes",
          "Average Comments",
          "IG POST",
          "IG STORY",
          "YOUTUBE (SEC)",
          "OFFER: "]

for each in reader:
    # print(each)
    row = {}
    for field in header:
        row[field] = each[field]
    db.coll.insert_one(row)
