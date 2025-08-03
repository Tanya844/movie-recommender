import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(user_id):
    # Load data
    ratings = pd.read_csv("ratings.csv")

    # Create user-movie matrix
    user_movie = ratings.pivot_table(index='userId', columns='movie', values='rating').fillna(0)

    # Calculate similarity between users
    user_sim = cosine_similarity(user_movie)
    sim_df = pd.DataFrame(user_sim, index=user_movie.index, columns=user_movie.index)

    if user_id not in user_movie.index:
        return []

    similar_users = sim_df[user_id].drop(user_id).sort_values(ascending=False)
    movie_scores = pd.Series(dtype='float64')

    for other_user in similar_users.index:
        other_ratings = user_movie.loc[other_user]
        unseen = user_movie.loc[user_id] == 0
        unseen_ratings = other_ratings[unseen]
        movie_scores = movie_scores.add(unseen_ratings, fill_value=0)

    top_movies = movie_scores.sort_values(ascending=False).head(3)
    return top_movies.to_dict()
