import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD

import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

import warnings; warnings.simplefilter('ignore')


def get_data(root_dir = "/"):

	streaming_platform_info = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
	md = pd. read_csv('recommender/data/movies_metadata.csv')
	md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
	md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

	md = md.drop([19730, 29503, 35587])
	smd = md[md['title'].isin(streaming_platform_info['Title'])]

	smd['tagline'] = smd['tagline'].fillna('')
	smd['description'] = smd['overview'] + smd['tagline']
	smd['description'] = smd['description'].fillna('')

	tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
	tfidf_matrix = tf.fit_transform(smd['description'])

	cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

	smd = smd.reset_index()
	titles = smd['title']
	indices = pd.Series(smd.index, index=smd['title'])

	return indices, cosine_sim, titles

def get_recommendations(title, indices, cosine_sim, titles):
    idx = indices[title]
    if not isinstance(idx, np.int64): idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return list(titles.iloc[movie_indices]), [s[1] for s in sim_scores]


def get_tv_data():

	smd = pd.read_csv("data/tv_plot.csv")

	smd['description'] = smd['Plot']
	smd['description'] = smd['Plot'].fillna('')

	tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
	tfidf_matrix = tf.fit_transform(smd['Plot'])

	cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

	smd = smd.reset_index()
	titles = smd['Title']
	indices = pd.Series(smd.index, index=smd['Title'])

	return indices, cosine_sim, titles

def compute_one_hot_genres(g, genres):
    if not isinstance(g, str):
        return np.zeros(len(genres))
    else:
        vec = np.zeros(len(genres))
        for item in g.split(','):
            vec[genres.index(item)] = 1
        return vec

def compute_plat_feature(name, dic, genres):
    df = dic[name]
    feature = np.zeros(len(genres))
    for item in df["Genres"]:
        feature += compute_one_hot_genres(item, genres)
    #for i, key in enumerate(genres):
        #feature[i] /= (genre_count[key]+1)
        #feature[i] *= 100
    feature = feature / np.max(feature) * 100
    feature = np.sqrt(feature) * 10
    return feature


def compute_plat_score(name, dic):
    df = dic[name]
    score = {}
    score["IMDb"] = np.mean(df["IMDb"].dropna())
    score["RT"] = np.mean(df["Rotten Tomatoes"].dropna().transform(lambda x:float((x[:-1]))))
    return score

def generate_genre_radar_plot(streaming_platform_info, plat_dic):
    genres = set()
    for g in streaming_platform_info["Genres"]:
        if isinstance(g, str):
            genres = genres.union(set(g.split(',')))
    genres = list(genres)

    # count # of movies in each genres
    genre_count = {}
    for key in genres:
        count = 0
        for item in streaming_platform_info["Genres"]:
            if isinstance(item, str):
                if key in item:
                    count += 1
        genre_count[key] = count

    #plat_dic = {"Netflix": netflix_df, "Hulu": hulu_df, "Prime": prime_df, "Disney": disney_df}
    plat_feature = {}
    for key in plat_dic.keys():
        plat_feature[key] = compute_plat_feature(key, plat_dic, genres)
        
    color_palette = ['rgb(212, 107, 99)', 'rgb(76, 224, 99)', 'rgb(67, 207, 232)', 'rgb(160, 73, 227)']

    for index, key in enumerate(plat_feature.keys()):
        """
        df = pd.DataFrame(dict(
            rating=plat_feature[key],
            genre=genres))
        fig = px.line_polar(df, r='rating', theta='genre', line_close=True, title=key)
        fig.show()
        """

        fig = go.Figure(data=go.Scatterpolar(
          r=plat_feature[key],
          theta=genres,
          fill='toself',
          line = {"color" : color_palette[index]},
        ))

        fig.update_layout(
            title=key,
            polar=dict(
            radialaxis=dict(
            visible=True
            ),
          ),
          showlegend=False,
          #plot_bgcolor='rgb(179,75,34)',
          plot_bgcolor='#f5e7b7',
        )

        fig.update_layout(
            paper_bgcolor='#f5e7b7',
            plot_bgcolor='#f5e7b7',
        )
        fig.show()


def generate_global_variable(streaming_platform_info, titles):
    movie_set = set(streaming_platform_info["Title"])
    recommender_set = set(titles)
    movie_set_buffer = recommender_set.intersection(movie_set)

    # construct movie title - platform dictionary
    TITLE_PLAT_MAP = {}
    for index, row in streaming_platform_info.iterrows():
        if row["Netflix"] == 1: TITLE_PLAT_MAP[row["Title"]] = "Netflix" 
        if row["Hulu"] == 1: TITLE_PLAT_MAP[row["Title"]] = "Hulu" 
        if row["Prime Video"] == 1: TITLE_PLAT_MAP[row["Title"]] = "Prime Video" 
        if row["Disney+"] == 1: TITLE_PLAT_MAP[row["Title"]] = "Disney+" 

    MOVIE_GENRE_MAP = {}
    for index, row in streaming_platform_info.iterrows():
        if row["Title"] in movie_set_buffer:
            if isinstance(row['Genres'], str):
                MOVIE_GENRE_MAP[row["Title"]] = row['Genres'].split(',')


    GENRE_COUNT = defaultdict(int)
    TOTAL_GENRE = 0
    for index, row in streaming_platform_info.iterrows():
        if row["Title"] in movie_set_buffer:
            if isinstance(row['Genres'], str):
                for g in row['Genres'].split(','):
                    GENRE_COUNT[g] += 1
                    TOTAL_GENRE += 1
    for g in GENRE_COUNT:
        GENRE_COUNT[g] /= TOTAL_GENRE
        
    return TITLE_PLAT_MAP, MOVIE_GENRE_MAP, GENRE_COUNT
    

