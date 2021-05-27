from django.urls.conf import include, path

from rest_framework.routers import DefaultRouter

from .views import FirstModelAPIView


ROUTER = DefaultRouter()


urlpatterns = [
    path('', include(ROUTER.urls)),
    path('first-model/', FirstModelAPIView.as_view())
]
