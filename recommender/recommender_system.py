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

import warnings; warnings.simplefilter('ignore')


def get_data():

	streaming_platform_info = pd.read_csv("../MoviesOnStreamingPlatforms_updated.csv")
	md = pd. read_csv('data/movies_metadata.csv')
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