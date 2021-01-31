import pandas as pd
import datetime
import numpy as np

df = pd.read_csv('./combinedDF.csv')
df['Date']=pd.to_datetime(df.Date)
df1 = df.drop(['Latitude', 'Longitude'], axis=1)
cleanedTemp = df1.groupby(['Date']).mean()
cleanedTemp.sort_values(by='Date', ascending=True)
cleanedTemp.index.names = ['date']

print(cleanedTemp)

dfCOVID = pd.read_csv('raw-data/us-counties.csv')
dfCleanCOVID = dfCOVID.drop(['county', 'state', 'fips', 'deaths'], axis=1)
dfFinalCOVID = dfCleanCOVID.groupby(['date']).mean()


sortedCOVID = dfFinalCOVID[315:346]
frames = [cleanedTemp, sortedCOVID]

result = pd.concat(frames, axis=1, join='inner')

result.to_csv('./lineData.csv')

print(result)

