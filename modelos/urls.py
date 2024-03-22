from django.urls import path
from .views import vista_simple

urlpatterns = [
    path('simple/', vista_simple, name='vista_simple'),
]


