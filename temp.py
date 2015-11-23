# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import csv
import pandas as pd
import sqlite3 as sql
os.chdir('/Users/neo/CLOUDSMAC/Dropbox/PythonWorking/')

"""
with open('./lecz/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header=next(inputFile).rstrip().split(',')
    for line in inputFile:
        line=line.rstrip().split(',')
        if line[0]=='Asia':
            print(line)
    print(header[0])
"""
        
dataframe=pd.read_csv('lecz/lecz-urban-rural-population-land-area-estimates_codebook.csv')
dataframe2=pd.read_csv('lecz/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

#blah!

