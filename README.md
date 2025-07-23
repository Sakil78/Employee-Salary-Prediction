# Employee Salary Prediction (Flask Web App)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Scikit‑learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Random Forest](https://img.shields.io/badge/Random%20Forest-v1.0-green)](https://www.randomforest.se/en/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7-00639C?style=for-the-badge&logo=xgboost)](https://xgboost.ai/)

This project is an AI/ML-powered web application for predicting employee salaries based on various features such as age, experience, job type, and more. It uses a Random Forest model trained on real-world data and provides interactive visualizations and evaluation metrics.

## Features

- Predict monthly and annual salaries for employees
- Interactive web interface built with Flask and Bootstrap
- Model evaluation metrics and visualizations
- Sample predictions and feature importance analysis

## Project Structure

- `app.py` – Main Flask application
- `models/` – Trained model, encoders, and scaler (`*.pkl`)
- `static/` – CSS, JS, and plot images
- `templates/` – HTML templates
- `web_app_assets/` – Model metadata and evaluation data (`*.json`)

## How to Run

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```sh
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Notes

- Make sure the `models/`, `static/`, `templates/`, and `web_app_assets/` folders are present and contain the necessary files.
- The app will load the trained model
