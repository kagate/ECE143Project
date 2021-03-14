import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools

def actors_scatter(df,platform):
    '''
  scatter plot for actors wise distribution of movies on platforms
  input param: df: input dataframe
  input param: platform: one of the platform
  '''
  assert(isinstance(df,pd.DataFrame))
  assert(isinstance(platform,str))
  moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
  imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
  imdbdf = df
  dictyr = {}
  directors = ''
  imdbdf = imdbdf.dropna()
  for i in range(len(imdbdf.index)):
      listdirectors = []
      movie  = imdbdf.iloc[i]['Title']
      valdf = (moviedf.loc[moviedf['Title'] == movie])
      if valdf.empty:
          continue
      jval = (valdf[platform].values[0])
      if jval == 1:
          directors = imdbdf.iloc[i]['Actors']
          listdirectors = directors.split(',')
          for currdir in listdirectors:
              try:
                  dictyr[currdir].append(imdbdf.iloc[i]['Title'])
              except:
                  dictyr[currdir] = []
                  dictyr[currdir].append(imdbdf.iloc[i]['Title'])
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
actors_scatter(imdbdf,'Netflix')
actors_scatter(imdbdf,'Hulu')
actors_scatter(imdbdf,'Prime Video')
actors_scatter(imdbdf,'Disney+')