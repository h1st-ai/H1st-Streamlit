from django.contrib import admin

from .workflow import FaultPredictionWorkflow
from .models.anomaly_detectors.vae_anomaly_detector import VAEAnomalyDetector
from .models.fault_classifiers.fuzzy_logic_fault_classifier import \
    FuzzyLogicFaultClassifier
from .models.fault_classifiers.cnn_fault_classifier import CNNFaultClassifier
from .models.fault_classifiers.ensemble_fault_classifier import \
    EnsembleFaultClassifier


admin.site.register([
    FaultPredictionWorkflow,
    VAEAnomalyDetector,
    EnsembleFaultClassifier, FuzzyLogicFaultClassifier, CNNFaultClassifier])
