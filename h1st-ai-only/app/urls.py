from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    # Home URL redirected to Admin
    path('', RedirectView.as_view(url='admin')),

    # Admin URLs
    path('admin/', admin.site.urls),

    # H1st URLs
    path('h1st/', include('h1st.django.urls'))
]
