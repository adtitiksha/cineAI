import os
import re

import pandas as pd


def extract_name_number(filepath):
    """
    Extracts the movie name and year from a file path string.

    Args:
      filepath: The file path string.

    Returns:
      A tuple containing the movie name and year, or None if the pattern is not found.
    """
    match = re.search(r"^(.*?) (\d{4})\.csv$", filepath)
    if match:
        return match.group(1), int(match.group(2))
    return None


# Path to the directory containing the movie reviews CSV files
reviews_directory = "/Users/titiksha/Downloads/dataset/reviews_per_movie_raw"
# Path to the movie information CSV file
movies_info_file = "/Users/titiksha/dev/CineAI/merged_output.csv"

# Load the movie information CSV (e.g., movie title, genre, director)
movies_info = pd.read_csv(movies_info_file)

# List to hold DataFrames of the movie reviews
reviews_dataframes = []

# Loop through all the movie reviews CSV files in the directory
for filename in os.listdir(reviews_directory):
    if filename.endswith(".csv"):  # Only process CSV files
        file_path = os.path.join(reviews_directory, filename)

        # Read the review CSV
        review_df = pd.read_csv(file_path)

        # Extract movie name and year from the file name
        result = extract_name_number(filename)
        name, year = result

        print(year)
        print(name)
        # Add 'name' and 'year' columns
        review_df["name"] = name
        review_df["year"] = int(year)
