from django.contrib import admin

from .workflow import IntrusionDetectionWorkflow


admin.site.register([
    IntrusionDetectionWorkflow,
])
