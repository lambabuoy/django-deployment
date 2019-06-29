from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from .models import Post
from django.db import utils


class IndexView(TemplateView):
    template_name = 'index.html'


class MovieListView(ListView):
    model = models.Movie


class MovieDetailView(DetailView):
    context_object_name = 'movie_detail'
    model = models.Movie
    template_name = 'basic_app/movie_details.html'


class MovieCreateView(CreateView):
    fields = ('title', 'plot', 'director', 'length', 'released_year', 'covers')
    model = models.Movie


class MovieUpdateView(UpdateView):
    fields = ('title', 'plot', 'director', 'length', 'released_year', 'covers')
    model = models.Movie


class MovieDeleteView(DeleteView):
    model = models.Movie
    success_url = reverse_lazy("basic_app:list")


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title'])
        posts = Post.objects.filter(entry_query).order_by('created')
        return render(request, 'search.html', {'query_string': query_string, 'posts': posts})
    else:
        return render(request, 'search.html', {'query_string': 'Null', 'found_entries': 'Enter a search term'})
