# Heart_disease_prediction
Heart Disease Prediction System is a web app that predicts heart disease risk using a machine learning model. Built with Python, Flask, HTML, and CSS, it features a user-friendly interface for data input and real-time predictions. Easy setup with detailed instructions provided in the repository.


## Overview

This project is a comprehensive web application designed to predict the likelihood of heart disease in individuals using machine learning. The application leverages Python for its machine learning models, Flask for the backend, and HTML/CSS for the frontend. It aims to provide a user-friendly interface for individuals to input their health data and receive predictions on their risk of heart disease.

## Features

--**Predictive Machine Learning Model**: Utilizes a robust machine learning model trained on a Kaggle dataset to accurately predict the risk of heart disease based on user input. The model is fine-tuned through preprocessing, training, and rigorous testing.

--**User Input-Based Risk Prediction**: Takes input from users based on various health parameters such as age, blood pressure, cholesterol levels, and more. It predicts the likelihood of heart disease occurring within the next 10 years based on these inputs.

--**Intuitive User Interface**: Designed with HTML and CSS for a sleek, user-friendly experience. The interface is responsive and easy to navigate, allowing users to input their health data effortlessly.

--**Real-Time Risk Assessment**: Provides instant feedback on heart disease risk. Users receive immediate, actionable insights and predictions based on their entered health metrics.

--**Seamless Backend Integration**: Built with Flask, the backend efficiently processes user inputs, interacts with the machine learning model, and manages data flow between the frontend and the model.

--**Interactive Data Visualization**: Features optional visualizations to help users better understand their risk factors and model predictions (if applicable).

--**Customizable and Scalable**: Easily adaptable for additional features, such as integrating more health metrics or extending the model to include other health conditions.



## Machine Learning Algorithms Used
The project employs a variety of machine learning algorithms to evaluate and predict heart disease risk:

- **RandomForestClassifier**: An ensemble learning method that uses multiple decision trees to improve prediction accuracy.
- **AdaBoostClassifier**: Boosts the performance of a weak classifier by combining multiple classifiers to create a strong classifier.
- **GradientBoostingClassifier**: Builds models in a sequential manner, each correcting the errors of its predecessor, to enhance predictive performance.
- **LogisticRegression**: A statistical method for binary classification that predicts the probability of a binary outcome.
- **SVC (Support Vector Classifier)**: Finds the optimal hyperplane that best separates different classes in the feature space.
- **KNeighborsClassifier**: Classifies data based on the majority vote from the nearest neighbors in the feature space.
- **DecisionTreeClassifier**: Uses a tree-like model of decisions and their possible consequences to make predictions.
- **GaussianNB**: Assumes that features follow a normal distribution and is used for classification tasks.
- **XGBClassifier**: An implementation of gradient boosting that is optimized for speed and performance, often used for large-scale problems.

## Technologies Used

- **Python**: For machine learning model development and data processing.
- **Flask**: For building the backend API and serving the web application.
- **HTML/CSS**: For designing and structuring the web application's frontend.
- **Scikit-Learn**: For machine learning model implementation (specify if a particular library was used).
- **Pandas/Numpy**: For data manipulation and preprocessing.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shu03bh/heart_disease_prediction.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd heart_disease_prediction
   ```

3. **Install Dependencies**:
   Create a virtual environment and install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

   Required Packages:
The requirements.txt file includes the following essential packages:

**Flask**: For building the backend API and serving the web application.
**scikit-learn**: For implementing and using the machine learning models.
**pandas**: For data manipulation and preprocessing.
**numpy**: For numerical operations.
**os**: For operating system interactions.
**pickle**: For serializing and deserializing Python objects.
**xgboost**: For the XGBClassifier (if used).

4. **Run the Application**:
   Start the Flask server to run the web application.
   ```bash
   python app.py
   ```

5. **Access the Web Application**:
   Open your web browser and go to `http://localhost:5000` to interact with the application.

## Dataset

The project uses a dataset containing various health metrics relevant to heart disease prediction. The dataset, sourced from Kaggle, has been preprocessed for this project. The model was then trained and tested on this processed dataset to ensure reliable predictions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please submit a pull request or open an issue.
