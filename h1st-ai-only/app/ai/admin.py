from django.contrib import admin

from .workflow import MyWorkflow
from .models.my_model import MyModel


admin.site.register([MyWorkflow, MyModel])
