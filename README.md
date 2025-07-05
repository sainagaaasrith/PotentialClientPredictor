# PotentialClientPredictor

## Overview
A Flask-based API to predict potential clients for promotion using a machine learning model.

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

---
Replace `yourusername` and feature names/values as appropriate for your setup.