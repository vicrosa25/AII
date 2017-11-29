# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Genre, Movie

# Create your views here.
def index(request):
    """ 
    Lógica para crear el index con el menú de la web
    """
    return render(request, 'films/index.html')
    


def genres(request):
    """ 
    Lógica para crear la vista con todos los géneros 
    """
    context = {
        'all_genres': Genre.objects.all(),
    }
    return render(request, 'films/genres.html', context)

def movies(request):
    """ 
    Lógica para crear la vista que muestra todas la películas 
    """
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'films/movies.html', context)

def moviesByGenre(request):
    """
    Lógica para crear la vista que muestra todas las películas
    agrupadas por género.
    """
    context = {
        'genres': Genre.objects.all(),
    }
    return render(request, 'films/moviesbygenres.html', context)