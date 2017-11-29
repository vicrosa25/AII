from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^genres/', views.genres, name='genres'),
    url(r'^movies/', views.movies, name='movies'),
    url(r'^moviesbygenres/', views.moviesByGenre, name='moviesbygenre')
]
