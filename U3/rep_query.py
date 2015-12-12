import requests
import sqlite3 as lite
import time
import collections
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse

con = lite.connect('../citi_bike.db')
cur = con.cursor()
with con:
    cur.execute('DELETE FROM available_bikes')

for i in range(60):
    r = requests.get('http://www.citibikenyc.com/stations/json', stream=True)
    #take the string and parse it into a Python datetime object
    exec_time = parse(r.json()['executionTime'])
    print(exec_time)

    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

    #loop through the stations in the station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    with con:
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

    if i < 59:
        if i==58: print(str(59-i) + " run to go. Next run in 60 sec.")
        else: print(str(59-i) + " runs to go. Next run in 60 sec.")
        time.sleep(30)
        print("Next run in 30 sec.")
        time.sleep(20)
        print("Next run in 10 sec.")
        time.sleep(10)
    else:
        print("60 runs finished")


con.close()
