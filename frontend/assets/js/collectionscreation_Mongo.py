#var MongoClient = require('mongodb').MongoClient;
#var url = "mongodb://localhost:27017/";

#MongoClient.connect(url, function(err, db) {
 # if (err) throw err;
 # var dbo = db.db("nxstlab");
 # dbo.createCollection("influencers", function(err, res) {
  #  if (err) throw err;
  #  console.log("Collection created!");
  #  db.close();
  #});
#

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["nxstlab"]

mycol = mydb["influencers"]

#collist = myclient.collection_names()
print(mycol.list_collections_names())
if "influencers" in collist:
  print("The collection exists.")