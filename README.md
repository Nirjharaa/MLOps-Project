# MLOps-Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Nirjharaa/MLOps-Project.mlflow \
MLFLOW_TRACKING_USERNAME=Nirjharaa \
MLFLOW_TRACKING_PASSWORD=b2edb1d1da991b286c779422094674077369df2b \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Nirjharaa/MLOps-Project.mlflow

export MLFLOW_TRACKING_USERNAME=Nirjharaa 

export MLFLOW_TRACKING_PASSWORD=b2edb1d1da991b286c779422094674077369df2b

```

