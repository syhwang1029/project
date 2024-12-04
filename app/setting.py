import pymongo
from pymongo import MongoClient

try:
    uri = "mongodb+srv://test:SkGZDvJMAOSW1ez7@cluster.2fuhu.mongodb.net/"
    client = MongoClient(uri)

    database = client["test"]
    collection = database["testcollection"]

    # start example code here

    # end example code here

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
