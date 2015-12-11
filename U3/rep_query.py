import requests
import sqlite3 as lite
import time
import collections
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse

r = requests.get('http://www.citibikenyc.com/stations/json', stream=True)
con = lite.connect('citi_bike.db')
cur = con.cursor()
with con:
    cur.execute('DELETE FROM available_bikes')

for i in range(60):
    #take the string and parse it into a Python datetime object
    exec_time = parse(r.json()['executionTime'])

    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

    #loop through the stations in the station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    with con:
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

    time.sleep(60)

con.close()
