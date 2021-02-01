import pandas as pd
pd.options.mode.chained_assignment = None

rawCOVID = pd.read_csv('./draftJoin.csv')
nonDates = pd.read_csv('./raw-data/non-dates.csv')
weatherData = pd.read_csv('./weatherData.csv')

weatherData.columns = ['Coords', 'date', 'Temp']


weatherData[["latitude","longitude"]] = weatherData.Coords.str.split(",",expand=True)
test = pd.DataFrame(weatherData)

test.drop(columns=['Coords'], axis=1, inplace=True)

print(test)

nonDatesList = nonDates['date'].tolist()

#print(nonDatesList)

df = rawCOVID[~rawCOVID['date'].isin(nonDatesList)]
df.dropna(inplace=True)

df['date']=pd.to_datetime(df.date)

df.sort_values(by=['date', 'state'], inplace=True, ascending=(True, True))

df.drop(columns=['index', 'longitude'], axis=1, inplace=True)

df.reset_index()
print(df)
test['date']=test['date'].astype(str)
test['Temp']=test['Temp'].astype(str)
df['date']=df['date'].astype(str)
df['fips']=df['fips'].astype(str)
#df['longitude']=df['longitude'].astype(str)
df['latitude']=df['latitude'].astype(str)
df['cases']=df['cases'].astype(str)
df['deaths']=df['deaths'].astype(str)
print(test.dtypes)
print(df.dtypes)

frames = [test, df]

result = pd.merge(test, df, on=['latitude','date'])

print(result)

result.to_csv('./test.csv')