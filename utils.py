import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

base = "data/"

data = pd.read_csv(base + "movies_metadata.csv", low_memory=False).head(20000)

def get_cosine_similarity():
    try:
        cosine_sim = np.load(base + "movies_processed.npy")

    except IOError:
        data['overview'] = data['overview'].fillna('')
        tfidf = TfidfVectorizer(stop_words="english")
        tfidf_marix = tfidf.fit_transform(data['overview'])

        cosine_sim = linear_kernel(tfidf_marix, tfidf_marix)
        np.save(base + "movies_processed.npy",cosine_sim)

    return cosine_sim

def recommend_me_similar_to(title, method):
    indices = pd.Series(data.index, index=data['title']).drop_duplicates()
    index = indices[title]
    sim_scores = list(enumerate(method[index]))
    sim_scores = sorted(sim_scores, key=lambda x : x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    result = data['title'].iloc[movie_indices].values

    return result
