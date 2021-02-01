
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
from app.api.utils import preprocess_drawn_image


app = FastAPI()

# Load pre-trained classifier ensemble workflow
default_classifier_ensemble_workflow = DefaultClassifierEnsembleWorkflow()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post('/predict', response_model=List[OutputData])
def predict_number(input_data: List[InputData]):
    # Predict number
    results = default_classifier_ensemble_workflow.predict({'X': np.array(input_data)})["classification"][0]

    return {"prediction": bool(results)}


# @app.get('/retrain')
# async def retrain_model():    
#     1. query db to get (prediction, correct_number, filename)
#     2. load image and change it into numpy array
#     3. re-train model (takes 2~3 minutes) how to handle this ?

