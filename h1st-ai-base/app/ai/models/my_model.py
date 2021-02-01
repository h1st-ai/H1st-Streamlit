from h1st.django.api import H1stModel


class MyModel(H1stModel):
    def predict(self, data: dict) -> dict:
        return data
