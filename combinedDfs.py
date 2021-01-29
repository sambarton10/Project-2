import os
import pandas as pd

df1 = pd.read_csv('./decemberDF.csv')
#print(df1)

df2 = pd.read_csv('./decemberDF31.csv')
#print(df2)

frames = [df1, df2]
result = pd.concat(frames)

#print(result)

result.to_csv('./combinedDF.csv', index=False, header=True)