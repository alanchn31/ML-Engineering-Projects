## Description
---
This repo looks at MLFlow, which is "An open-source platform to manage the ML lifecycle." by Databricks

**Why MLFlow?**
* It provides a nice structure to organize code and view results, in the experimentation phase of the machine learning life cycle.

* It provides:
    1. Artifact Versioning
    2. Experiment Comparison
    3. Deployment Capabilities

This repo trains an cross-validated ElasticNet model and persists it as an artefact. The code is derived from:
https://github.com/mlflow/mlflow/tree/master/examples/sklearn_elasticnet_wine

## Running this MLFlow Project:
---
* Install mlflow using ``` pip install mlflow ``` if you have not done so
* Run ```mlflow run https://github.com/alanchn31/ML-Engineering-Projects.git#wine-quality-elasticnet```

## Deploying Model:
---
1. AWS Sagemaker:  
    a) Login to aws using aws-cli to authenticate  
    b) Build and push the container to ECR (only needs to be called once)
    ```bash
    mlflow sagemaker build-and-push-container
    ```
    c) Run locally to test the model  
    ```bash
    mlflow sagemaker run-local -m trained_model
    ```
    d) deploy to Sagemaker
    ```
    mlflow sagemaker deploy <parameters> - deploy the model remotely
    ```

2. Azure ML:  
T.B.D.