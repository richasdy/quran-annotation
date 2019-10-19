import pandas as pd
import json
from db import *


def checkPostedData(postedData, functionName):
    if(functionName == "FindSurah"):
        if("surahNumber" not in postedData):
            return 301
        else:
            return 200


def storeCorpusToDB():
    # read csv files and convert it to dataframe (corpusaq)
    print('Read CSV Files Start')
    corpusAqDataFrame = pd.read_csv(
        'corpusaqWithArabic.csv', delimiter=',', index_col=None)
    print('Read CSV Files Finish')

    # drop existing data
    corpusAQ.drop()

    for index, row in corpusAqDataFrame.iterrows():
        corpusAQ.insert({
            "_id": str(row["location"]),
            "buckwalter": row["buckwalter"],
            "partOfSpeech": row["part of speech"],
            "treebank": row["treebank"],
            "arabic": row["arabic"],
            "meaning": ""
        })
        print("corpus = "+str(row["location"])+" Stored")

    # read csv files and convert it to dataframe (wordbyword)
    print('Read CSV Files Start')
    wordbywordDataFrame = pd.read_csv(
        'wordbywordtranslation.csv', delimiter=',', index_col=None)
    print('Read CSV Files Finish')

    # drop existing data
    wordbyword.drop()

    for index, row in wordbywordDataFrame.iterrows():
        _id = ""
        _id = str(row["suratnumber"])+":"+str(row["ayatnumber"])+":"+str(row["wordnumber"])
        wordbyword.insert({
            "_id": _id,
            "suratnumber": row["suratnumber"],
            "ayatnumber": row["ayatnumber"],
            "wordnumber": row["wordnumber"],
            "translation": row["translation"]
        })
        print("wordbyword = "+_id+" Stored")
