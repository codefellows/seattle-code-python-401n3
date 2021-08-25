from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movies

# Create your views here.

class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movies
    context_object_name = 'sw_movies'

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movies