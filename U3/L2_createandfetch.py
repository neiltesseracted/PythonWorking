import requests
import datetime
import sqlite3 as lite

cityraw="""Atlanta,GA,33.762909,-84.422675
Austin,TX,30.303936,-97.754355
Boston,MA,42.331960,-71.020173
Chicago,IL,41.837551,-87.681844
Cleveland,OH,41.478462,-81.679435
Denver,CO,39.761850,-104.881105
Las Vegas,NV,36.229214,-115.26008
Los Angeles,CA,34.019394,-118.410825
Miami,FL,25.775163,-80.208615
Minneapolis,MN,44.963324,-93.268320
Nashville,TN,36.171800,-86.785002
New Orleans,LA,30.053420,-89.934502
New York,NY,40.663619,-73.938589
Philadelphia,PA,40.009376,-75.133346
Phoenix,AZ,33.572154,-112.090132
Salt Lake City,UT,40.778996,-111.932630
San Francisco,CA,37.727239,-123.032229
Seattle,WA,47.620499,-122.350876
Washington,DC,38.904103,-77.017229"""
g=(l.split(',') for l in cityraw.splitlines())
city={}
for i in g:
    city[i[0]]=i[2]+','+i[3]
# now city is a dictionary

con=lite.connect('weather.db')
cur=con.cursor()
with con:
    cur.execute('DROP TABLE IF EXISTS maxtemp;')
    cur.execute('CREATE TABLE maxtemp (timestamp INT PRIMARY KEY, ' + ','.join( ['\''+ k + '\' REAL'for k in city.keys()] ) + ');')

# fetching data
key='https://api.forecast.io/forecast/0ff596c1401ec252d126604049ad2fb2/'
for d in xrange(30,0,-1):
    timestamp=(datetime.datetime.now() - datetime.timedelta(days=d)).strftime('%s')
    #time=timestamp.strftime('%Y-%m-%dT%H:%M:%S-0500')
    with con:
        cur.execute("INSERT INTO maxtemp (timestamp) VALUES (?);", (timestamp,) )

    for c in city.keys():
        ll=city[c]

        api=key+ll+','+timestamp
        print(c + ' ' + timestamp)

        r=requests.get(api, stream=True)

        maxtemp=r.json()['daily']['data'][0]['temperatureMax']

        with con:
            cur.execute("UPDATE maxtemp SET \'"+c+"\' = (?) WHERE timestamp=(?);", (maxtemp, timestamp) )

con.close()
print 'DONE!'








