
import glob
import os
import sys
sys.path.append("..")
sys.path.append("../..")
from typing import List

import cv2
from fastapi.datastructures import UploadFile
from fastapi.params import File
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import shutil
from starlette.datastructures import FormData
import sqlalchemy

from app.ai.workflow import DefaultClassifierEnsembleWorkflow
from app.api.db import InputData, OutputData

# Create a backend app
app = FastAPI()

# Load pre-trained classifier ensemble workflow
default_classifier_ensemble_workflow = DefaultClassifierEnsembleWorkflow()

@app.post('/predict', response_model=List[OutputData])
def predict_number(input_data: List[InputData]):
    # Predict number
    input_list = []    
    for data in input_data:
        input_list.append([val for val in data.dict().values()])
    results = default_classifier_ensemble_workflow.predict({'X': np.array(input_list)})["predictions"]
    
    return [{"next_month_default": bool(result)} for result in results]

