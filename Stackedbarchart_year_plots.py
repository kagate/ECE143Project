import csv
import numpy as np
from collections import Counter
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud 
import itertools
import random
tvdf = pd.read_csv('TV_shows_all_features.csv', converters = {'Timestamp':str})
moviedf = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv', converters = {'Timestamp':str})
imdbdf = pd.read_csv('IMDB-Movie-Data.csv', converters = {'Timestamp':str})
colors = ["#546E3D", "#9AFF47", "#E39E63", "#760000", "#9B2700", "#D8EA65", "#9B6900", "#C28500", "#FF950E", "#FF5D1C", "#DFB28A", "#C86A3D", "#CED09F"]
def create_dict(df,platform):
    ''' 
    Creates a dictionary for year wise list of movies and the number of movies for each set of 10 years
    params input: df: input dataframe
    params input: platform: platform for which dictionary is to be created
    params output: returns a dictionary of number of movies for each set of 10 years
    '''
    assert(isinstance(df,pd.DataFrame))
    assert(isinstance(platform,str))
    tvdf = df
    dictyr = {}
    for i in range(len(tvdf.index)):
        if tvdf.iloc[i][platform] == True:
            try:
                dictyr[tvdf.iloc[i]['Year']].append(tvdf.iloc[i]['Title'])
            except:
                dictyr[tvdf.iloc[i]['Year']] = []
                dictyr[tvdf.iloc[i]['Year']].append(tvdf.iloc[i]['Title'])
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
    newdictyrchunksnumnetflix = {}
    for keys,values in dictyrchunksnum.items():
        newdictyrchunksnumnetflix[str(i)+'-'+str(i+9)] = values
        i = i+10
    return newdictyrchunksnumnetflix
newdictyrchunksnumnetflix = create_dict(tvdf,'Netflix')
newdictyrchunksnumhulu = create_dict(tvdf,'Hulu')
newdictyrchunksnumpv = create_dict(tvdf,'Prime Video')
newdictyrchunksnumdp = create_dict(tvdf,'Disney+')
for k,v in newdictyrchunksnumhulu.items():
    if k in newdictyrchunksnumnetflix.keys():
        continue
    else:
        newdictyrchunksnumnetflix[k] = 0
for k,v in newdictyrchunksnumhulu.items():
    if k in newdictyrchunksnumpv.keys():
        continue
    else:
        newdictyrchunksnumpv[k] = 0
for k,v in newdictyrchunksnumhulu.items():
    if k in newdictyrchunksnumdp.keys():
        continue
    else:
        newdictyrchunksnumdp[k] = 0
yrdict_tv = {}
for k,v in newdictyrchunksnumnetflix.items():
    try:
        yrdict_tv[k]
    except:
        yrdict_tv[k] = {}
    yrdict_tv[k]['Netflix'] = v
for k,v in newdictyrchunksnumhulu.items():
    try:
        yrdict_tv[k]
    except:
        yrdict_tv[k] = {}
    yrdict_tv[k]['Hulu'] = v
for k,v in newdictyrchunksnumpv.items():
    try:
        yrdict_tv[k]
    except:
        yrdict_tv[k] = {}
    yrdict_tv[k]['Prime Video'] = v

for k,v in newdictyrchunksnumdp.items():
    try:
        yrdict_tv[k]
    except:
        yrdict_tv[k] = {}
    yrdict_tv[k]['Disney+'] = v
newdictyrchunksnumnetflix_m = create_dict(moviedf,'Netflix')
newdictyrchunksnumhulu_m = create_dict(moviedf,'Hulu')
newdictyrchunksnumpv_m = create_dict(moviedf,'Prime Video')
newdictyrchunksnumdp_m = create_dict(moviedf,'Disney+')
for k,v in newdictyrchunksnumpv_m.items():
    if k in newdictyrchunksnumnetflix_m.keys():
        continue
    else:
        newdictyrchunksnumnetflix_m[k] = 0
for k,v in newdictyrchunksnumpv_m.items():
    if k in newdictyrchunksnumhulu_m.keys():
        continue
    else:
        newdictyrchunksnumhulu_m[k] = 0
for k,v in newdictyrchunksnumpv_m.items():
    if k in newdictyrchunksnumdp_m.keys():
        continue
    else:
        newdictyrchunksnumdp_m[k] = 0
