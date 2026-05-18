from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artista

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
