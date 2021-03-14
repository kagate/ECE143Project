import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools

def country_pie(df,platform):
  '''
  pie chart for country wise distribution of movies on platforms
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
          directors = moviedf.iloc[i]['Country']
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
  plt.pie(data, labels = labels)
  plt.axis('equal')
  plt.show()
country_pie(moviedf,'Netflix')
country_pie(moviedf,'Hulu')
country_pie(moviedf,'Prime Video')
country_pie(moviedf,'Disney+')