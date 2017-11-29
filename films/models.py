# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Movie(models.Model):
    movieID     = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=120)
    genres      = models.ManyToManyField("Genre", related_name='movies')
    imdbId       = models.IntegerField(null=True, blank=True)
    tmdbId      = models.IntegerField(null=True, blank=True)

    def list_of_genres(self):
        """
        Devuelve un string con todos los géneros de la película
        separados por comas.
        """
        return ", ".join([genre.name for genre in self.genres.all()])

    
    def __unicode__(self):
        """
        Es el toStrint() de Django
        """
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    content = models.TextField()
    movie   = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __unicode__(self): 
        return self.content

class Rating(models.Model):
    rate    = models.DecimalField(max_digits=2, decimal_places=1)
    movie   = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.rate)