yrdict_m = {}
for k,v in newdictyrchunksnumnetflix_m.items():
    try:
        yrdict_m[k]
    except:
        yrdict_m[k] = {}
    yrdict_m[k]['Netflix'] = v
for k,v in newdictyrchunksnumhulu_m.items():
    try:
        yrdict_m[k]
    except:
        yrdict_m[k] = {}
    yrdict_m[k]['Hulu'] = v
for k,v in newdictyrchunksnumpv_m.items():
    try:
        yrdict_m[k]
    except:
        yrdict_m[k] = {}
    yrdict_m[k]['Prime Video'] = v
for k,v in newdictyrchunksnumdp_m.items():
    try:
        yrdict_m[k]
    except:
        yrdict_m[k] = {}
    yrdict_m[k]['Disney+'] = v
'''
Uses a dictionary of dictionaries to take year wise data of number of movies on each platform Netflix, Hulu, Prime Video 
and Disney+ and plots a stacked bar chart for representation
yrdict_m: dictionary of dictionaries of year wise distribution of platforms and number of movies
'''
assert(isinstance(yrdict_m,dict))
for k,v in yrdict_m.items():
    assert(isinstance(v,dict))
plt.figure(figsize=(20,10))
plt.bar(yrdict_m['1900-1909'].keys(), yrdict_m['1900-1909'].values(), width=0.4, align='center', label='1900-1909', color=colors[0])
plt.bar(yrdict_m['1910-1919'].keys(), yrdict_m['1910-1919'].values(), bottom=[yrdict_m['1900-1909'][i] for i in yrdict_m['1910-1919'].keys()], width=0.4, align='center', label='1910-1919', color=colors[1])
plt.bar(yrdict_m['1920-1929'].keys(), yrdict_m['1920-1929'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i] for i in yrdict_m['1920-1929'].keys()], width=0.4, align='center', label='1920-1929',color  = colors[2])
plt.bar(yrdict_m['1930-1939'].keys(), yrdict_m['1930-1939'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i] for i in yrdict_m['1930-1939'].keys()], width=0.4, align='center', label='1930-1939', color = colors[3])
plt.bar(yrdict_m['1940-1949'].keys(), yrdict_m['1940-1949'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i] for i in yrdict_m['1940-1949'].keys()], width=0.4, align='center', label='1940-1949',color = colors[4])
plt.bar(yrdict_m['1950-1959'].keys(), yrdict_m['1950-1959'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i] for i in yrdict_m['1950-1959'].keys()], width=0.4, align='center', label='1950-1959', color = colors[5])
plt.bar(yrdict_m['1960-1969'].keys(), yrdict_m['1960-1969'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i] for i in yrdict_m['1960-1969'].keys()], width=0.4, align='center', label='1960-1969', color = colors[6])
plt.bar(yrdict_m['1970-1979'].keys(), yrdict_m['1970-1979'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i] for i in yrdict_m['1970-1979'].keys()], width=0.4, align='center', label='1970-1979', color = colors[7])
plt.bar(yrdict_m['1980-1989'].keys(), yrdict_m['1980-1989'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i]+yrdict_m['1970-1979'][i] for i in yrdict_m['1980-1989'].keys()], width=0.4, align='center', label='1980-1989', color = colors[8])
plt.bar(yrdict_m['1990-1999'].keys(), yrdict_m['1990-1999'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i]+yrdict_m['1970-1979'][i]+yrdict_m['1980-1989'][i] for i in yrdict_m['1990-1999'].keys()], width=0.4, align='center', label='1990-1999', color = colors[9])
plt.bar(yrdict_m['2000-2009'].keys(), yrdict_m['2000-2009'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i]+yrdict_m['1970-1979'][i]+yrdict_m['1980-1989'][i]+yrdict_m['1990-1999'][i] for i in yrdict_m['2000-2009'].keys()], width=0.4, align='center', label='2000-2009', color = colors[10])
plt.bar(yrdict_m['2010-2019'].keys(), yrdict_m['2010-2019'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i]+yrdict_m['1970-1979'][i]+yrdict_m['1980-1989'][i]+yrdict_m['1990-1999'][i]+yrdict_m['2000-2009'][i] for i in yrdict_m['2010-2019'].keys()], width=0.4, align='center', label='2010-2019', color = colors[11])
plt.bar(yrdict_m['2020-2029'].keys(), yrdict_m['2020-2029'].values(), bottom=[yrdict_m['1900-1909'][i]+yrdict_m['1910-1919'][i]+yrdict_m['1920-1929'][i]+yrdict_m['1930-1939'][i]+yrdict_m['1940-1949'][i]+yrdict_m['1950-1959'][i]+yrdict_m['1960-1969'][i]+yrdict_m['1970-1979'][i]+yrdict_m['1980-1989'][i]+yrdict_m['1990-1999'][i]+yrdict_m['2000-2009'][i]+yrdict_m['2010-2019'][i] for i in yrdict_m['2020-2029'].keys()], width=0.4, align='center', label='2020-2029', color = colors[12])
plt.xlabel('Platforms')
plt.ylabel('Number of Movies')
ax = plt.axes() 
ax.set_facecolor("#f5e7b7") 
SMALL_SIZE = 20
plt.rcParams['figure.facecolor'] = '#f5e7b7'
plt.rc('font', size=SMALL_SIZE) 
plt.rc('axes', titlesize=SMALL_SIZE)  
plt.legend()
'''
Uses a dictionary of dictionaries to take year wise data of number of TV Shows on each platform Netflix, Hulu, Prime Video 
and Disney+ and plots a stacked bar chart for representation
yrdict_tv: dictionary of dictionaries of year wise distribution of platforms and number of TV Shows
'''
assert(isinstance(yrdict_tv,dict))
for k,v in yrdict_m.items():
    assert(isinstance(v,dict))
