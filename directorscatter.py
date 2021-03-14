import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools
moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
def director_scatter(df,platform):
    moviedf = df
    dictyr = {}
    directors = ''
    moviedf = moviedf.dropna()
    for i in range(len(moviedf.index)):
        listdirectors = []
        if moviedf.iloc[i][platform] == 1:
            directors = moviedf.iloc[i]['Directors']
            listdirectors = directors.split(',')
            for currdir in listdirectors:
                try:
                    dictyr[currdir].append(moviedf.iloc[i]['Title'])
                except:
                    dictyr[currdir] = []
                    dictyr[currdir].append(moviedf.iloc[i]['Title'])
    dictyrnum = {}
    for keys,values in dictyr.items():
        dictyrnum[keys] = len(values)
    ordereddictyrnum = OrderedDict(sorted(dictyrnum.items(), key=lambda t: t[0]))
    labels = []
    data = []
    labelscnt = []
    for keys,values in ordereddictyrnum.items():
        labels.append(keys)
        data.append(values)
    for i in range(len(labels)):
        labelscnt.append(labels.index(labels[i]))
    plt.scatter(labelscnt,data)
    fig = plt.gcf()
    fig.set_size_inches(20,20)
    for i, txt in enumerate(labels):
        plt.annotate(txt, (labelscnt[i],data[i]))
    plt.show()
director_scatter(moviedf,'Netflix')
director_scatter(moviedf,'Hulu')
director_scatter(moviedf,'Prime Video')
director_scatter(moviedf,'Disney+')