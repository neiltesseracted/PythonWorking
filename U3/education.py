from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3 as lite
import statsmodels.formula.api as smf
import math

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
soup('table')[6].contents[1].contents[1]
tag=soup('table')[6].contents[1].contents[1].contents[4].contents[1].contents[1].contents[0].contents[3].contents[1]

#df=pd.DataFrame(columns=['Country', 'Year', 'Total', 'Men', 'Women'])

con= lite.connect('edu.db')
cur = con.cursor()
with con:
    cur.execute('DROP TABLE IF EXISTS edu;')
    cur.execute('CREATE TABLE edu (Country TEXT PRIMARY KEY, Year INT, Total INT, Men INT, Women INT);')

# Grab edu table
i=0
for tr in tag('tr')[4::]:
    """df.loc[i]= [''] + [ float('nan') ] * 4
    df.loc[i]=[tr('td')[0].string,
               tr('td')[1].string,
               tr('td')[4].string,
               tr('td')[7].string,
               tr('td')[10].string]"""
    with con:
        cur.execute("INSERT INTO edu VALUES (?,?,?,?,?);", (tr('td')[0].string,
                                                           tr('td')[1].string,
                                                           tr('td')[4].string,
                                                           tr('td')[7].string,
                                                           tr('td')[10].string))
    i+=1

# read gdp csv
import csv

with con:
    cur.execute('DROP TABLE IF EXISTS gdp;')
    cur.execute('CREATE TABLE gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010);')

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first FOUR lines
    next(inputFile)
    next(inputFile)
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-6]) + '");')

#merge table
with con:
    cur.execute("DROP TABLE IF EXISTS ge;")
    cur.execute("CREATE TABLE ge AS SELECT * FROM edu e, gdp g WHERE e.Country=g.country_name;")

# to df
df=pd.read_sql('SELECT * FROM ge;', con, index_col='Country')
df=df.replace('',float('nan'))
for col in df.columns[0:3]:
    if col!='country_name': df[col]=df[col].astype(int)
df['_2008']=df['_2008'].astype(float)

df.iloc[:,0:4].hist()

# log transform
df['_2008']=df['_2008'].map(lambda x: math.log(x))

est1 = smf.ols(formula="Total ~ _2008", data=df).fit()
print est1.summary()
