import pandas as pd
import sqlite3 as lite
import datetime

con=lite.connect('weather.db')
df=pd.read_sql('SELECT * FROM maxtemp ORDER BY timestamp;', con, index_col='timestamp')
con.close()

diff=df.diff().dropna()
winner=(df.max()-df.min()).idxmax()

dateformat='%Y-%m-%d'
periodstart=datetime.datetime.utcfromtimestamp(df.index.min()).strftime(dateformat)
perioduntil=datetime.datetime.utcfromtimestamp(df.index.max()).strftime(dateformat)

winner_hi=(df[winner].idxmax(), df[winner][df[winner].idxmax()])
winner_lo=(df[winner].idxmin(), df[winner][df[winner].idxmin()])

print("City with greatest range in daily temperatureMax throughout past month is %s. " % winner)
print("Daily temperatureMax observed from %s to %s, " % (periodstart,perioduntil) )
print("during which highest temperatureMax in %s was %d F on %s, lowest temperatureMax %d F on %s." % (
        winner,
        winner_hi[1],
        datetime.datetime.utcfromtimestamp(winner_hi[0]).strftime(dateformat),
        winner_lo[1],
        datetime.datetime.utcfromtimestamp(winner_lo[0]).strftime(dateformat)
        )
      )


