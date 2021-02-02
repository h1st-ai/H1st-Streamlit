import h1st.core as h1
from app.ai.models.sklearn_smv_classifier import SklearnSVMClassifier
from app.ai.models.tensorflow_mlp_classifier import TensorflowMLPClassifier
from app.ai.models.default_classifier_ensemble import DefaultClassifierEnsemble


class DefaultClassifierEnsembleWorkflow(h1.Graph):
    def __init__(self):
        super().__init__()

        self.start()
        self.add(
            DefaultClassifierEnsemble(
                [SklearnSVMClassifier().load('sk_svm_default_classifier'), 
                 TensorflowMLPClassifier().load('tf_mlp_default_classifier')]
            ).load('default_classifier_ensemble'))
        self.end()

