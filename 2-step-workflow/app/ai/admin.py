from django.contrib import admin

from .workflow import MyWorkflow
from .models.step1_models.my_step1_model import MyStep1Model
from .models.step2_models.my_step2_model import MyStep2Model


admin.site.register([
    MyWorkflow,
    MyStep1Model, MyStep2Model
])
