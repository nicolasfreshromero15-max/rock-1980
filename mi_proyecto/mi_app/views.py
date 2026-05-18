from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artista, Banda, Cancion

# === CRUD ARTISTA ===
class ArtistaListView(ListView):
    model = Artista
    template_name = 'mi_app/artista_list.html'
    context_object_name = 'artistas'

class ArtistaCreateView(CreateView):
    model = Artista
    template_name = 'mi_app/artista_form.html'
    fields = ['nombre', 'bandas_donde_participo', 'genero_principal']
    success_url = reverse_lazy('artista_list')
    
class ArtistaUpdateView(UpdateView):
    model = Artista
    template_name = 'mi_app/artista_form.html'
    fields = ['nombre', 'bandas_donde_participo', 'genero_principal']
    success_url = reverse_lazy('artista_list')

class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'mi_app/artista_confirm_delete.html'
    success_url = reverse_lazy('artista_list')

# === CRUD BANDA ===
class BandaListView(ListView):
    model = Banda
    template_name = 'mi_app/banda_list.html'
    context_object_name = 'bandas'

class BandaCreateView(CreateView):
    model = Banda
    template_name = 'mi_app/banda_form.html'
    fields = ['nombre', 'genero_principal']
    success_url = reverse_lazy('banda_list')

class BandaUpdateView(UpdateView):
    model = Banda
    template_name = 'mi_app/banda_form.html'
    fields = ['nombre', 'genero_principal']
    success_url = reverse_lazy('banda_list')

class BandaDeleteView(DeleteView):
    model = Banda
    template_name = 'mi_app/banda_confirm_delete.html'
    success_url = reverse_lazy('banda_list')

# === CRUD CANCION ===
class CancionListView(ListView):
    model = Cancion
    template_name = 'mi_app/cancion_list.html'
    context_object_name = 'canciones'

class CancionCreateView(CreateView):
    model = Cancion
    template_name = 'mi_app/cancion_form.html'
    fields = ['titulo', 'anio_lanzamiento']
    success_url = reverse_lazy('cancion_list')

class CancionUpdateView(UpdateView):
    model = Cancion
    template_name = 'mi_app/cancion_form.html'
    fields = ['titulo', 'anio_lanzamiento']
    success_url = reverse_lazy('cancion_list')

class CancionDeleteView(DeleteView):
    model = Cancion
    template_name = 'mi_app/cancion_confirm_delete.html'
    success_url = reverse_lazy('cancion_list')
