# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:05:08 2015

@author: neo
"""

import sqlite3 as sql
import os
import pandas as pd
os.chdir('/Users/neo/CLOUDSMAC/Dropbox/PythonWorking/somesql')

con = sql.connect('madb.db')
with con:
    print("sqlite version is %s" % con.cursor().execute('select sqlite_version()').fetchone())
    cur=con.cursor()
    
    cur.execute("select * from cities")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print
    
    tocities=( ('dummycity1','ZY'), ('dummycity2','ZZ'))
    cur.executemany("insert into cities values(?,?)", tocities)
    
    rows=cur.execute("select * from cities").fetchall()
    for row in rows:
        print(row)
    print
    df=pd.DataFrame(rows,columns=[desc[0] for desc in cur.description])
    print(df)
    print
    
    cur.execute("delete from cities where state='ZZ' or state='ZY'")
    
    rows=cur.execute("select * from cities").fetchall()
    for row in rows:
        print(row)
    print
    
