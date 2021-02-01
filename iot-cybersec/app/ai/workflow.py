from h1st.core.node import Action, Decision
from h1st.django.api import H1stWorkflow, H1stModel

from django.db.models import ForeignKey, PROTECT


class IntrusionDetectionWorkflow(H1stWorkflow):
    class Meta:
        verbose_name = 'Intrusion Detection Workflow'
        verbose_name_plural = 'Intrusion Detection Workflows'

        db_table = 'H1stAI_IntrusionDetectionWorkflow'

        default_related_name = 'intrusion_detection_workflows'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create Workflow structure if all attributes have been initialized
        ...

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}: '
