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
movie_metadata = pd.read_csv("/Users/titiksha/dev/CineAI/merged_output.csv")

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

        # Add 'name' and 'year' columns
        review_df["name"] = name
        review_df["year"] = int(year)

        # Append the review DataFrame to the list
        reviews_dataframes.append(review_df)

# Combine all review DataFrames into one large DataFrame
reviews_combined = pd.concat(reviews_dataframes, ignore_index=True)

# Display the first few rows of the combined reviews DataFrame
# print(reviews_combined.head())

# Merge the reviews data with the movie metadata based on 'name' and 'year'
final_data = pd.merge(
    reviews_combined, movie_metadata, how="inner", on=["name", "year"]
)

# Display the first few rows of the merged data
# print(final_data.head())

# Fill missing values with a default value, or drop rows with missing values
final_data = final_data.fillna("Unknown")


final_data.rename(
    columns={"rating_x": "user_rating", "rating_y": "overall_ratings"}, inplace=True
)

final_data.to_csv("movie_data.csv", index=False)
