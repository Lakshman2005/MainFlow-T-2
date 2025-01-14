# -*- coding: utf-8 -*-
"""Task-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BOlN0BXyYb-Tiae1zOgMt-qucMxzKxkO
"""

import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('01.Data Cleaning and Preprocessing.csv')

# Explore the DataFrame
print(df.head())

# Get the shape of the DataFrame (number of rows and columns)
print(df.shape)

# Get the data types of each column
print(df.dtypes)

# Get a summary of the DataFrame
print(df.info())

# Handle missing values
# Check for missing values in the DataFrame
print(df.isnull().sum())

# Check for missing values
missing_values = df.isnull().sum()

df_cleaned = df.drop(columns=['AAWhiteSt-4 ', 'SulphidityL-4 '])

# Handle only numeric columns for filling missing values
numeric_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].mean())

# Filter rows where Y-Kappa is greater than 25
filtered_df = df_cleaned[df_cleaned['Y-Kappa'] > 25]

# Calculate summary statistics for numerical columns
summary_statistics = filtered_df.describe()

print("Summary statistics:\n", summary_statistics)

