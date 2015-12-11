import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite


r = requests.get('http://www.citibikenyc.com/stations/json', stream=True)

station = r.json()['stationBeanList']

r.iter_content()
"""
n=0
for i in r.iter_lines():
    n+=1
    print(i)
    if n>32: break
    """

df = json_normalize(r.json()['stationBeanList'])

df['availableBikes'].hist()
plt.show()

print(df['statusValue'].value_counts())

df['availableBikes'].mean()
df['availableBikes'].median()
df['availableBikes'][df['statusValue'] == 'In Service'].mean()
df['availableBikes'][df['statusValue'] == 'In Service'].median()

cmd="""CREATE TABLE citibike_reference (
    id INT PRIMARY KEY,
    totalDocks INT,
    city TEXT,
    altitude INT,
    stAddress2 TEXT,
    longitude NUMERIC,
    postalCode TEXT,
    testStation TEXT,
    stAddress1 TEXT,
    stationName TEXT,
    landMark TEXT,
    latitude NUMERIC,
    location TEXT
)"""

con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
    cur.execute(cmd)

sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

station_ids=df['id'].tolist()
station_ids = ['_' + str(x) + ' INT' for x in station_ids]
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")


