# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:26:53 2021

@author: Mason
"""
import pandas

data = pandas.read_csv('FinalCombinedData.csv')
newFips = []

for fips in data['fips']:
    fips = str(fips)
    if len(fips) < 5:
        fips = "0" + fips
        newFips.append(fips)
    else:
        newFips.append(fips)

data['new_fips'] = newFips
data = data.drop(['fips'], axis = 1)

data.to_csv("AdjustedFinal.csv")