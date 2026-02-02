import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Spam Email Detection(1) (1).xlsx - spam.csv')

# --- 1. Handling missing values ---
# The dataset contained 3 unnamed columns that were mostly empty (NaN).
df = df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
df.columns = ['target', 'text']
# Check for nulls in the main columns
print(f"Missing values:\n{df.isnull().sum()}")

# --- 2. Fixing wrong data types or formats ---
df['text'] = df['text'].astype(str)
df['target'] = df['target'].astype(str)

# --- 3. Detecting and treating outliers ---
# Using message length as the metric for outliers
df['message_len'] = df['text'].apply(len)
Q1 = df['message_len'].quantile(0.25)
Q3 = df['message_len'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

# Capping outliers (messages longer than the upper bound)
outliers_count = df[df['message_len'] > upper_bound].shape[0]
df['message_len'] = np.where(df['message_len'] > upper_bound, upper_bound, df['message_len'])

# --- 4. Removing duplicate records ---
initial_count = len(df)
df = df.drop_duplicates(subset=['text'])
print(f"Duplicates removed: {initial_count - len(df)}")

# --- 5. Handling categorical variables (encoding) ---
# Map 'ham' to 0 and 'spam' to 1 for machine learning compatibility
df['target_encoded'] = df['target'].map({'ham': 0, 'spam': 1})

print("\n--- Final Cleaned Data Preview ---")
print(df.head())