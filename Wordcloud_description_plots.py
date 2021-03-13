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
def red_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    '''
    Plotting wordcloud font as red
    '''
    assert(isinstance(word,str))
    return "hsl(0, 100%%, %d%%)" % random.randint(30, 50)

def green_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    '''
    Plotting wordcloud font as green
    '''
    assert(isinstance(word,str))
    return "hsl(100, 100%%, %d%%)" % random.randint(20, 40)
def blue_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    '''
    Plotting wordcloud font as blue
    '''
    assert(isinstance(word,str))
    return "hsl(190, 100%%, %d%%)" % random.randint(40, 60)
def purple_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    '''
    Plotting wordcloud font as purple
    '''
    assert(isinstance(word,str))
    return "hsl(300, 47%%, %d%%)" % random.randint(60, 80)
def create_Wordcloud(df,platform,color):
    '''
    Takes the dataframe, the platform and the color function as the input and plots the wordcloud
    param input: df: input dataframe
    param input: platform: input platform 
    param input: color: color function 
    '''
    assert(isinstance(df,pd.DataFrame))
    assert(isinstance(platform,str))
    assert(isinstance(color,str))
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
        jval = (valdf[platform].values[0])
        if jval == 1:
            directors = imdbdf.iloc[i]['Description']
            listdirectors.append(directors.split(','))
    mergedlist = list(itertools.chain.from_iterable(listdirectors))
    unique_string=(" ").join(mergedlist)
    wordcloud = WordCloud(width = 1000, height = 500, background_color='#f5e7b7').generate(unique_string)
    if color == 'red':
        func = red_func
    if color == 'green':
        func = green_func
    if color == 'blue':
        func = blue_func
    if color == 'purple':
        func = purple_func
    plt.imshow(wordcloud.recolor(color_func=func))
    plt.axis("off")
    plt.savefig("wordc1_net_mov_d"+".png", bbox_inches='tight')
    plt.show()
    plt.close()
create_Wordcloud(imdbdf,'Netflix','red')
create_Wordcloud(imdbdf,'Hulu','green')
create_Wordcloud(imdbdf,'Prime Video','blue')
create_Wordcloud(imdbdf,'Disney+','purple')