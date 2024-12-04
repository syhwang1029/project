import pymongo
from pymongo import MongoClient
# momgobd 공식 듀토리얼 참고
# https://www.mongodb.com/ko-kr/docs/languages/python/pymongo-driver/v4.8/connect/

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
