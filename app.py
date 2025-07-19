import pickle
import json
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
import io
import base64
import os

app = Flask(__name__)

# Load the saved model and preprocessors
with open('models/salary_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('web_app_assets/feature_options.json', 'r') as f:
    feature_options = json.load(f)

with open('web_app_assets/model_metadata.json', 'r') as f:
    model_metadata = json.load(f)

# Load evaluation data
try:
    with open('web_app_assets/evaluation_data.json', 'r') as f:
        evaluation_data = json.load(f)
except FileNotFoundError:
    print("Warning: evaluation_data.json not found. Creating default evaluation data.")
    evaluation_data = {
        'model_performance': {
            'r2_score': 0.9207,
            'r2_percentage': 92.07,
            'rmse': 27280,
            'mae': 8252,
            'accuracy_description': "92.1% accuracy"
        },
        'sample_predictions': [],
        'feature_importance': [],
        'data_info': {
            'total_samples': 9670,
            'training_samples': 7736,
            'test_samples': 1934,
            'features_count': 7
        }
    }

@app.route('/')
def home():
    return render_template('index.html', 
                         feature_options=feature_options, 
                         model_metadata=model_metadata,
                         evaluation_data=evaluation_data)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = {
            'Age': int(request.form['age']),
            'Years of Experience': int(request.form['experience']),
            'Gender': request.form['gender'],
            'Job_Type': request.form['job_type'],
            'Job_Rank': request.form['job_rank'],
            'Experience_Level': request.form['experience_level'],
            'Education_Level_Clean': request.form['education_level']
        }
        
        # Create DataFrame
        input_df = pd.DataFrame([data])
        
        # Encode categorical variables
        categorical_features = ['Gender', 'Job_Type', 'Job_Rank', 'Experience_Level', 'Education_Level_Clean']
        numerical_features = ['Age', 'Years of Experience']
        
        for col in categorical_features:
            if col in label_encoders:
                input_df[col] = label_encoders[col].transform(input_df[col])
        
        # Scale numerical features
        input_df[numerical_features] = scaler.transform(input_df[numerical_features])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        return jsonify({
            'success': True,
            'monthly_salary': round(prediction, 0),
            'annual_salary': round(prediction * 12, 0),
            'formatted_monthly': f"₹{prediction:,.0f}",
            'formatted_annual': f"₹{prediction * 12:,.0f}"
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
