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
    # read csv files and convert it to dataframe
    print('Read CSV Files Start')
    corpusAqDataFrame = pd.read_csv(
        'corpusaqWithArabic.csv', delimiter=',', index_col=None)
    print('Read CSV Files Finish')

    for index, row in corpusAqDataFrame.iterrows():
        corpusAQ.insert({
            "_id": str(row["location"]),
            "buckwalter": row["buckwalter"],
            "partOfSpeech": row["part of speech"],
            "treebank": row["treebank"],
            "arabic": row["arabic"],
            "meaning": ""
        })
        print(str(row["location"])+" Stored")
