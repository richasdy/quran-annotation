import pandas as pd
import time
from lang_trans.arabic import buckwalter

# start timer
startTime = time.time()

# read csv files and convert it to dataframe
print('Read CSV Files Start')
corpusAqDataFrame = pd.read_csv('corpusaq-full.csv', delimiter=',', index_col=None)
print('Read CSV Files Finish')

# add an arabic translation with buckwalter to the dataframe
print('Adding Arabic To Dataframe Start')
for index, row in corpusAqDataFrame.iterrows():
    corpusAqDataFrame.loc[index, "arabic"] = buckwalter.untransliterate(
        corpusAqDataFrame.loc[index, "buckwalter"])
    print('location '+corpusAqDataFrame.loc[index, 'location']+' done')
print('Adding Arabic To Dataframe Finish')

# write complete dataframe to csv
print('Write Dataframe to CSV Start')
corpusAqDataFrame.to_csv('corpusaqWithArabic.csv', index=False)
print('Write Dataframe to CSV Finish')

# stop timer print execution time
print("Execution Time : %s Seconds" % (time.time() - startTime))

# # testing arabic csv
# corpusAqWithArabicDataFrame = pd.read_csv('corpusaq_plus_arabic.csv', delimiter=',')
# print(corpusAqWithArabicDataFrame.iloc[0])
# print(buckwalter.trans(corpusAqWithArabicDataFrame.iloc[0].loc['arabic']))
