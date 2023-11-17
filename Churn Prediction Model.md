Churn Prediction Model
Overview

This repository contains a churn prediction model designed to assist telecom operators in identifying customers who are most likely to churn. The model utilizes a multilayer perceptron (MLP) implemented with the Keras functional API. The trained model is then deployed using Flask, allowing users to make predictions through a web interface.
Features

The model uses the following features for churn prediction:

    TotalCharges
    MonthlyCharges
    Tenure
    Contract
    PaymentMethod
    TechSupport

Model Architecture

The churn prediction model is implemented using the Keras functional API. The architecture of the multilayer perceptron includes input layers for each feature, dense hidden layers, and a sigmoid output layer for binary classification (churn or no churn).
Deployment with Flask

The trained model is deployed using Flask, a lightweight web framework for Python. Users can interact with the model through a simple web interface. The Flask app includes HTML templates for user input and result display.


Run the Flask app:



    python app.py

    Open your web browser and navigate to access the churn prediction interface.

    Input values for the features (TotalCharges, MonthlyCharges, Tenure, Contract, PaymentMethod, TechSupport) and click "Predict" to see the model's churn prediction.

Model Training

The model is trained using a labeled dataset with historical customer data. The training script and dataset used can be found in the train_model directory. Ensure that you have the necessary data before retraining the model.
Directory Structure

    app.py: Flask application for model deployment.
    templates/: HTML templates for user interface.
    train_model/: Scripts and resources for model training.
    model.h5: Pre-trained MLP model.

Dependencies

    Flask
    Keras
    NumPy
    Pandas
    scikit-learn
    TensorFlow

