from typing import List, Optional

import databases
from pydantic import BaseModel
import sqlalchemy


DATABASE_URL = "sqlite:///./num_cls.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
prediction_feedback = sqlalchemy.Table(
    "prediction_feedback",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("filename", sqlalchemy.String),
    sqlalchemy.Column("prediction", sqlalchemy.Integer),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

class PredictionFeedback(BaseModel):
    id: int
    filename: str
    prediction: int
    feedback: bool
    correct_number: Optional[int]

# class H1stPydantic(h1.Model, BaseModel):

# class H1stModel(BaseModel):
#     name : str
#     train_data : str
#     created_at : str
#     version : int

# class H1stGraph(BaseModel):
#     models : List[H1stModel]

# class WageInputData(BaseModel):
#     experience: int
#     test_score: int
#     interview_score: int

# class WageInputData(BaseModel):
#     experience: int
#     test_score: int
#     interview_score: int    

