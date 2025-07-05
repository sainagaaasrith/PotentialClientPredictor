# PotentialClientPredictor

## Overview

### Bank Customer Classification for Business Promotion

**Project Overview**
This project aims to identify potential customers for promoting bank and business services. We leverage machine learning techniques to classify customers as "recommended" or "not recommended" based on their characteristics. The solution includes data preprocessing, model training, and a Flask-based API for real-time predictions, all containerized with Docker for easy deployment.

**Dataset**
The dataset comprises approximately 4000 customer records, each labeled as either "recommended" or "not recommended."

**Technical Stack**
- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, Flask
- Containerization: Docker
- API Testing: Postman, cURL

**Methodology**
1. **Data Preprocessing**
   - Data Cleaning: Handling unknown values by imputing them with the mode of their respective columns.
   - Feature Scaling: Applying StandardScaler to numerical features to standardize their range.
   - Categorical Encoding: Utilizing OneHotEncoder to convert categorical features into a numerical format suitable for machine learning models.
2. **Model Training & Evaluation**
   - We explored various classification algorithms to find the best fit for our problem: Logistic Regression, Decision Tree, Random Forest, K-Means (potentially used for clustering or as a feature engineering step), and Naive Bayes.
   - After thorough evaluation using metrics such as F1 Score and accuracy, Logistic Regression emerged as the optimal model, consistently achieving an impressive accuracy of approximately 91%.
3. **Model Persistence**
   - The trained Logistic Regression model is saved as a serialized .pkl file for efficient loading and deployment.
4. **API Development**
   - A RESTful API was developed using the Flask framework to serve predictions.
   - Endpoint: `/predict`
   - Method: POST
   - Functionality: This endpoint accepts customer data as input and returns a prediction (recommended/not recommended) along with the raw prediction probability.
5. **Containerization with Docker**
   - The entire solution is containerized for easy deployment.

## Getting Started

### 1. Build Docker Image
```
docker build -t potential-client-predictor .
```

### 2. Tag and Push to Docker Hub
```
docker tag potential-client-predictor yourusername/potential-client-predictor:latest
docker push yourusername/potential-client-predictor:latest
```

### 3. Pull and Run on EC2
```
docker pull yourusername/potential-client-predictor:latest
docker run -d -p 5000:5000 --name potential-client-predictor yourusername/potential-client-predictor:latest
```

### 4. API Endpoints
- `GET /`  
  Returns required feature names for prediction.
- `POST /predict`  
  Request body: JSON with required features.  
  Example:
  ```json
  {
    "feature1": value1,
    "feature2": value2
  }
  ```
  Response:
  ```json
  {
    "prediction": "Best Client for Promotion",
    "raw_prediction": 1
  }
  ```

### 5. Test with Postman or curl
- Example curl command:
  ```sh
  curl -X POST http://<EC2-Public-IP>:5000/predict -H "Content-Type: application/json" -d '{"feature1": value1, "feature2": value2}'
  ```
