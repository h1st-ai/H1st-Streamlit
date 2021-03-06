from django.urls.conf import include, path

from rest_framework.routers import DefaultRouter

from .views import MyModelAPIView


ROUTER = DefaultRouter()


urlpatterns = [
    path('', include(ROUTER.urls)),
    path('my-model/', MyModelAPIView.as_view())
]
