from h1st.model.model import Model as H1stModel


class MyModel(H1stModel):
    def predict(self, input_data):
        return input_data