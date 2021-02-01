from django.contrib import admin

from .workflow import ObjectDetectionAndClassificationWorkflow
from .models.object_detectors.my_object_detector import MyObjectDetector
from .models.object_classifiers.my_object_classifier import MyObjectClassifier


admin.site.register([
    ObjectDetectionAndClassificationWorkflow,
    MyObjectDetector, MyObjectClassifier
])
