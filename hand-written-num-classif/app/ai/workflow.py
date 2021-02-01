import h1st.core as h1
from app.ai.cnn_model import CNNNumberClassifier


class ImageClsWorkflow(h1.Graph):
    def __init__(self):
        super().__init__()

        self.start()
        self.add(CNNNumberClassifier().load("mnist_cnn"))
        self.end()
