"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
        # Incluye las URLs de cada aplicación
    path('calidad/', include('calidad.urls')),
    path('modelos/', include('modelos.urls')),
    path('operativos/', include('operativos.urls')),
    path('seguridad/', include('seguridad.urls')),
    path('tareas/', include('tareas.urls')),
    path('tarjetas_control/', include('tarjetas_control.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('servicios/', include('servicios.urls')),
    path('planner/', include('planner.urls')),
    path('procesos/', include('procesos.urls')),
    path('bugs/', include('bugs.urls')),
    path("select2/", include("django_select2.urls")),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = '/home/'
