import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools

def runtime_pie(df,platform):
  '''
  pie chart for runtime wise distribution of movies on platforms
  input param: df: input dataframe
  input param: platform: one of the platform
  '''
  assert(isinstance(df,pd.DataFrame))
  assert(isinstance(platform,str))
  moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
  imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
  dictyr = {}
  moviedf = df
  moviedf = moviedf.dropna()
  for i in range(len(moviedf.index)):
      if moviedf.iloc[i][platform] == 1:
          try:
              dictyr[moviedf.iloc[i]['Runtime']].append(moviedf.iloc[i]['Title'])
          except:
              dictyr[moviedf.iloc[i]['Runtime']] = []
              dictyr[moviedf.iloc[i]['Runtime']].append(moviedf.iloc[i]['Title'])
  dictyrnum = {}
  for keys,values in dictyr.items():
      dictyrnum[keys] = len(values)
  ordereddictyrnum = OrderedDict(sorted(dictyrnum.items(), key=lambda t: t[0]))
  minyrn = list(ordereddictyrnum.keys())[0]
  z =  (minyrn - 10)//10
  cnt = 10 + z
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
  i = 10 + z
  newdictyrchunksnum = {}
  for keys,values in dictyrchunksnum.items():
      newdictyrchunksnum[str(i)+'-'+str(i+29)] = values
      i = i+30
  labels = []
  data = []
  for keys,values in newdictyrchunksnum.items():
      labels.append(keys)
      data.append(values)
  plt.pie(data, labels=labels)
  plt.axis('equal')
  plt.show()
runtime_pie(moviedf,'Netflix')
runtime_pie(moviedf,'Hulu')
runtime_pie(moviedf,'Prime Video')
runtime_pie(moviedf,'Disney+')