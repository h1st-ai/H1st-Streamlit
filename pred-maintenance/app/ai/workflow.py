from h1st.core.node import Action, Decision
from h1st.django.api import H1stWorkflow, H1stModel

from django.db.models import ForeignKey, PROTECT


class FaultPredictionWorkflow(H1stWorkflow):
    anomaly_detector = \
        ForeignKey(
            verbose_name='Anomaly Detector',
            to=H1stModel,
            on_delete=PROTECT)

    fault_classifier = \
        ForeignKey(
            verbose_name='Fault Classifier',
            to=H1stModel,
            on_delete=PROTECT)

    class Meta:
        verbose_name = 'Fault Prediction Workflow'
        verbose_name_plural = 'Fault Prediction Workflows'

        db_table = 'H1stAI_FaultPredictionWorkflow'

        default_related_name = 'fault_prediction_workflows'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create Workflow structure if all attributes have been initialized
        if hasattr(self, 'anomaly_detector') and \
                hasattr(self, 'fault_classifier'):
            self.start() \
                .add(Decision(self.anomaly_detector)) \
                .add(
                    yes=Action(self.fault_classifier)
                )

            self.end()
