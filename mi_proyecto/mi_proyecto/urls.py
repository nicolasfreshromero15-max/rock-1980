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
from django.contrib.auth import views as auth_views
from django.urls import path
from mi_app.views import HomeView
from mi_app.views import (RegisterView,
ArtistaListView, ArtistaCreateView, ArtistaUpdateView, 
 ArtistaDeleteView, BandaListView, BandaCreateView, BandaUpdateView, BandaDeleteView,
CancionListView, CancionCreateView, CancionUpdateView, CancionDeleteView
)

urlpatterns = [
    # Registro de usuarios
    path('register/', RegisterView.as_view(), name='register'),
    # Página de inicio
    path ('', HomeView.as_view(), name='home'), 
    path('admin/', admin.site.urls),
    # Artistas
    path('artistas/', ArtistaListView.as_view(), name='artista_list'),
    path('artistas/nuevo/', ArtistaCreateView.as_view(), name='artista_create'),
    path('artistas/editar/<int:pk>/', ArtistaUpdateView.as_view(), name='artista_update'),
    path('artistas/borrar/<int:pk>/', ArtistaDeleteView.as_view(), name='artista_delete'),
    # Bandas
    path('bandas/', BandaListView.as_view(), name='banda_list'),
    path('bandas/nuevo/', BandaCreateView.as_view(), name='banda_create'),
    path('bandas/editar/<int:pk>/', BandaUpdateView.as_view(), name='banda_update'),
    path('bandas/borrar/<int:pk>/', BandaDeleteView.as_view(), name='banda_delete'),

    # Canciones
    path('canciones/', CancionListView.as_view(), name='cancion_list'),
    path('canciones/nuevo/', CancionCreateView.as_view(), name='cancion_create'),
    path('canciones/editar/<int:pk>/', CancionUpdateView.as_view(), name='cancion_update'),
    path('canciones/borrar/<int:pk>/', CancionDeleteView.as_view(), name='cancion_delete'),

    # Login (Inicio de sesión)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout (Cierre de sesión)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

