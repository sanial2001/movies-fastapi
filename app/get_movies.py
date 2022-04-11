from .ML import movies_coupon
import pickle
import pandas as pd

pickle_in = open("knn.pkl", "rb")
knn = pickle.load(pickle_in)


def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies_coupon.movies[movies_coupon.movies['title'].str.contains(movie_name)]
    # print(movie_list)
    if len(movie_list):
        movie_idx = movie_list.iloc[0]['movieId']
        # print(movies_coupon.final_dataset[movies_coupon.final_dataset['movieId'] == movie_idx].size)
        try:
            movie_idx = movies_coupon.final_dataset[movies_coupon.final_dataset['movieId'] == movie_idx].index[0]
            distances, indices = knn.kneighbors(movies_coupon.csr_data[movie_idx],
                                                n_neighbors=n_movies_to_reccomend + 1)
            rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())),
                                       key=lambda x: x[1])[:0:-1]
            recommend_frame = []
            for val in rec_movie_indices:
                movie_idx = movies_coupon.final_dataset.iloc[val[0]]['movieId']
                idx = movies_coupon.movies[movies_coupon.movies['movieId'] == movie_idx].index
                recommend_frame.append({'Title': movies_coupon.movies.iloc[idx]['title'].values[0], 'Distance': val[1]})
            df = pd.DataFrame(recommend_frame, index=range(1, n_movies_to_reccomend + 1))
            return df
        except:
            return pd.DataFrame
    else:
        return pd.DataFrame
