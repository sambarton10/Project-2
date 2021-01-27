# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:12:14 2021

@author: Mason
"""

from sqlalchemy import create_engine, Integer, BigInteger, Float, Text, Date
import pandas
from config import password

engine = create_engine("postgresql://postgres:" + password + "@localhost/weatherCOVID")

longlatDF = pandas.read_csv("data/county_centers.csv", header = 0)
stateDF = pandas.read_csv("data/us-states.csv", header = 0)
countyDF = pandas.read_csv("data/us-counties.csv", header = 0)

adjustedLonglat = longlatDF.drop(['clon10', 'clat10', 'pclon00', 'pclat00', 'pclon10', 'pclat10'], axis = 1)


# print(adjustedLonglat)
# print(stateDF)
# print(countyDF)

adjustedLonglat.to_sql("lat_long", con = engine, if_exists = "replace", dtype = {"fips": BigInteger, "clon00": Float,
                                                                                 "clat00": Float})
engine.execute("SELECT * FROM lat_long").fetchall()
print("lat_long table updated!")


stateDF.to_sql("state", con = engine, if_exists = "replace", dtype = {"date": Date, "state": Text, "fips": Integer,
                                                                           "cases": BigInteger, "deaths": BigInteger})
engine.execute("SELECT * FROM state").fetchall()
print("state table updated!")

countyDF.to_sql("county", con = engine, if_exists = "replace")
engine.execute("SELECT * FROM county").fetchall()
print("county table updated!")