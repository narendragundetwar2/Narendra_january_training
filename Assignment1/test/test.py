import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# Load dataset
df = pd.read_csv("synthetic_customer_churn_100k.csv")


# DATA CLEANING & PREPARATION

# Handling missing values
df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)

# Fixing incorrect data types
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Detecting & treating outliers (IQR method)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Removing duplicate records
df.drop_duplicates(inplace=True)

# Dropping irrelevant features
df.drop(columns=["customerID"], inplace=True, errors="ignore")

# CATEGORICAL VARIABLE HANDLING


# One-Hot Encoding
df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

# Label Encoding
le = LabelEncoder()
df["Churn"] = le.fit_transform(df["Churn"])

# Ordinal Encoding
oe = OrdinalEncoder()
df[["Contract"]] = oe.fit_transform(df[["Contract"]])

# Frequency Encoding
df["PaymentMethod"] = df["PaymentMethod"].map(
    df["PaymentMethod"].value_counts()
)

# Target Encoding
df["InternetService"] = df.groupby("InternetService")["Churn"].mean()

# Final output
print(df.head())
print("Preprocessing completed successfully")





