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
import copy

from app.ai.workflow import DigitClassificationWorkflow
from app.api.db import database, prediction_feedback, PredictionFeedback
from app.api.utils import preprocess_drawn_image


app = FastAPI()
app.mount("/img_files", StaticFiles(directory="api/img_files"), name="img_files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-trained image classification workflow
digit_cls_workflow = DigitClassificationWorkflow()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post('/predict_digit')
async def predict_digit(file: UploadFile = File(default=None)):
    file_path = os.path.join('api', 'img_files', file.filename)
    file_content = (file.file.read())
    with open(file_path, "wb+") as file_object:
        file_object.write(file_content)
        file_object.close()


    with open(file_path, "r") as file_object:
        # Get a drawn image
        input_img = preprocess_drawn_image(file_object, (28,28))
        
        # Predict number
        results = digit_cls_workflow.predict({'X': input_img})["classification"][0]


    # Save feedback in database
    query = prediction_feedback.insert().values(
        filename = file.filename,
        prediction = int(results),
    )

    await database.execute(query)
    
    return {"prediction": int(results)}

@app.get('/predictions', response_model=List[PredictionFeedback])
async def get_predictions():
    query = prediction_feedback.select()
    result = await database.fetch_all(query=query)
    return result

# @app.post('/feedback')
# async def send_feed_back(file: UploadFile = File(default=None), prediction: int = Form(None), feedback: bool = Form(True), correct_number: int = Form(None)):
    
#     # save file into uploads folder
#     with open(os.path.join('api', 'img_files', file.filename), 'wb+') as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Save feedback in database
#     query = prediction_feedback.insert().values(
#         filename = file.filename,
#         prediction = prediction,
#         feedback = feedback,
#         correct_number = correct_number
#     )
#     obj = await database.execute(query)
#     return {
#         'result': obj
#     }




# @app.get('/retrain')
# async def retrain_model():    
#     1. query db to get (prediction, correct_number, filename)
#     2. load image and change it into numpy array
#     3. re-train model (takes 2~3 minutes) how to handle this ?

