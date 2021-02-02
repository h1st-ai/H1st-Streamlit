from h1st.django.api import H1stWorkflow, H1stModel

from django.db.models import ForeignKey, PROTECT


class MyWorkflow(H1stWorkflow):
    step1 = \
        ForeignKey(
            verbose_name='Step 1',
            to=H1stModel,
            on_delete=PROTECT,
            related_name='multistep_workflow_step1')

    step2 = \
        ForeignKey(
            verbose_name='Step 2',
            to=H1stModel,
            on_delete=PROTECT,
            related_name='multistep_workflow_step2')

    class Meta:
        verbose_name = '2-Step Workflow'
        verbose_name_plural = '2-Step Workflows'

        db_table = 'H1stAI_MultiStepWorkflow'

        default_related_name = 'multi_step_workflows'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create Workflow structure if all attributes have been initialized
        if hasattr(self, 'step1') and hasattr(self, 'step2'):
            self.start()
            self.add(self.step1)
            self.add(self.step2)
            self.end()

    def __str__(self):
        return f'{type(self).__name__} #{self.uuid}: ' \
               f'Step 1 = {self.step1}; ' \
               f'Step 2 = {self.step2}'
