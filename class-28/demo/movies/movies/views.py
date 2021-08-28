from django.shortcuts import render
from .models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie

class MovieCreateView(CreateView):
    template_name = 'movie_create.html'
    model = Movie
    fields = ['name', 'description', 'owner']
    success_url = reverse_lazy('list_view')

class MovieUpdateView(UpdateView):
    template_name = 'movie_update.html'
    model = Movie
    fields = ['name', 'description', 'owner']

class MovieDeleteView(DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('list_view')
