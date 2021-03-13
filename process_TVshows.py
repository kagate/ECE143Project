''' 
    This file contains functions which save a csv file (tv_shows.csv) with an added column under a new file name:

    add_TVshow_decade outputs TV_shows_decade.csv --> original TV show csv with added decade column
    add_TVshow_actor outputs TV_shows_actors.csv --> original TV show csv with added actors column (each entry has list of actors)
    add_TVshow_producer outputs TV_shows_producers.csv --> original TV show csv with added producers column (each entry has list of executive producers)
    add_TVshow_genre outputs TV_shows_genres.csv --> original TV show csv with added genres column (each entry has list of genres)
    add_TVshow_language outputs TV_shows_languages.csv --> original TV show csv with added language column
    consolidated_TVshow_data outputs TV_shows_all_features.csv --> original tv_shows.csv with all new columns generated in above functions
'''
def add_TVshow_decade(file_name='tv_shows.csv'):
    ''' 
    Plot doughnut plot of tv show languages 
    
    :param file_name: name of input csv file
    :type file_name: str
    '''

    import pandas as pd
    from pandas.api.types import CategoricalDtype
    
    assert isinstance(file_name,str)
    
    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})

    TVshow_data['Decade'] = ''                                          # make column for decade
    for index,row in TVshow_data.iterrows():                            # for every show in TVshow_data
        TVshow_data['Decade'][index] = row['Year']//10*10               # calculate decade based on start year and add to decade column

    TVshow_data.to_csv(r'TV_shows_decade.csv',index=False)              # save final dataframe to csv file

    return TVshow_data

def add_TVshow_actor(file_name='tv_shows.csv'):
    ''' 
    Add directors and actors columns to TVshow dataframe 
    
    :param file_name: name of input csv file
    :type file_name: str
    '''
    import pandas as pd
    from tvmaze.api import Api                                          # import TV show API with TV show attributes
    
    assert isinstance(file_name,str)

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    api = Api()

    TVshow_data['Actors'] = ''                                          # make column for actors
    for index,row in TVshow_data.iterrows():                            # for every show in TVshow_data
        new_show = []                                                   
        show_name = row[0]                                              # extract show title
        try:
            new_show.append(api.search.single_show(show_name))          # search for the show title in api
        except:
            new_show = []                                               # if an error is raised, return an empty array
        if not new_show == [] and new_show[0].name == show_name:        # if a show was found with that title and the titles match exactly
            id_num = api.search.single_show(show_name).id               # get the show id number in the api
            actors = []
            for actor in range(len(api.show.cast(id_num))):             # for all actors in the cast list
                actor_name = api.show.cast(id_num)[actor].person.name   # get their name from their id number
                actors.append(actor_name)                               # append name to output actor list
            TVshow_data['Actors'][index] = actors                       # put output actor list in Actors column for this show
        else:
            TVshow_data['Actors'][index] = []                           # if no show is found, put an empty list in Actors column for this show
    TVshow_data.to_csv(r'TV_shows_actors.csv',index=False)              # save final dataframe to csv file

    return TVshow_data

def add_TVshow_producer(file_name='tv_shows.csv'):
    '''
    This function extracts TV show producers from the TvMaze API
    
    :param file_name: name of input csv file
    :type file_name: str
    '''
    
    import pandas as pd
    from tvmaze.api import Api # import TV show API with TV show attributes
    
    assert isinstance(file_name,str)

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    api = Api()

    TVshow_data['Producers'] = ''                                       # make column for producers
    for index,row in TVshow_data.iterrows():                            # for every show in TVshow_data
        new_show = []
        show_name = row[0]                                              # extract show title
        try:
            new_show.append(api.search.single_show(show_name))          # search for the show title in api
        except:
            new_show = []                                               # if an error is raised, return an empty array
        if not new_show == [] and new_show[0].name == show_name:        # if a show was found with that title and the titles match exactly
            id_num = api.search.single_show(show_name).id               # get the show id number in the api
            crew_members = []
            for crew_member in range(len(api.show.crew(id_num))):       # for all people in the crew list
                crew_role = api.show.crew(id_num)[crew_member].type     # get the role of each person in the crew
                if crew_role in ['Executive Producer','Co-Executive Producer']: # if their role is executive producer
                    crew_members.append(api.show.crew(id_num)[crew_member].person.name) # append their name to the output producer list
            TVshow_data['Producers'][index] = crew_members              # put output producer list in Producers column for this show
            print(crew_members)
        else:
            TVshow_data['Producers'][index] = []                        # if no show is found, put an empty list in Producers column for this show
    TVshow_data.to_csv(r'TV_shows_producers.csv',index=False)           # save final dataframe to csv file

    return TVshow_data