def platform_recommender(list_of_watched, indices, cosine_sim, titles):
    recommended_movies = []
    rec_movie_scores = []
    plat_count = defaultdict(int)
    plat_score = defaultdict(int)
    for movie in list_of_watched:
        rec_movie_list, score = get_recommendations(movie, indices, cosine_sim, titles)
        recommended_movies += rec_movie_list
        rec_movie_scores += score
    for i, movie in enumerate(recommended_movies):
        plat = TITLE_PLAT_MAP[movie]
        plat_score[plat] += rec_movie_scores[i]
        plat_count[plat] += 1
    for plat in plat_score:
        plat_score[plat] /= plat_count[plat]
    return plat_score

def generate_portforlio_contents(list_of_watched, streaming_platform_info):
    # preprocess the movie data
    indices, cosine_sim, titles = get_data()
    
    TITLE_PLAT_MAP, MOVIE_GENRE_MAP, GENRE_COUNT = generate_global_variable(streaming_platform_info, titles)
    
    recommended_movies = []
    rec_movie_scores = []
    genres = []

    genre_count = defaultdict(int)
    plat_count = defaultdict(int)
    plat_score = defaultdict(int)
    plat_movie_dict = defaultdict(list)

    #list to create dataframe
    plat_df = []
    score_df = []
    genre_df = []
    title_df = []

    for movie in list_of_watched:
        rec_movie_list, score = get_recommendations(movie, indices, cosine_sim, titles)
        recommended_movies += rec_movie_list
        rec_movie_scores += score
    for i, movie in enumerate(recommended_movies):
        if movie in MOVIE_GENRE_MAP:
            for g in MOVIE_GENRE_MAP[movie]:
                genre_count[g] += rec_movie_scores[i]

        plat = TITLE_PLAT_MAP[movie]
        plat_movie_dict[plat].append(movie)
        plat_score[plat] += rec_movie_scores[i]
        plat_count[plat] += 1

        plat_df.append(plat)
        score_df.append(rec_movie_scores[i])
        if movie in MOVIE_GENRE_MAP:
            genre_df.append(MOVIE_GENRE_MAP[movie][0])
        else:
            genre_df.append("Action")
        if len(movie) > 20:
            title_df.append(movie[:20] + "...")
        else:
            title_df.append(movie)

    recommended_move_df = pd.DataFrame(data = {"Title": title_df, 
                                               "Platform": plat_df, "Score":score_df,
                                              "Genre": genre_df})

    max_score = 0
    for plat in plat_score:
        plat_score[plat] /= plat_count[plat]
        max_score = max(plat_score[plat], max_score)
    for plat in plat_score:
        plat_score[plat] /= max_score
        plat_score[plat] *= 100
    
    for g in genre_count:
        genre_count[g] /= GENRE_COUNT[g]
    del genre_count["Short"]
    del genre_count["Western"]
    
    return genre_count, plat_count, plat_score, recommended_move_df

def personal_preference_radar(genre_count):
    fig = go.Figure(data=go.Scatterpolar(
      r=list(genre_count.values()),
      theta=list(genre_count.keys()),
      fill='toself',
      line = {"color" : 'rgb(245, 200, 66)'},
    ))

    fig.update_layout(
        title='Personal Movie Portfolio',
        polar=dict(
        radialaxis=dict(
        visible=True
        ),
      ),
      showlegend=False,
      plot_bgcolor='rgb(179,75,34)',
    )

    fig.update_layout(
        paper_bgcolor='#f5e7b7',
        plot_bgcolor='#f5e7b7',
    )

    fig.show()

def generate_plat_recommendation_plot(plat_count, plat_score):
    fig = go.Figure(data=go.Scatter(
    x=list(plat_count.keys()),
    y=list(plat_score.values()),
    mode='markers',
    marker=dict(size=np.sqrt(np.array(list(plat_count.values())))*15,
                #color=np.sqrt(np.array(list(plat_count.values())))*15
               color = ['rgb(212, 107, 99)', 'rgb(67, 207, 232)', 'rgb(76, 224, 99)', 'rgb(160, 73, 227)']),
    #marker_colorscale=px.colors.sequential.Oryel
    #color = ['rgb(212, 107, 99)', 'rgb(76, 224, 99)', 'rgb(67, 207, 232)', 'rgb(160, 73, 227)']
    ))

    fig.update_layout(
        title='Streaming Platform Recommendation',
        xaxis=dict(
            title='Platform',
            gridcolor='white',
        ),
        yaxis=dict(
            title='Recommendation Score',
            gridcolor='white',
        ),
        paper_bgcolor='#f5e7b7',
        plot_bgcolor='#f5e7b7',
    )

    fig.show()

def generate_platwise_movie_recommendation(recommended_move_df):
    for plat in ["Netflix", "Prime Video", "Hulu", "Disney+"]:
        df = recommended_move_df
        df = df.loc[df['Platform'] == plat]
        fig = px.sunburst(df, path=['Genre', 'Title'], values='Score',
                          color='Score', 
                          color_continuous_scale='fall',
                          color_continuous_midpoint=np.average(df['Score'], weights=df['Score']))
        fig.update_layout(
        title = plat,
        paper_bgcolor='#f5e7b7',
        plot_bgcolor='#f5e7b7',
        )
        fig.show()