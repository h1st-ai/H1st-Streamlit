import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score
import tensorflow as tf

from app.ai import config
from app.ai.utils import prepare_train_test_data
import h1st.core as h1


class DefaultClassifierEnsemble(h1.RandomForestClassifierStackEnsemble):
    def load_data(self,):
        df = pd.read_excel(config.DATA_PATH, header=1)
        return df

    def prep(self, loaded_data):
        return prepare_train_test_data(loaded_data)
