# Derived from http://the-odd-dataguy.com/be-more-efficient-to-produce-ml-models-with-mlflow/
import mlflow.sagemaker as mfs

# AWS setup
awsid = "xxxxxx"# id of the AWS user that will deploy the system
region "xxxxx" # AWS region to deploy the API
arn = f"arn:aws:iam::{awsid}:role/xxxxx" # Arn of the role that will be used to do the deployment on sagemaker

# Give a nae ot the app
app_name = "wine-quality" # Name of the app that will be deployed

# Setup the path for the deployment
model_uri = "trained_model"
image_url = awsid + ".dkr.ecr." + region + ".amazonaws.com/mlflow-pyfunc:1.4.0" #import tant to give the right version mlfloe deploy in ECR

# Deploy it
mfs.deploy(app_name = app_name,
           model_uri = model_uri,
           region_name = region,
           mode = "replace", # like that you can overwrite
           execution_role_arn = arn,
           image_url = image_url)