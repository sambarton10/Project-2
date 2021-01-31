import pandas as pd
import os
import datetime
import numpy as np

df = pd.read_csv('/Users/sambarton/Project-2/draftJoin.csv')
lon = df['longitude'].drop_duplicates()
lat = df['latitude'].drop_duplicates()


dataframe = pd.DataFrame()
dataframe['Lon'] = lon
dataframe['Lat'] = lat

dataframe['combined']=dataframe['Lat'].astype(str)+','+dataframe['Lon'].astype(str)

#print(dataframe)

df = dataframe.apply (pd.to_numeric, errors='coerce')
df = dataframe.dropna()

#print(df)

#print(dataframe)

coords=df['combined'].tolist()

print(coords)


#longitude,latitude