# Employee Salary Prediction (Flask Web App)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Scikit‑learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Random Forest](https://img.shields.io/pypi/v/scikit-learn?label=Random%20Forest&style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7-00639C?style=for-the-badge&logo=xgboost)](https://xgboost.ai/)

This project is an AI/ML-powered web application for predicting employee salaries based on various features such as age, experience, job type, and more. It uses a Random Forest model trained on real-world data and provides interactive visualizations and evaluation metrics.

## ✨ Key Features

- **Real‑Time Salary Prediction**  
  Low‑latency inference (<500 ms) across ~10K employee records.
- **Robust Preprocessing Pipeline**  
  Categorical encoding & scaling pipeline built with Pandas and scikit‑learn, reducing data prep time by 60%.
- **High‑Performance Model**  
  Random Forest regressor tuned via grid search, delivering **R² = 0.921**, **RMSE = Rs. 27,280**, **MAE = Rs. 8,252**.
- **Interactive Visualizations**  
  Matplotlib‑driven plots for feature importance, residual analysis, and actual vs. predicted salary distributions.
- **CI/CD & Deployment**  
  Model serialization with Joblib and automated redeployment on Render for 50% higher throughput.

---

## 🛠️ Tech Stack

| Component             | Technology / Library    |
|-----------------------|-------------------------|
| **Backend**           | Flask                   |
| **ML Framework**      | scikit‑learn, XGBoost   |
| **Data Handling**     | Pandas, NumPy           |
| **Model Persistence** | Joblib                  |
| **Visualization**     | Matplotlib              |
| **Deployment**        | Render.com              |

---

## Project Structure

- `app.py` – Main Flask application
- `models/` – Trained model, encoders, and scaler (`*.pkl`)
- `static/` – CSS, JS, and plot images
- `templates/` – HTML templates
- `web_app_assets/` – Model metadata and evaluation data (`*.json`)

## 🧠 Machine Learning Pipeline

### 1. Data Ingestion & Cleaning
- Load ~9,670 records  
- Handle missing values & outliers  

### 2. Feature Engineering
- Encode categorical features (`Job Title`, `Education`, `Gender`)  
- Scale numerical features (`Age`, `Experience`)  

### 3. Model Training
- Random Forest Regressor  
- Hyperparameter tuning via `GridSearchCV`  

### 4. Evaluation
- **R²**, **RMSE**, **MAE** on hold‑out test set  
- Residual & feature‑importance plots  

### 5. Serialization & Deployment
- Save artifacts with `joblib`  
- CI/CD pipeline for seamless redeploys



## 🔧 How to Run

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
