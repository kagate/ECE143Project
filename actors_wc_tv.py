import xlrd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import OrderedDict
import itertools
from wordcloud import WordCloud 
import random
import itertools
def actors_wc(df,platform,func):
  '''
  wordcloud for actors for TV Shows on platforms
  input param: df: input dataframe
  input param: platform: one of the platform
  '''
  tvdf = pd.read_csv('data/TV_shows_all_features.csv', converters = {'Timestamp':str})
  assert(isinstance(df,pd.DataFrame))
  assert(isinstance(platform,str))
  tvdf = df
  dictyr = {}
  directors = ''
  tvdf = tvdf.dropna()
  for i in range(len(tvdf.index)):
      listdirectors = []
      if tvdf.iloc[i][platform] == True:
          directors = tvdf.iloc[i]['Actors']
          listdirectors = directors.split(',')
          for currdir in listdirectors:
              if currdir == '[]':
                continue
              currdir = currdir.replace("'","")
              currdir = currdir.replace("[","")
              currdir = currdir.replace("]","")
              try:
                  dictyr[currdir].append(tvdf.iloc[i]['Title'])
              except:
                  dictyr[currdir] = []
                  dictyr[currdir].append(tvdf.iloc[i]['Title'])
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
  wordcloud = WordCloud(collocations=False,background_color='#f5e7b7',).generate_from_frequencies(d)
  plt.figure(figsize=(15,8))
  plt.imshow(wordcloud.recolor(color_func=func))
  plt.axis("off")
  plt.savefig("wordc-netflix-tv-act"+".png", bbox_inches='tight')
  plt.show()
  plt.close()
actors_wc(tvdf,'Netflix',red_func)
actors_wc(tvdf,'Hulu',green_func)
actors_wc(tvdf,'Prime Video',blue_func)
actors_wc(tvdf,'Disney+',purple_func)