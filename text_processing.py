import string

import nltk
import pandas as pd
import swifter
from loguru import logger
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from tqdm import tqdm

tqdm.pandas(desc="my bar!")


# Download NLTK resources
logger.debug("Download NLTK resources")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Intialize lemmatizer and stopwords
logger.debug("Initialize lemmatizer and stopwords")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


final_data = pd.read_csv("/Users/titiksha/dev/CineAI/movie_data.csv")
print(final_data.info())


# Function to preprocess the review text
def preprocess_review(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())

    # Remove punctuation and stopwords
    tokens = [
        word
        for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]

    # Lemmatize each token
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into a string
    return " ".join(tokens)


# Apply the preprocessing function to the 'review' column
logger.debug("Apply the preprocessing function to the 'review' column")
# final_data["cleaned_review"] = final_data["review"].progress_apply(preprocess_review)
final_data["cleaned_review"] = final_data["review"].swifter.apply(preprocess_review)


# Display the cleaned reviews
logger.debug("Display the cleaned reviews")
print(final_data[["review", "cleaned_review"]].head())


final_data.to_csv("movie_data_text_processing.csv", index=False)
