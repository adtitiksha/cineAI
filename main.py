import os

import pandas as pd

# Path to the directory containing the CSV files
csv_directory = "/Users/titiksha/Downloads/dataset/movies_per_genre"

# List to hold DataFrames
dataframes = []

# Loop through all CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):  # Make sure we only read CSV files
        file_path = os.path.join(csv_directory, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Add a new column for the filename (without extension)
        df["Genre"] = os.path.splitext(filename)[0]

        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dataframes, ignore_index=True)

# Show the result (first few rows)
print(final_df.head())

# Optionally, save the concatenated DataFrame to a new CSV file
final_df.to_csv("merged_output.csv", index=False)

movie_df = pd.read_csv("/Users/titiksha/dev/CineAI/merged_output.csv")
