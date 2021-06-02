import pathlib
import string
from tensorflow import keras
from h1st.contrib.models.transformers import Seq2SeqTransformer as H1stSeq2SeqTransformer


class MyModel(H1stSeq2SeqTransformer):
    def __init__(self, version=None, vocab_size = 15000, sequence_length = 20, batch_size = 64, embed_dim=256, latent_dim=2048, num_heads = 8):
        super().__init__(vocab_size=vocab_size, sequence_length=sequence_length, batch_size=batch_size, embed_dim=embed_dim, latent_dim=latent_dim, num_heads=num_heads, version=version)

    def load_data(self, text_file=None):
        if text_file is None:
            text_file = keras.utils.get_file(
                fname="spa-eng.zip",
                origin="http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip",
                extract=True,
            )
            text_file = pathlib.Path(text_file).parent / "spa-eng" / "spa.txt"

        return super().load_data(text_file=text_file)

    def prep_data(self, data):
        self.strip_chars = string.punctuation + "¿"
        return super().prep_data(data)

    # ### customize if necessary ###
    # def train(self, data):
    #     ...

    # ### customize if necessary ###
    # def predict(self, data):
    #     ...

