from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.anotasiAlQuran
corpusAQ = db["corpusAQ"]
users = db["users"]
anotation = db["anotation"]
wordbyword = db["wordbyword"]