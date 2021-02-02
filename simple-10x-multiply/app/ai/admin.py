from django.contrib import admin

from .workflow import MyWorkflow


admin.site.register([MyWorkflow])
