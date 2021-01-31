from h1st.django.model.api import H1stWorkflow, H1stModel

from django.db.models import ForeignKey, PROTECT


class MyWorkflow(H1stWorkflow):
    first_step = \
        ForeignKey(
            to=H1stModel,
            on_delete=PROTECT)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start() \
            .add(self.first_step)

        self.end()

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}: ' \
               f'First Step = {self.first_step}'
