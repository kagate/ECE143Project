''' Consolidate TV show CSV files '''
def TVshow_IMDB_clean_data(file_name='tv_shows.csv'):
    ''' Remove TV shows without IMDB data '''
    import pandas as pd

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    TVshow_IMDB = pd.read_csv('title.basics.csv',dtype={'tconst':object, 'titleType':str, 'primaryTitle':str, 'originalTitle':str, 'isAdult':bool, 'startYear':object, 'endYear':object, 'runtimeMinutes':object, 'genres':object})

    # generate dictionary of movies in tv_shows.csv with id numbers in IMDB data
    TVshow_IMDB.drop(TVshow_IMDB[TVshow_IMDB['titleType'] != 'tvSeries'].index, inplace = True) # remove rows with title types other than tv series
    TVshow_IMDB_clean = TVshow_IMDB[TVshow_IMDB['primaryTitle'].isin(TVshow_data.Title)] # keep only the rows with titles in tvshow_data
    TVshow_IMDB_clean = TVshow_IMDB_clean.set_index('tconst') # set indices to be tconst
    TVshow_id_dict = pd.Series(TVshow_IMDB_clean.index,index=TVshow_IMDB_clean.primaryTitle).to_dict() # generate dictionary of movies in tv_shows.csv and their id numbers from IMDB data

    return TVshow_id_dict, TVshow_IMDB_clean, TVshow_data

def TVshow_genres(file_name='tv_shows.csv'):
    import pandas as pd
    import numpy as np
    from collections import Counter

    # Other functions
    import platform_plots

    TVshow_id_dict, TVshow_IMDB_clean, TVshow_data = TVshow_IMDB_clean_data(file_name)
    
    # get genres for each movie in TVshow_id_dict
    TVshow_data['Genres'] = '' # make column for genres
    for index,row in TVshow_data.iterrows():
        show = row[0]
        if show in TVshow_id_dict: # if show title is in id dictionary
            id_num = TVshow_id_dict[show] # get id number from dictionary
            TVshow_data['Genres'][index] = TVshow_IMDB_clean.loc[id_num,'genres'] # put genre from IMDB data in Genres column of TVshow_data

    TVshow_data.drop(TVshow_data[TVshow_data['Genres'] == ''].index, inplace=True) # remove rows without genres
    TVshow_data.drop(TVshow_data[TVshow_data['Genres'] == '\\N'].index, inplace=True) # remove rows with genres '\\N'
    TVshow_data = TVshow_data.reset_index()

    # the following is just to plot using the old pie chart code
    # NetflixGenresTemp_TVShow = [] # make empty array for TV show genres
    # HuluGenresTemp_TVShow = [] # make empty array for TV show genres
    # PrimeGenresTemp_TVShow = [] # make empty array for TV show genres
    # DisneyGenresTemp_TVShow = [] # make empty array for TV show genres

    # for index,row in TVshow_data.iterrows():
    #     if row['Netflix']: # if the show is on Netflix platform
    #         NetflixGenresTemp_TVShow.append(row['Genres'].split(','))
    #     elif row['Hulu']:
    #         HuluGenresTemp_TVShow.append(row['Genres'].split(','))
    #     elif row['Prime Video']:
    #         PrimeGenresTemp_TVShow.append(row['Genres'].split(','))
    #     elif row['Disney+']:
    #         DisneyGenresTemp_TVShow.append(row['Genres'].split(','))

    # NetflixTVShowGenres = sum(NetflixGenresTemp_TVShow, [])
    # HuluTVShowGenres = sum(HuluGenresTemp_TVShow, [])
    # PrimeTVShowGenres = sum(PrimeGenresTemp_TVShow, [])
    # DisneyTVShowGenres = sum(DisneyGenresTemp_TVShow, [])

    # NetflixTVShowGenresDict = Counter(NetflixTVShowGenres)
    # DictSize = len(NetflixTVShowGenresDict)
    # ExplodeListNetflix_TVShow = [0.1]*DictSize
    # platform_plots.pie_charts(NetflixTVShowGenresDict, "Netflix TV Shows Genres", "NetflixTVShowsGenres.png", ExplodeListNetflix_TVShow)

    # HuluTVShowGenresDict = Counter(HuluTVShowGenres)
    # DictSize = len(HuluTVShowGenresDict)
    # ExplodeListHulu_TVShow = [0.1]*DictSize
    # platform_plots.pie_charts(HuluTVShowGenresDict, "Hulu TV Shows Genres", "HuluTVShowsGenres.png", ExplodeListHulu_TVShow)

    # PrimeTVShowGenresDict = Counter(PrimeTVShowGenres)
    # DictSize = len(PrimeTVShowGenresDict)
    # ExplodeListPrime_TVShow = [0.1]*DictSize
    # platform_plots.pie_charts(PrimeTVShowGenresDict, "Prime Video TV Shows Genres", "PrimeTVShowsGenres.png", ExplodeListPrime_TVShow)

    # DisneyTVShowGenresDict = Counter(DisneyTVShowGenres)
    # DictSize = len(DisneyTVShowGenresDict)
    # ExplodeListDisney_TVShow = [0.1]*DictSize
    # platform_plots.pie_charts(DisneyTVShowGenresDict, "Disney+ TV Shows Genres", "DisneyTVShowsGenres.png", ExplodeListDisney_TVShow)

    return TVshow_data