def add_TVshow_genre(file_name='tv_shows.csv'):
    '''
    This function extracts genres from the TvMaze API and adds it to the input csv file.
    
    :param file_name: name of input csv file
    :type file_name: str
    '''
    
    import pandas as pd
    from tvmaze.api import Api
    
    assert isinstance(file_name,str)

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    api = Api()

    TVshow_data['Genres'] = ''                                          # make column for genres
    for index,row in TVshow_data.iterrows():                            # for every show in TVshow_data
        new_show = []
        show_name = row[0]                                              # extract show title
        try:
            new_show.append(api.search.single_show(show_name))          # search for the show title in api
        except:
            new_show = []                                               # if an error is raised, return an empty array
        if not new_show == [] and new_show[0].name == show_name:        # if a show was found with that title and the titles match exactly
            TVshow_data['Genres'][index] = new_show[0].genres           # add the genres list to the Genres column for that show
        else:
            TVshow_data['Genres'][index] = []                           # if no show is found, put an empty list in Genres column for this show
    TVshow_data.to_csv(r'TV_shows_genres.csv',index=False)              # save final dataframe to csv file

    return TVshow_data

def add_TVshow_language(file_name='tv_shows.csv'):
    '''
    This function extracts languages for TV shows from the TvMaze API and adds it to the data in the input csv file.
    
    :param file_name: name of input csv file
    :type file_name: str
    '''
    
    import pandas as pd
    from tvmaze.api import Api
    
    assert isinstance(file_name,str)

    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    api = Api()

    TVshow_data['Language'] = ''                                        # make column for languages
    for index,row in TVshow_data.iterrows():                            # for every show in TVshow_data
        new_show = []
        show_name = row[0]                                              # extract show title
        try:
            new_show.append(api.search.single_show(show_name))          # search for the show title in api
        except:
            new_show = []                                               # if an error is raised, return an empty array
        if not new_show == [] and new_show[0].name == show_name:        # if a show was found with that title and the titles match exactly
            TVshow_data['Language'][index] = new_show[0].language       # add the language to the Language column for that show
        else:
            TVshow_data['Language'][index] = []                         # if no show is found, put an empty list in Language column for this show
    TVshow_data.to_csv(r'TV_shows_languages.csv',index=False)           # save final dataframe to csv file

    return TVshow_data

def consolidated_TVshow_data(file_name='tv_shows.csv'):
    '''
    This function takes the extracted data from the previous functions and consolidates them into 1 output csv file containing all of the TV shows in the input csv file.
    
    :param file_name: name of input csv file
    :type file_name: str
    '''
    import pandas as pd
    
    assert isinstance(file_name,str)

    # import all modified csv's from functions above
    TVshow_data = pd.read_csv(file_name,index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool})
    TVshow_data_decade = pd.read_csv('TV_shows_decade.csv',index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool, 'Decade':object})
    TVshow_data_actors = pd.read_csv('TV_shows_actors.csv',index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool, 'Actors':object})
    TVshow_data_producers = pd.read_csv('TV_shows_producers.csv',index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool, 'Producers':object})
    TVshow_data_genres = pd.read_csv('TV_shows_genres.csv',index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool, 'Genres':object})
    TVshow_data_languages = pd.read_csv('TV_shows_languages.csv',index_col=0,dtype={'Title': str, 'Year': int, 'Age': object, 'IMDb':float, 'Rotten Tomatoes':object, 'Netflix':bool, 'Hulu':bool, 'Prime Video':bool, 'Disney+':bool, 'type':bool, 'Language':object})

    
    # append every new column in each of the above csv's to the original TVshow_data csv
    TVshow_data['Decade'] = ''
    TVshow_data['Actors'] = ''
    TVshow_data['Producers'] = ''
    TVshow_data['Genres'] = ''
    TVshow_data['Language'] = ''

    for index,row in TVshow_data.iterrows():
        TVshow_data['Decade'][index] = TVshow_data_decade['Decade'][index]
    for index,row in TVshow_data.iterrows():
        TVshow_data['Actors'][index] = TVshow_data_actors['Actors'][index]
    for index,row in TVshow_data.iterrows():
        TVshow_data['Producers'][index] = TVshow_data_producers['Producers'][index]
    for index,row in TVshow_data.iterrows():
        TVshow_data['Genres'][index] = TVshow_data_genres['Genres'][index]
    for index,row in TVshow_data.iterrows():
        TVshow_data['Language'][index] = TVshow_data_languages['Language'][index]

    # save final dataframe to csv file
    TVshow_data.to_csv(r'TV_shows_all_features.csv',index=False)           
