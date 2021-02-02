# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:12:14 2021

@author: Mason
"""

from sqlalchemy import create_engine, Numeric, Text
import pandas
from config import password

engine = create_engine("postgresql://postgres:" + password + "@localhost/weatherCOVID")

combinedDF = pandas.read_csv("../AdjustedFinal.csv", header = 0)

print(combinedDF)

combinedDF.to_sql("covid_weather", con = engine, if_exists = "replace", dtype = {"latitude": Numeric, "longitude": Numeric, "new_fips": Text})
engine.execute("SELECT * FROM covid_weather").fetchall()
print("covid_weather table updated!")

"""
longlatDF = pandas.read_csv("./../raw-data/county_centers.csv", header = 0)
stateDF = pandas.read_csv("./../raw-data/us-states.csv", header = 0)
countyDF = pandas.read_csv("../raw-data/us-counties.csv", header = 0)
weatherDF = pandas.read_csv("../weatherData1.csv", header = 0)

adjustedLonglat = longlatDF.drop(['clon00', 'clat00', 'pclon00', 'pclat00', 'pclon10', 'pclat10'], axis = 1)

print(adjustedLonglat)
print(stateDF)
print(countyDF)
print(weatherDF)

adjustedLonglat.to_sql("lat_long", con = engine, if_exists = "replace", dtype = {"clon10": Numeric, "clat10": Numeric})
engine.execute("SELECT * FROM lat_long").fetchall()
print("lat_long table updated!")


stateDF.to_sql("state", con = engine, if_exists = "replace")
engine.execute("SELECT * FROM state").fetchall()
print("state table updated!")

countyDF.to_sql("county", con = engine, if_exists = "replace")
engine.execute("SELECT * FROM county").fetchall()
print("county table updated!")

weatherDF.to_sql("weather", con = engine, if_exists = "replace", dtype = {"latitude": Numeric, "longitude": Numeric})
engine.execute("SELECT * FROM weather").fetchall()
print("weather table updated!")
"""