def TVshow_year(file_name='tv_shows.csv'):
    ''' Plot doughnut plot of tv show languages '''

    import pandas as pd
    from pandas.api.types import CategoricalDtype

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})

    TVshow_data['Decade'] = '' # make column for decade
    for index,row in TVshow_data.iterrows():
        TVshow_data['Decade'][index] = row['Year']//10*10 # calculate decade based on start year and add to decade column

    # make Decade column categorical dtype
    df_out_type = CategoricalDtype(categories=TVshow_data['Decade'].unique(), ordered=True)
    TVshow_data['Decade'] = TVshow_data['Decade'].astype(df_out_type)   

    return TVshow_data

def TVshow_actor(file_name='tv_shows.csv'):
    ''' Add directors and actors columns to TVshow dataframe '''
    import pandas as pd
    
    TVshow_people_info = pd.read_csv('name.basics.csv',dtype={'nconst':object, 'primaryName':str, 'birthYear':object, 'deathYear':object, 'primaryProfession':object, 'knownForTitles':object})
    #TVshow_people_info = TVshow_people_info.set_index('nconst') # set indices to be tconst
    TVshow_people = pd.read_csv('title.principals.csv',dtype={'tconst':object, 'ordering':int, 'nconst':object, 'category':object, 'job':object, 'characters':object})
    TVshow_id_dict, TVshow_IMDB_clean, TVshow_data = TVshow_IMDB_clean_data(file_name)

    TVshow_actors_clean = TVshow_people[TVshow_people['tconst'].isin(TVshow_IMDB_clean.index)] # only include people who are known for TV shows in TV show id number dictionary
    TVshow_actors_clean = TVshow_actors_clean[TVshow_actors_clean['category'].notna()] # remove people who's profession is unknown
    TVshow_actors_clean = TVshow_actors_clean.set_index('tconst') # set indices to tvshow id number
    TVshow_actors = TVshow_actors_clean[TVshow_actors_clean['category'].isin(['actor','actress'])]

    # generate dictionary of people id number and name
    TVshow_people_info = TVshow_people_info[TVshow_people_info['primaryProfession'].isin(['actor','actress'])]
    people_id_dict = pd.Series(TVshow_people_info.primaryName,index=TVshow_people_info.index).to_dict() 

    TVshow_actors['TVshowTitle'] = '' # make column for TVshow title
    TVshow_actors['ActorName'] = '' # make column for actor/actress name
    for index,row in TVshow_actors.iterrows():
        id_num = index # get id number from dictionary
        name_id_num = row['nconst'] # get name id number 
        TVshow_actors['TVshowTitle'][index] = TVshow_IMDB_clean.loc[id_num,'primaryTitle'] # put TV show title in TVshowTitle column
        TVshow_actors['ActorName'][index] = people_id_dict[name_id_num] # put actor name in ActorName column
    return TVshow_actors

if __name__ == '__main__':
    print(TVshow_actor(file_name='tv_shows.csv'))