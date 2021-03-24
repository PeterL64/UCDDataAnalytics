from urllib.request import urlretrieve
import pandas as pd

# Test3
import kaggle
kaggle.api.aunthenticate()
kaggle.api.dataset_download_files('https://www.kaggle.com/harryarthur/ireland-rugby-match-data-internationals?select=IREMatchData%28FULL%29.csv', \
                                  path=r'/UCDDataAnalyticsProject/IrishRugbyData', \
                                  unzip=True)





# Test1
#url = 'https://www.kaggle.com/harryarthur/ireland-rugby-match-data-internationals?select=IREMatchData%28FULL%29.csv'
#Test = urlretrieve(url, 'RugbyDataTest.csv')
#Test1 = pd.read_csv(Test)
#print(Test1)



# Test2
#import requests
#url1 = 'https://www.kaggle.com/harryarthur/ireland-rugby-match-data-internationals?select=IREMatchData%28FULL%29.csv'
#r = requests.get(url1)
#text = r.text
#print(text)