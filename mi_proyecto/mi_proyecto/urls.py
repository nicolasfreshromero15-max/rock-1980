"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path

from mi_proyecto.mi_app.views import ArtistaListView, ArtistaCreateView, ArtistaUpdateView, ArtistaDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artistas/', ArtistaListView.as_view(), name='artista_list'),
    path('artistas/nuevo/', ArtistaCreateView.as_view(), name='artista_create'),
    path('artistas/editar/<int:pk>/', ArtistaUpdateView.as_view(), name='artista_update'),
    path('artistas/borrar/<int:pk>/', ArtistaDeleteView.as_view(), name='artista_delete'),
]
