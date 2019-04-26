import csv
from pymongo import MongoClient

email = []
follow_count = 0
mongo_client = MongoClient()
db = mongo_client.ser517

#Open the csv file to read the records of the csv
csvfile = open(
            'C://Users//vihar//Desktop//Influencer Database - Sheet1.csv',
            'r')

#The reader variable stores the list of all the rows of the csv sheet
reader = csv.DictReader(csvfile)

#The header variables contains the titles of all the columns in the csv
header = ["First Name", "Last Name", "Email:", "Password",
          "website", "instagram", "followers", "youtube",
          "subscribers", "Facebook", "Likes",
          "twitter","followers(twitter)","Areas of interest"]

#The for loop traverses through all the rows of the csv sheet
for each in reader:

    row = {}
    website_social_media_handles = ""
    follow = []
    follow_count = 0

    # The records that have an email that already exists in the database
    # or if the email field is bank, then they are being stored
    # in another collection as it requires Sponsors attention
    if each["Email:"] == "" or each["Email:"] in email:
      row["first_name"] = each["First Name"]
      row["last_name"] = each["Last Name"]
      row["email"] = each["Email:"]
      db.email_error.insert_one(row)
      continue

    # Add data to the collection as per the match between
    # column header of the csv and
    # fields in the project database collection
    for field in header:
      if field == "Email:":
        row["email"] = each[field]
        email.append(each[field])
      if field == "First Name":
        row["first_name"] = each[field]
      if field == "Last Name":
        row["last_name"] = each[field]
      if field == "Password":
        row["password"] = each["First Name"] + each["Last Name"]
        row["confirm_password"] = row["password"]
      if field == "website":
        if each[field] != "":
          row["big_deal_on_option1"] = True
          website_social_media_handles = website_social_media_handles + each[field]
        else:
          row["big_deal_on_option1"] = False
      if field == "instagram":
        if each[field] != "":
          if website_social_media_handles == "":
            website_social_media_handles = website_social_media_handles + each[field]
          else:
            website_social_media_handles = website_social_media_handles + ", " + each[field]
          row["big_deal_on_option2"] = True
        else:
          row["big_deal_on_option2"] = False
      if field == "youtube":
        if each[field] != "" and each[field] != "n/a" and each[field] != "N/A":
          if website_social_media_handles == "":
            website_social_media_handles = website_social_media_handles + each[field]
          else:
            website_social_media_handles = website_social_media_handles + ", " + each[field]
          row["big_deal_on_option3"] = True
        else:
          row["big_deal_on_option3"] = False
      if field == "Facebook":
        if each[field] != "":
          if website_social_media_handles == "":
            website_social_media_handles = website_social_media_handles + each[field]
          else:
            website_social_media_handles = website_social_media_handles + ", " + each[field]
          row["big_deal_on_option4"] = True
        else:
          row["big_deal_on_option4"] = False
      if field == "twitter":
        if each[field] != "":
          if website_social_media_handles == "":
            website_social_media_handles = website_social_media_handles + each[field]
          else:
            website_social_media_handles = website_social_media_handles + ", " + each[field]
          row["big_deal_on_option5"] = True
        else:
          row["big_deal_on_option5"] = False
      row["website_social_media_handles"] = website_social_media_handles
      if field == "Areas of interest":
        row["areas_of_interest"] = [x.strip() for x in each[field].split(',') if x!= ""]
      if field == "followers" and each[field] != "":
        follow_count = int(each[field].replace(",",""))
      if field == "subscribers" and each[field] != "":
        if follow_count == 0:
          follow_count = int(each[field].replace(",",""))
      if field == "Likes" and each[field] != "":
        if follow_count == 0:
          follow_count = int(each[field].replace(",",""))
      if field == "followers(twitter)" and each[field] != "":
        if follow_count == 0:
          follow_count = int(each[field].replace(",",""))
      if follow_count <= 2000:
        row["followers"] = "low"
      elif follow_count >= 2001 and follow_count <= 50000:
        row["followers"] = "moderate"
      else:
        row["followers"] = "high"

      # The gender field is being hardcoded as it is not available in current sponsors data
      # and the gender field is a required field for the database
      row["gender"] = "Male"

      # The path of a default image is being hardcoded as the available data from Sponsor
      # has no images for the influencers but a influencer can upload a image 
      # through the project website
      row["image"] = "/static/uploads/influencer_profile/default.png"
    
    # Add the row to the project database collection if the row has valid data
    if bool(row):    
      db.influencer.insert_one(row)
