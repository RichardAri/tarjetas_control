from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index_planner, name='index_planner'),
    path('tarjetas/', views.ver_tarjetas_diarias, name='ver_tarjetas_diarias'),
    
]
