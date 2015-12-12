import pandas as pd
import sqlite3 as lite
import collections
import datetime

con = lite.connect('../citi_bike.db')
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time", con, index_col='execution_time')

hour_change = collections.defaultdict(int)

for col in df.columns:
    vals=df[col].tolist()
    id=col[1:]
    chg=0
    for k, v in enumerate(vals):
        if k < len(vals) - 1:
            chg += abs(vals[k] - vals[k+1])
    hour_change[int(id)] = chg

winner=max(hour_change, key=lambda x: hour_change[x])

cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (winner,))
data = cur.fetchone()
print("The most active station is station id %s at %s latitude: %s longitude: %s " % data)
print("With %d bicycles coming and going in the hour between %s and %s" % (
    hour_change[winner],
    datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S'),
    datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S'),
))

import matplotlib.pyplot as plt

plt.bar(hour_change.keys(), hour_change.values())
plt.show()