plt.figure(figsize=(20,10))
plt.bar(yrdict_tv['1950-1959'].keys(), yrdict_tv['1950-1959'].values(), width=0.4, align='center', label='1950-1959', color=colors[5])
plt.bar(yrdict_tv['1960-1969'].keys(), yrdict_tv['1960-1969'].values(), bottom=[yrdict_tv['1950-1959'][i] for i in yrdict_tv['1960-1969'].keys()], width=0.4, align='center', label='1960-1969', color = colors[6])
plt.bar(yrdict_tv['1970-1979'].keys(), yrdict_tv['1970-1979'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i] for i in yrdict_tv['1970-1979'].keys()], width=0.4, align='center', label='1970-1979', color = colors[7])
plt.bar(yrdict_tv['1980-1989'].keys(), yrdict_tv['1980-1989'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i]+yrdict_tv['1970-1979'][i] for i in yrdict_tv['1980-1989'].keys()], width=0.4, align='center', label='1980-1989', color = colors[8])
plt.bar(yrdict_tv['1990-1999'].keys(), yrdict_tv['1990-1999'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i]+yrdict_tv['1970-1979'][i]+yrdict_tv['1980-1989'][i] for i in yrdict_tv['1990-1999'].keys()], width=0.4, align='center', label='1990-1999', color = colors[9])
plt.bar(yrdict_tv['2000-2009'].keys(), yrdict_tv['2000-2009'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i]+yrdict_tv['1970-1979'][i]+yrdict_tv['1980-1989'][i]+yrdict_tv['1990-1999'][i] for i in yrdict_tv['2000-2009'].keys()], width=0.4, align='center', label='2000-2009', color = colors[10])
plt.bar(yrdict_tv['2010-2019'].keys(), yrdict_tv['2010-2019'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i]+yrdict_tv['1970-1979'][i]+yrdict_tv['1980-1989'][i]+yrdict_tv['1990-1999'][i]+yrdict_tv['2000-2009'][i] for i in yrdict_tv['2010-2019'].keys()], width=0.4, align='center', label='2010-2019', color = colors[11])
plt.bar(yrdict_tv['2020-2029'].keys(), yrdict_tv['2020-2029'].values(), bottom=[yrdict_tv['1950-1959'][i]+yrdict_tv['1960-1969'][i]+yrdict_tv['1970-1979'][i]+yrdict_tv['1980-1989'][i]+yrdict_tv['1990-1999'][i]+yrdict_tv['2000-2009'][i]+yrdict_tv['2010-2019'][i] for i in yrdict_tv['2020-2029'].keys()], width=0.4, align='center', label='2020-2029', color = colors[12])
plt.xlabel('Platforms')
plt.ylabel('Number of TV Shows')
SMALL_SIZE = 20
ax = plt.axes() 
ax.set_facecolor("#f5e7b7") 
plt.rcParams['figure.facecolor'] = '#f5e7b7'
plt.rc('font', size=SMALL_SIZE)          
plt.rc('axes', titlesize=SMALL_SIZE)  
plt.rcParams['axes.facecolor']='#f5e7b7'
plt.legend()