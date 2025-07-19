# Employee Salary Prediction (Flask Web App)

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
- The app will load the trained model and