# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:06:29 2021

@author: Mason
"""

import pandas
from sqlalchemy import create_engine
from config import password

engine = create_engine("postgresql://postgres:" + password + "@localhost/weatherCOVID")

data = engine.execute("SELECT weather.date, county, state, fips, clon10, longitude, latitude, clat10, cases, deaths, tempf FROM county LEFT JOIN lat_long USING (fips) LEFT JOIN weather ON lat_long.clon10 = weather.longitude WHERE tempf IS NOT NULL ORDER BY state;")

queryDF = pandas.DataFrame(data)

queryDF.to_csv("testJoin.csv")