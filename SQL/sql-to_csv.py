# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:06:29 2021

@author: Mason
"""

import pandas
from sqlalchemy import create_engine
from config import password

engine = create_engine("postgresql://postgres:" + password + "@localhost/weatherCOVID")

data = engine.execute("SELECT date, state, county, new_fips, tempf, cases, deaths FROM covid_weather ORDER BY date, state, county;")

queryDF = pandas.DataFrame(data)
print(queryDF)

queryDF.to_csv("FINAL_data.csv")