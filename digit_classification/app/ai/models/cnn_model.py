import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle as pkl
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds
from numpy import nan as NaN

import digit_classification.app.ai.config
import h1st.core as h1


def cnn_block(x, filters, kernel_size=3, stride=1, name=None, conv_shortcut=False):
    bn_axis = 3    
    preact = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5, name=name + '_preact_bn')(x)
    preact = layers.Activation('relu', name=name + '_preact_relu')(preact)
   
    if conv_shortcut:
        shortcut = layers.Conv2D(
            2 * filters, 1, strides=stride, name=name + '_0_conv')(preact)
    else:
        shortcut = layers.MaxPooling2D(1, strides=stride)(x) if stride > 1 else x
    
    x = layers.Conv2D(
        filters, 1, strides=1, use_bias=False, name=name + '_1_conv')(preact)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5, name=name + '_1_bn')(x)
    x = layers.Activation('relu', name=name + '_1_relu')(x)
    x = layers.ZeroPadding2D(padding=((1, 1), (1, 1)), name=name + '_2_pad')(x)
    x = layers.Conv2D(
        filters,
        kernel_size,
        strides=stride,
        use_bias=False,
        name=name + '_2_conv')(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5, name=name + '_2_bn')(x)
    x = layers.Activation('relu', name=name + '_2_relu')(x)
    x = layers.Conv2D(2 * filters, 1, name=name + '_3_conv')(x)
    x = layers.Add(name=name + '_out')([shortcut, x])
    return x


def build_cnn_classifier(input_shape=(None, None, 3), n_class=3, classifier_activation='softmax'):
    inputs = tf.keras.Input(shape=input_shape)
    x = cnn_block(inputs, 8, kernel_size=3, stride=3, name='block1', conv_shortcut=True)
    x = cnn_block(x, 16, kernel_size=3, stride=2, name='block2', conv_shortcut=True)
    x = cnn_block(x, 32, kernel_size=3, stride=2, name='block3', conv_shortcut=True)
    x = layers.GlobalMaxPool2D()(x)
    outputs = layers.Dense(n_class, activation=classifier_activation,
                     name='predictions')(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs, name="test_model")
    return model


class DigitClassifier(h1.MLModel):
    def __init__(self):
        self.base_model = build_cnn_classifier(input_shape=(28, 28, 1), n_class=10)

    def load_data(self):
        """
        Implement logic of load data from data source
        :returns: loaded data
        """
        (ds_train, ds_test), ds_info = tfds.load(
            'mnist',
            split=['train', 'test'],
            shuffle_files=True,
            as_supervised=True,
            with_info=True,
        )
        return {
            "ds_train": ds_train,
            "ds_test": ds_test,
            "ds_info": ds_info
        }
    
    def prep(self, loaded_data: dict) -> dict:
        """
        Implement logic to prepare data from loaded data
        :param data: loaded data from ``load_data`` method
        :returns: prepared data
        """        
        def normalize_img(image, label):
            """Normalizes images: `uint8` -> `float32`."""
            return tf.cast(image, tf.float32) / 255., label
        
        ds_train = loaded_data["ds_train"]
        ds_test = loaded_data["ds_test"]
        ds_info = loaded_data["ds_info"]

        ds_train = ds_train.map(
            normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        ds_train = ds_train.cache()
        ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
        ds_train = ds_train.batch(128)
        ds_train = ds_train.prefetch(tf.data.experimental.AUTOTUNE)        
        
        ds_test = ds_test.map(
            normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        ds_test = ds_test.batch(128)
        ds_test = ds_test.cache()
        ds_test = ds_test.prefetch(tf.data.experimental.AUTOTUNE)        
        return {
            "ds_train": ds_train,
            "ds_test": ds_test,
        }        

    def explore(self, loaded_data: dict) -> None:
        """
        Implement logic to explore data from loaded data
        """
        ds_train = loaded_data['ds_train']
        y_true = []
        for idx, image_set in enumerate(ds_train):
            y_true.append(image_set[1])
        y_true = tf.concat(y_true, axis=0)
        np_array = y_true.numpy()
        plt.title('Distribution of Label in Train Data')        
        plt.hist(np_array)
        plt.show()

        ds_test = loaded_data['ds_test']
        y_true = []
        for idx, image_set in enumerate(ds_test):
            y_true.append(image_set[1])
        y_true = tf.concat(y_true, axis=0)
        np_array = y_true.numpy()
        plt.title('Distribution of Label in Test Data')
        plt.hist(np_array)  
        plt.show()

    def train(self, prepared_data: dict):
        """
        Implement logic of training model
        :param prepared_data: prepared data from ``prep`` method
        """
        ds_train, ds_test = prepared_data['ds_train'], prepared_data['ds_test']
        self.base_model.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
        )        
    
        self.base_model.fit(
            ds_train,
            epochs=6,
            validation_data=ds_test,
        )        

    def evaluate(self):
        """
        Implement logic to evaluate the model using the prepared_data
        This function will calculate model metrics and store it into self.metrics
        :param data: loaded data
        """
        
    def predict(self, input_data: dict) -> dict:
        """
        Implement logic to generate prediction from data
        :params data: data for prediction
        :returns: prediction result as a dictionary
        """
        X = input_data['X']
        if X.max() > 1:
            X = tf.cast(X, tf.float32) / 255.        
        prediction = self.base_model.predict(X)
        # not raise NotImplementedError so the initial model created by integrator will just work 
        prediction = np.argmax(prediction, axis=1)
        return {"classification" : prediction}

    