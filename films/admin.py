# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie, Genre, Tag, Rating

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Rating)
