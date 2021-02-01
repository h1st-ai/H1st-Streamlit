import h1st.core as h1
from app.ai.sklearn_smv_classifier import SklearnSVMClassifier
from app.ai.tensorflow_mlp_classifier import TensorflowMLPClassifier
from app.ai.classifier_ensemble import RFClassifierStackEnsemble


class ClassifierEnsembleWorkflow(h1.Graph):
    def __init__(self):
        super().__init__()

        self.start()
        self.add(
            RFClassifierStackEnsemble(
                [SklearnSVMClassifier().load('my_sk_svm'), 
                 TensorflowMLPClassifier().load('my_tf_mlp')]
            ).load('my_ensemble'))
        self.end()
