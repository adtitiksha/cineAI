import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

final_data = pd.read_csv("/Users/titiksha/dev/CineAI/movie_data_limited_reviews.csv")

# Pivot the data to create a user-movie matrix
user_movie_matrix = final_data.pivot_table(
    index="username", columns="movie_name", values="overall_ratings"
)

# Fill missing values with 0 (assuming unrated movies are 0)
user_movie_matrix = user_movie_matrix.fillna(0)

# Compute the cosine similarity between movies
movie_similarity = cosine_similarity(user_movie_matrix.T)

# Convert the similarity matrix to a DataFrame
movie_similarity_df = pd.DataFrame(
    movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns
)

# Display similarity between two movies
print(movie_similarity_df[["Inception", "Titanic"]].head())
