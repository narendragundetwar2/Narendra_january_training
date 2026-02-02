Test04 – Supervised Machine Learning Assignment

House Price Prediction

Project Title
House Price Prediction Using Supervised Machine Learning Algorithms

1. Problem Statement
The goal of this project is to build an automated system that accurately filters out unsolicited and potentially harmful "Spam" messages from legitimate "Ham" communications. By leveraging data cleaning and machine learning, the project aims to minimize the intrusion of spam while ensuring that no critical legitimate messages are lost (False Positives).

 2. Dataset Description
The dataset used for this project consists of raw SMS/text messages.
Initial Size: 5,572 records.
. Features: Includes the raw `text` of the message and a `target` label.
. Class Distribution: Contains two categories: "ham" and "spam".

3. Data Cleaning and Preprocessing Steps
. To ensure high-quality input for the model, the following steps were taken:
. Handling Missing Values: "Unnamed" columns were dropped, and the core columns were verified to have zero missing values.
. Data Type Correction: Columns were converted into appropriate formats for processing.
. Outlier Treatment: Message lengths were analyzed using the IQR Method; 68 outliers were detected and capped at a length of 250.00 characters.
. Deduplication: 409 duplicate records were removed, resulting in a final dataset of 5,163 records.
. Categorical Encoding: Labels were mapped to numerical values where ham and spam.

 4. Algorithms and Evaluation Metrics
The model performance was measured using standard classification metrics to ensure a balance between precision and sensitivity:
. Accuracy: The overall success rate of the model.
. Precision: The ability to avoid flagging legitimate mail as spam.
. Recall: The ability to capture all actual spam messages.
. F1 Score: The harmonic mean of precision and recall.

 5. Model Performance Results
The model achieved exceptional results, as evidenced by the high scores across all metrics: 
. Accuracy: 98%.
. Precision: 97%.
. Recall: 91%.
. F1 Score: 94%.

 6. Visualization
The Confusion Matrix provides a visual breakdown of the model's predictions against the actual values:
. True Negatives (889): Correctly identified "Ham".
. True Positives (124): Correctly identified "Spam".
. False Positives (4): Legitimate messages incorrectly flagged as spam.
. False Negatives (12): Spam messages that reached the inbox.

 7. Conclusion
The project successfully developed a robust spam detection model with an Accuracy of 98% . The data cleaning phase was critical, specifically the removal of duplicates and capping of message lengths, which provided a cleaner signal for the algorithm. With a high Precision of 97% , the model is highly reliable for real-world application as it rarely misclassifies important legitimate messages.

