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