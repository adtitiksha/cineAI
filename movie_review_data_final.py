import numpy as np
import pandas as pd
from scipy import stats

final_data = pd.read_csv("/Users/titiksha/dev/CineAI/movie_data_sentiment_analysis.csv")

final_data = final_data.drop("review_url", axis=1)
final_data = final_data.rename(columns={"name": "movie_name", "title": "review_title"})
final_data["user_rating"] = pd.to_numeric(final_data["user_rating"], errors="coerce")
final_data["overall_ratings"] = pd.to_numeric(
    final_data["overall_ratings"], errors="coerce"
)
final_data = final_data.dropna()

print(final_data.info())


# Group by movie_name


aggregated_data = (
    final_data.groupby("movie_name")
    .agg(
        user_rating_mean=("user_rating", "mean"),
        overall_ratings=("overall_ratings", "first"),
        sentiment_score_mean=("sentiment_score", "mean"),
        sentiment_score_median=("sentiment_score", "median"),
        sentiment_score_mode=(
            "sentiment_score",
            lambda x: x.mode().iloc[0] if not x.mode().empty else None,
        ),
        year=("year", "first"),
        genre=("Genre", "first"),
    )
    .reset_index()
)

print(aggregated_data.head())
aggregated_data.to_csv("final_movie_data_reviews.csv", index=False)
