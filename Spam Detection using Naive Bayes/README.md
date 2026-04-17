# Spam Detection using Naive Bayes & NLP
## Project Overview
This project focuses on building a Spam Detection System using Natural Language Processing (NLP) and the Naive Bayes algorithm. The model classifies messages as Spam or Not Spam (Ham) based on the text content.
With the increasing use of messaging platforms, spam detection plays a crucial role in filtering unwanted and harmful messages.
## Objective
- To classify messages into Spam or Ham
- To apply basic NLP techniques for text preprocessing
- To build a machine learning model using Naive Bayes
- To evaluate model performance using standard metrics
## Technologies Used
1.Python 
2.NumPy
3.Pandas
4.Scikit-learn
5.Natural Language Processing (NLP)
## Dataset
The dataset contains labeled messages as spam or ham
Common dataset used: SMS Spam Collection Dataset
## Project Workflow
1️.Data Preprocessing
* Convert text to lowercase
* Remove punctuation and special characters
* Tokenization
* Stopword removal
2️. Feature Extraction
* Used TF-IDF (Term Frequency - Inverse Document Frequency) to convert text into numerical features
3️. Model Building
* Applied Multinomial Naive Bayes algorithm
* Trained the model on processed data
4️. Model Evaluation
* Accuracy Score
* Confusion Matrix
* Precision & Recall
## Results
* The model successfully classifies spam messages with good accuracy
* Naive Bayes performs well for text classification problems
