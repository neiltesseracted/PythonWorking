# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:23:21 2015

@author: neo
"""

import sqlite3 as sql, os, pandas as pd, csv


os.chdir(os.getcwd())

#con = sql.connect('madb.db')

with sql.connect('madb.db') as con:
    cur=con.cursor()
    cur.execute("drop table if exists weather;")
    cur.execute("drop table if exists cities;")
    cur.execute("drop table if exists weather_import;")
    cur.execute("drop table if exists city_weather;")  
    
    #create cities
    cities=(
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')
    )
    cur.execute("create table cities (city text, state text);")
    cur.executemany("insert into cities values (?,?)",cities)
    
    #import weather into an intermediary all string table weather_import
    #I was doing it in sqlite, using a intermediary table to read fixed width csv
    #then I found out that python can't use sqlite's dot command
    #probably csvreader can read fixed width? but doing sqlite way anyway
    cur.execute("create table weather_import(line char);")
    with open('weather.csv','r') as f:
        R=csv.reader(f)
        for row in R:
            cur.execute("insert into weather_import values (?)", row)
    
    #cur.execute(".import weather.csv weather_import") #nope it won't work
    
    #read data from weather_import to weather
    cur.execute("create table weather as \
                    select trim(substr(line,2,16)) as City,\
                           cast(trim(substr(line,18,8)) as integer) as Year,\
                           trim(substr(line,26,12)) as Warm_Month,\
                           trim(substr(line,38,12)) as Cold_Month,\
                           cast(trim(substr(line,50)) as integer) as Average_High \
                    from weather_import;")
    cur.execute("delete from weather where rowid=1;")
    
    #rows=cur.execute("select * from weather;").fetchall()
    #dfw=pd.DataFrame(rows,columns=[desc[0] for desc in cur.description])
    #dfcity=pd.DataFrame(cur.execute("select * from cities;").fetchall(), columns=[desc[0] for desc in cur.description])
    
    #join two tables
    cur.execute("create table city_weather as \
                select w.*, c.state from weather as w left join cities as c  \
                on w.city=c.city;")
    rows=cur.execute("select * from city_weather;").fetchall()
    df=pd.DataFrame(rows,columns=[desc[0] for desc in cur.description])
    
    rows=cur.execute("select city, state from city_weather where warm_month='July' \
                    order by average_high desc;").fetchall()
    
    print("The cities that are warmest in July are: ")
    for row in rows:
        print(str(row[0])+ ', ' + str(row[1]))
