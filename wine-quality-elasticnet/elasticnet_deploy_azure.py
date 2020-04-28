# Code derived from https://www.mlflow.org/docs/latest/models.html
import mlflow.azureml

from azureml.core import Workspace
from azureml.core.webservice import AciWebservice, Webservice


# Create or load an existing Azure ML workspace. You can also load an existing workspace using
# Workspace.get(name="<workspace_name>")
workspace_name = ""
subscription_id = ""
resource_group = ""
location = ""
# azure_workspace = Workspace.create(name=workspace_name,
#                                    subscription_id=subscription_id,
#                                    resource_group=resource_group,
#                                    location=location,
#                                    create_resource_group=True,
#                                    exist_okay=True)
azure_workspace = Workspace.get(name=workspace_name,
                                subscription_id=subscription_id,
                                resource_group=resource_group)

# Build an Azure ML container image for deployment
azure_image, azure_model = mlflow.azureml.build_image(model_uri="trained_model",
                                                      workspace=azure_workspace,
                                                      description="Wine regression model 1",
                                                      synchronous=True)
# If your image build failed, you can access build logs at the following URI:
print("Access the following URI for build logs: {}".format(azure_image.image_build_log_uri))

# Deploy the container image to ACI
webservice_deployment_config = AciWebservice.deploy_configuration()
webservice = Webservice.deploy_from_image(
                    image=azure_image, workspace=azure_workspace, name="wine-quality")
webservice.wait_for_deployment()

# After the image deployment completes, requests can be posted via HTTP to the new ACI
# webservice's scoring URI. The following example posts a sample input from the wine dataset
# used in the MLflow ElasticNet example:
# https://github.com/mlflow/mlflow/tree/master/examples/sklearn_elasticnet_wine
print("Scoring URI is: %s", webservice.scoring_uri)

import requests
import json

# `sample_input` is a JSON-serialized pandas DataFrame with the `split` orientation
sample_input = {
    "columns": [
        "alcohol",
        "chlorides",
        "citric acid",
        "density",
        "fixed acidity",
        "free sulfur dioxide",
        "pH",
        "residual sugar",
        "sulphates",
        "total sulfur dioxide",
        "volatile acidity"
    ],
    "data": [
        [8.8, 0.045, 0.36, 1.001, 7, 45, 3, 20.7, 0.45, 170, 0.27]
    ]
}
response = requests.post(
              url=webservice.scoring_uri, data=json.dumps(sample_input),
              headers={"Content-type": "application/json"})
response_json = json.loads(response.text)
print(response_json)