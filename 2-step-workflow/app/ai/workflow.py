from h1st.django.api import H1stWorkflow, H1stModel

from django.db.models import ForeignKey, PROTECT


class ObjectDetectionAndClassificationWorkflow(H1stWorkflow):
    object_detector = \
        ForeignKey(
            verbose_name='Object Detector',
            to=H1stModel,
            on_delete=PROTECT)

    object_classifier = \
        ForeignKey(
            verbose_name='Object Classifier',
            to=H1stModel,
            on_delete=PROTECT)

    class Meta:
        verbose_name = 'Object Detection and Classification Workflow'
        verbose_name_plural = 'Object Detection and Classification Workflows'

        db_table = 'H1stAI_ObjectDetectionAndClassificationWorkflow'

        default_related_name = 'obj_detect_classify_workflows'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create Workflow structure if all attributes have been initialized
        if hasattr(self, 'object_detector') and \
                hasattr(self, 'object_classifier'):
            self.start() \
                .add(self.object_detector) \
                .add(self.object_classifier)

            self.end()

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}: ' \
               f'Object Detector = {self.object_detector}; ' \
               f'Object Classifier = {self.object_classifier}'
