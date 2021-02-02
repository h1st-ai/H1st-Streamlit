import h1st.core as h1
from app.ai.models.cnn_model import DigitClassifier


class DigitClassificationWorkflow(h1.Graph):
    def __init__(self):
        super().__init__()

        self.start()
        self.add(DigitClassifier().load("mnist_cnn_v1"))
        self.end()
