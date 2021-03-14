import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools

def desc(df,platform):
  '''
  wordcloud for description of movies on platforms
  input param: df: input dataframe
  input param: platform: one of the platform
  '''
  assert(isinstance(df,pd.DataFrame))
  assert(isinstance(platform,str))
  moviedf = pd.read_csv('data/MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
  imdbdf = pd.read_csv('data/IMDB-Movie-Data.csv', converters = {'Timestamp':str})
  imdbdf = df
  directors = ''
  dictyr = {}
  imdbdf = imdbdf.dropna()
  listdirectors = []
  for i in range(len(imdbdf.index)):
      movie  = imdbdf.iloc[i]['Title']
      valdf = (moviedf.loc[moviedf['Title'] == movie])
      if valdf.empty:
          continue
      jval = (valdf['Netflix'].values[0])
      if jval == 1:
          directors = imdbdf.iloc[i]['Description']
          listdirectors.append(directors.split(','))
  mergedlist = list(itertools.chain.from_iterable(listdirectors))
  unique_string=(" ").join(mergedlist)
  wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
  plt.figure(figsize=(15,8))
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.savefig("wordc1"+".png", bbox_inches='tight')
  plt.show()
  plt.close()
desc(imdbdf,'Netflix')
desc(imdbdf,'Hulu')
desc(imdbdf,'Prime Video')
desc(imdbdf,'Disney+')