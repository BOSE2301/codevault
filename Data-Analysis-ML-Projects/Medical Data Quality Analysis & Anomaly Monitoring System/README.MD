# Anomaly Detection with Blockchain, AWS Integration, and FastAPI Deployment

This project—developed in a Jupyter Notebook (`.ipynb`)—demonstrates a full machine learning pipeline for anomaly detection using Isolation Forest and neural networks, integrated with **AWS S3** for storage, **blockchain-style hash verification** for integrity, and **FastAPI** for model deployment.

---

## File Format

- **Main Code File**: `notebook.ipynb`  
  Contains all steps, from environment setup to API deployment.

---

## Project Objectives

- Set up the environment and configure AWS services
- Load, clean, and merge medical datasets (Breast Cancer & Diabetes)
- Verify data integrity using **SHA-256** hashing (blockchain-style)
- Detect anomalies in medical data using **Isolation Forest**
- Train a neural network with **hyperparameter tuning**
- Evaluate and visualize model performance
- Deploy the model via **FastAPI** and test predictions with CSV uploads

---

## Chapter Overview

### **Chapter 1: Environment Setup and AWS Configuration**
- Import libraries: `os`, `boto3`, `google.colab`, `logging`
- Retrieve AWS credentials securely from Colab secrets
- Configure S3 client and logging

### **Chapter 2: Data Loading and Preparation**
- Load Breast Cancer and Diabetes datasets from `sklearn.datasets`
- Extend, normalize, and combine datasets to create 1337 samples
- Upload `X_combined.csv` and `y_combined.csv` to S3

### **Chapter 3: File Integrity and Data Verification**
- Use SHA-256 hashing to create and store file hashes
- Append hash log (`file_hashes.txt`) to S3 for immutable reference
- Download and verify datasets to ensure integrity

### **Chapter 4: Anomaly Detection**
- Use Isolation Forest to detect anomalies in the test data
- Visualize anomalies and upload results to S3
- Save the model as `isolation_forest.pkl`

### **Chapter 5: Neural Network Training with Hyperparameter Tuning**
- Build a 3-layer dense neural network using TensorFlow
- Perform grid search over hyperparameters (learning rate, batch size, etc.)
- Save best model as `best_model.h5` and scaler as `scaler.pkl`
- Upload artifacts and hash them for integrity verification

### **Chapter 6: Model Evaluation and Visualization**
- Evaluate using accuracy, confusion matrix, and ROC AUC
- Generate and upload visualizations (confusion matrix, training history)

### **Chapter 7: FastAPI Deployment and Testing**
- Build an API with FastAPI for real-time predictions
- Load the trained model and scaler from S3
- Test `/predict/` endpoint with a sample CSV input

---

## Requirements

This project was run in **Google Colab**. To replicate locally, install:

```bash
pip install boto3 pandas numpy scikit-learn tensorflow matplotlib seaborn joblib fastapi uvicorn requests python-multipart
