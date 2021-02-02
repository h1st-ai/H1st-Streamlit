from h1st.django.api import H1stWorkflow
from h1st.core.node import Action


class Multiply(Action):
    def __init__(self, n_times):
        super().__init__()
        self.n_times = n_times

    def call(self, command, data: dict) -> dict:
        return {k: self.n_times * v for k, v in data.items()}


class MyWorkflow(H1stWorkflow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start()
        self.add(Multiply(10))
        self.end()
