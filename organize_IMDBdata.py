'''ECE 143 Project'''

import csv
import numpy as np
from collections import Counter

# load tv_shows csv 
TVshowData = []
TVshowsCSVFile = open('/Users/laurabecerra/code/finalproject/ECE143Project/tv_shows.csv', encoding="utf8")
TVshowsCSVReader = csv.reader(TVshowsCSVFile)
TVshowData = list(TVshowsCSVReader)
NumTVshows = len(TVshowData)

IMDBTVShowData = []
with open('/Users/laurabecerra/code/finalproject/ECE143Project/title.basics.csv', encoding="utf8") as IMDBTVShowDataFile:
    IMDBDataReader = csv.reader(IMDBTVShowDataFile)
    IMDBTVShowData = list(IMDBDataReader)

#get genre data
for row in TVshowData:
    title = row[1]
    for row_IMDB in IMDBTVShowData:
        if title == row_IMDB[2] and row_IMDB[1] == 'tvSeries' and not row_IMDB[11] == None:
            row.append(row_IMDB[8])  
            break

with open('TV_shows_with_genres.csv','w+',newline='') as new_file:
    write = csv.writer(new_file)
    write.writerows(row for row in TVshowData)
