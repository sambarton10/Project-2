import requests
import pandas as pd
from config import weather_api_key
import json as js

#Create An Empty List To Add Temperature Data To
responses = []

#Read Zipcode Data Into Pandas Dataframe
zipData = pd.read_csv("raw-data/county_centers.csv")
#Read Dates Data Into Pandas Dataframe

dateData = pd.read_csv("raw-data/dates.csv")

#Convert Date Column To A List With Dates

dates = dateData['date'].tolist()


LONclon10 = zipData['pclon10'].tolist()
LATclat10 = zipData['pclat10'].tolist()


dataframe = pd.DataFrame()
dataframe['Lon'] = LONclon10
dataframe['Lat'] = LATclat10

dataframe['combined']=dataframe['Lat'].astype(str)+','+dataframe['Lon'].astype(str)

#print(dataframe)

df = dataframe.apply (pd.to_numeric, errors='coerce')
df = dataframe.dropna()

#print(df)

#print(dataframe)

coords=df['combined'].tolist()
#print(coords)
#print(coords)
testCoords = ['32.536090909,-86.64484848']

testDates = ['2020-07-19', '2021-01-20']


for date in dates[0:5]:

    baseURL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
    format = '&format=json'
    queryURL = baseURL + weather_api_key + format + "&date=" + date

    #print(queryURL)
    
    test = requests.get(queryURL)
    print("next date!!")
  
    for coord in coords:
        rr = requests.get(queryURL + "&q=" + coord)
        my_dict = rr.json()
        y = js.dumps(my_dict)
        jsonDict = js.loads(y)
        x = (jsonDict['data']['weather'][0]['avgtempF'])
        paths = [coord, date, x]
        responses.append(paths)
        print(paths)
        print("next coord!")

print(responses)

responsesDF = pd.DataFrame(responses)
responsesDF.to_csv('./dataframe.csv', index=False, header=True)
print(responsesDF)
#print(responses)
