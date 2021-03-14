import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools
from wordcloud import WordCloud
def actors_wordcloud(df,platform):
  '''
  wordcloud for actors wise distribution of movies on platforms
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
  d = dict(zip(labels, data))
  wordcloud = WordCloud(collocations=False).generate_from_frequencies(d)
  plt.figure(figsize=(15,8))
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.savefig("wordc1"+".png", bbox_inches='tight')
  plt.show()
  plt.close()
actors_wordcloud(imdbdf,'Netflix')
actors_wordcloud(imdbdf,'Hulu')
actors_wordcloud(imdbdf,'Prime Video')
actors_wordcloud(imdbdf,'Disney+')