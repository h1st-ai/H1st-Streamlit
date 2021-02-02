from h1st.django.api import H1stWorkflow
from h1st.core.node import Action


class Multiply10x(Action):
    def call(self, command, data: dict) -> dict:
        return {k: 10 * v for k, v in data.items()}


class My10xWorkflow(H1stWorkflow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start()
        self.add(Multiply10x())
        self.end()
