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
    You should see this:
    ```bash
    Serving on http://DESKTOP-MVR83PR:1234
    ```
    Then, do a POST request to http://localhost:1234/invocations using JSON:
    ```json
    {
	"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],
	
	"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]
    }
    ```
    Headers should be:
    ```json
    {
        "Content-Type": "application/json",
        "format": "pandas-split"
    }
    ```
    This would give a result:
    ```json
    [33.04794191637013]
    ```
    d) Deploy to Sagemaker  
    Fill in the details in elasticnet_deploy_aws.py and run the file
    ```
    python elasticnet_deploy_aws.py
    ```
    Once done, look up the endpoint URL in AWS Sagemaker and call it the exact same way as the local endpoint we set up earlier. 
    Remember NOT to ever commit personal information about aws on github.


2. Azure ML:  
T.B.D.