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

#Convert Zipcode Column To A List With Zipcodes
zipcodes = zipData["fips"].tolist()
#print(zipcodes)
#Stringify the Zipcodes Which Are Integers
stringifiedZips = map(str, zipcodes)
print(list(stringifiedZips))

#print(zipcodes) '92208', '60154'

#test zipcode dataset to test loop
testZips = ['92203', '60154']

testDates = ['2020-07-19', '2021-01-20']

'''
for date in dates:

    baseURL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
    format = '&format=json'
    queryURL = baseURL + weather_api_key + format + "&date=" + date

    #print(queryURL)
    
    test = requests.get(queryURL)
    #print(test)
    
    for zip in stringifiedZips:
        rr = requests.get(queryURL + "&q=" + zip)
        my_dict = rr.json()
        y = js.dumps(my_dict)
        jsonDict = js.loads(y)
        responses.append(jsonDict['data']['weather'][0]['avgtempF'])
        
        
print(responses)
'''
baseURL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
format = '&format=json'
date = '2020-07-11'    
queryURL = baseURL + weather_api_key + format + "&date=" + date
for zip in stringifiedZips:
        rr = requests.get(queryURL + "&q=" + zip)
        my_dict = rr.json()
        y = js.dumps(my_dict)
        jsonDict = js.loads(y)
        responses.append(jsonDict['data'])

print(responses)