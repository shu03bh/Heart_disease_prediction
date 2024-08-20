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

4. **Run the Application**:
   Start the Flask server to run the web application.
   ```bash
   python app.py
   ```

5. **Access the Web Application**:
   Open your web browser and go to `http://localhost:5000` to interact with the application.

## Dataset

The project uses a dataset containing various health metrics relevant to heart disease prediction. EnsuThe dataset, sourced from Kaggle, has been preprocessed for this project. The model was then trained and tested on this processed dataset to ensure reliable predictions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please submit a pull request or open an issue.
