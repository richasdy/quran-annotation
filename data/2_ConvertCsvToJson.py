import pandas as pd
import json

# read csv files and convert it to dataframe
print('Read CSV Files Start')
corpusAqDataFrame = pd.read_csv('corpusaqWithArabic.csv', delimiter=',', index_col=None)
print('Read CSV Files Finish')

for index, row in corpusAqDataFrame.iterrows():
    corpusDict = {
        "location":row["location"],
        "buckwalter":row["buckwalter"],
        "partOfSpeech":row["part of speech"],
        "treebank":row["treebank"],
        "arabic":row["arabic"],
        "meaning":""
    }
    print(json.dumps(corpusDict,ensure_ascii=False))