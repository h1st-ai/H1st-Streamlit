from django.urls.conf import include, path

from rest_framework.routers import DefaultRouter


ROUTER = DefaultRouter()


urlpatterns = [
    path('', include(ROUTER.urls))
]
