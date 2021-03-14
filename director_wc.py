import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools
from wordcloud import WordCloud

def create_wordcloud_director(df,platform):
    '''
    Wordcloud for director distribution of movies on platforms
    input param: df: input dataframe
    input param: platform: one of the platform
    '''
    assert(isinstance(df,pd.DataFrame))
    assert(isinstance(platform,str))
    moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
    imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
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
    d = dict(zip(labels, data))
    wordcloud = WordCloud(collocations=False).generate_from_frequencies(d)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("wordc1"+".png", bbox_inches='tight')
    plt.show()
    plt.close()
create_wordcloud_director(moviedf,'Netflix')
create_wordcloud_director(moviedf,'Hulu')
create_wordcloud_director(moviedf,'Prime Video')
create_wordcloud_director(moviedf,'Disney+')