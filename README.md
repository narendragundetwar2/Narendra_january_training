Spam Message Detection and Classification Project Report

1. Project Title
Spam Message Detection and Classification using Machine Learning

2. Objective
The primary objective of this project is to build a robust machine learning model capable of accurately classifying messages as either "Ham" (legitimate) or "Spam". By leveraging Natural Language Processing (NLP) techniques, the system aims to automate the filtering process to enhance communication security and user experience.

3. Problem Statement
The rapid increase in digital communication has led to an explosion of unsolicited "spam" messages. These messages often contain promotional content, phishing links, or malware. Manually identifying and deleting these messages is time-consuming and prone to human error. There is a need for an automated system that can analyze the textual content of a message and predict its category with high precision.

4. Dataset Description
The project utilizes a collection of SMS messages tagged as ham or spam.
Source File: Spam Email Detection(1) (1).xlsx - spam.csv
Initial Size: 5,572 records and 5 columns.
Key Columns:
v1 (Target): Label of the message (ham/spam).
v2 (Text): The actual content of the message.
Unnamed columns (2, 3, 4): Redundant columns containing mostly null values.
Cleaned Dataset: cleaned_spam_data.csv (5,163 records).

5. Data Preprocessing Steps (Mandatory)
Based on the Spam_Cleaning_Output.pdf, the following steps were performed:
Column Cleanup: Dropped unnecessary 'Unnamed' columns to streamline the dataset.
Missing Value Handling: Verified that there were no missing values in the critical target and text columns.
Duplicate Removal: Identified and removed 409 duplicate entries, reducing the dataset from 5,572 to 5,163 unique records to prevent model bias.
Outlier Treatment: - Analyzed the message_len (number of characters).
Detected 68 extreme outliers using the Interquartile Range (IQR) method.
Capping: Message lengths were capped at 250 characters to ensure consistency.
Label Encoding: Converted the categorical target variable into a numerical format:
ham → 0
spam → 1
Text Vectorization: Used TF-IDF (Term Frequency-Inverse Document Frequency) to convert text data into numerical features for the machine learning models.

6. Algorithms Implemented
Three different classification algorithms were implemented and compared:
Multinomial Naive Bayes: A probabilistic learning algorithm widely used for text classification.
Logistic Regression: A statistical model used for binary classification.
Random Forest Classifier: An ensemble learning method that uses multiple decision trees for higher accuracy.

7. Evaluation Metrics
To assess the models, the following metrics were used:
Accuracy: The percentage of total correct predictions.
Precision: The ability of the classifier not to label a legitimate message as spam (Crucial for avoiding "False Positives").
Recall: The ability of the classifier to find all the spam messages.
F1-Score: The weighted average of Precision and Recall.

8. Results and Model Comparison
The models were evaluated on a 20% test split. The results are summarized below:
Model	Accuracy	Precision	Recall	F1-Score
Naive Bayes	97.48%	1.0000	0.7758	0.8737
Logistic Regression	96.22%	0.9425	0.7068	0.8078
Random Forest	97.48%	0.9687	0.8017	0.8773

9. Conclusion / Observations
Performance: All implemented models achieved an accuracy of over 96%, indicating high effectiveness in detecting spam.
Best Model: While Random Forest provided the best balance between precision and recall (highest F1-Score), Naive Bayes achieved a Perfect Precision (1.0). In a spam detection context, Naive Bayes is often preferred because it ensures that no legitimate "Ham" messages are accidentally marked as "Spam".
Preprocessing Impact: Removing duplicates and capping message lengths helped in creating a more generalized model that is less sensitive to extreme outliers.

10. How to Run the Project
Environment Setup: Ensure Python is installed along with the following libraries:
Bash pip install pandas scikit-learn
Data Loading: Place cleaned_spam_data.csv in your project directory.
Execution:
Load the dataset using pandas.
Split the data into training and testing sets (80/20 ratio).
Initialize the TfidfVectorizer and transform the text data.
Train the MultinomialNB or RandomForestClassifier.
Predict on test data and generate a classification report.




