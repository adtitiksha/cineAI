from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import plotly.express as px
import pygwalker as pyg
import seaborn as sns
import swifter
from loguru import logger
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
from tqdm import tqdm
from wordcloud import WordCloud

nltk.download("vader_lexicon")

logger.debug("Initialize SentimentIntensityAnalyzer")
sia = SentimentIntensityAnalyzer()


# Function to get sentiment polarity score
def get_sentiment(text):
    return sia.polarity_scores(text)["compound"]


logger.debug("Read the cleaned movie data")
final_data = pd.read_csv("/Users/titiksha/dev/CineAI/movie_data_text_processing.csv")
print(final_data.info())


# Apply sentiment analysis on cleaned reviews
logger.debug("Apply sentiment analysis on cleaned reviews")
final_data["sentiment_score"] = final_data["cleaned_review"].swifter.apply(
    get_sentiment
)

# Display the sentiment scores
logger.debug("Save the sentiment scores")
# print(final_data[["review", "sentiment_score"]].head())
final_data.to_csv("movie_data_sentiment_analysis.csv", index=False)

final_data = final_data.drop("review_url", axis=1)
final_data = final_data.rename(columns={"name": "movie_name", "title": "review_title"})
print(final_data.info())


# walker = pyg.walk(final_data)
logger.debug("Write to HTML")
with open("pygwalker_demo.html", "w", encoding="utf-8") as f:
    f.write(pyg.to_html(final_data))
# walker

# Plot the distribution of ratings
# plt.figure(figsize=(10, 6))
# sns.histplot(final_data["overall_ratings"], kde=True, bins=20, color="blue")
# plt.title("Distribution of Movie Ratings")
# plt.xlabel("Rating")
# plt.ylabel("Frequency")
# plt.show()

# # Plot the distribution of sentiment scores
# plt.figure(figsize=(10, 6))
# sns.histplot(final_data["sentiment_score"], kde=True, bins=20, color="red")
# plt.title("Distribution of Sentiment Scores")
# plt.xlabel("Sentiment Score")
# plt.ylabel("Frequency")
# plt.show()
