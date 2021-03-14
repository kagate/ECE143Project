import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools
moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
dictyr = {}
for i in range(len(moviedf.index)):
    try:
        dictyr[moviedf.iloc[i]['Year']].append(moviedf.iloc[i]['Title'])
    except:
        dictyr[moviedf.iloc[i]['Year']] = []
        dictyr[moviedf.iloc[i]['Year']].append(moviedf.iloc[i]['Title'])
dictyrnum = {}
for keys,values in dictyr.items():
    dictyrnum[keys] = len(values)
ordereddictyrnum = OrderedDict(sorted(dictyrnum.items(), key=lambda t: t[0]))
minyr = list(ordereddictyrnum.keys())[0]
print(minyr)
def plot_yr_pie(df,platform):
    '''
    Pie charts for year wise distribution of movies on platforms
    input param: df: input dataframe
    input param: platform: one of the platform
    '''
    moviedf = df
    dictyr = {}
    for i in range(len(moviedf.index)):
        if moviedf.iloc[i][platform] == 1:
            try:
                dictyr[moviedf.iloc[i]['Year']].append(moviedf.iloc[i]['Title'])
            except:
                dictyr[moviedf.iloc[i]['Year']] = []
                dictyr[moviedf.iloc[i]['Year']].append(moviedf.iloc[i]['Title'])
    dictyrnum = {}
    for keys,values in dictyr.items():
        dictyrnum[keys] = len(values)
    ordereddictyrnum = OrderedDict(sorted(dictyrnum.items(), key=lambda t: t[0]))
    minyrn = list(ordereddictyrnum.keys())[0]
    z =  (minyrn - 1900)//10
    cnt = 1900 + z*10
    cntfil = 0
    dictyrchunksnum = {}
    for keys in ordereddictyrnum.keys():
        try:
            cntfil = (keys-cnt)//10
            dictyrchunksnum[cntfil] = dictyrchunksnum[cntfil] + ordereddictyrnum[keys]
        except:
            cntfil = (keys-cnt)//10
            dictyrchunksnum[cntfil] = 0
            dictyrchunksnum[cntfil] = dictyrchunksnum[cntfil] + ordereddictyrnum[keys]
    i = 1900 + z*10
    newdictyrchunksnum = {}
    for keys,values in dictyrchunksnum.items():
        newdictyrchunksnum[str(i)+'-'+str(i+9)] = values
        i = i+10
    labels = []
    data = []
    for keys,values in newdictyrchunksnum.items():
        labels.append(keys)
        data.append(values)
    plt.pie(data, labels=labels)
    plt.axis('equal')
    plt.show()
plot_yr_pie(moviedf,'Netflix')
plot_yr_pie(moviedf,'Hulu')
plot_yr_pie(moviedf,'Prime Video')
plot_yr_pie(moviedf,'Disney+')