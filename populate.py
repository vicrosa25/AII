import os, csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

import django

django.setup()

from films.models import Movie, Genre, Tag, Rating


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOVIES_DIR = os.path.join(BASE_DIR, 'lab1/data/movies.csv')
TAGS_DIR = os.path.join(BASE_DIR, 'lab1/data/tags.csv')
RATINGS_DIR = os.path.join(BASE_DIR, 'lab1/data/ratings.csv')
LINKS_DIR = os.path.join(BASE_DIR, 'lab1/data/links.csv')   


movies = csv.reader(open(MOVIES_DIR), delimiter=',')
tags = csv.reader(open(TAGS_DIR), delimiter=',')
ratings = csv.reader(open(RATINGS_DIR), delimiter=',')
links = csv.reader(open(LINKS_DIR), delimiter=',')


# for n in range(1, 100): # movieId,title,genres
#     # movie = Movie.objects.create(
#     #     movieID=movies[n][0],
#     #     title=movies[n][1],
#     # )
#     movie = Movie()
#     movie.movieID = movies[n][0]
#     movie.title = movies[n][1]
#     movie.save()
#     genres = movies[n][2].split('|')
#     for g in genres:
#         genre, created = Genre.objects.get_or_create(name=g)
#         if not created:
#             genre.save()
#         movie.genres.add(genre)

# for n in range(1, 100):
#     movie = Movie.objects.get(movieID=links[n][0])
#     # print links[n][1], links[n][2]
#     movie.imdbId = links[n][1]
#     movie.tmdbId = links[n][2]
#     movie.save()
    


for row in movies: # movieId,title,genres
    if row[0] != 'movieId':
        movie = Movie()
        movie.movieID = row[0]
        movie.title = row[1]
        movie.save()
        
        genres = row[2].split('|')
#         for g in genres:
#             genre = addGenre(g)
#             movie.genres.add(genre)
        for g in genres:
            genre, created = Genre.objects.get_or_create(name=g)
            if not created:
                genre.save()
            movie.genres.add(genre)

for row in links: # movieId,imdbId,tmdbId
    if row[0] != 'movieId':
        movie = Movie.objects.get(movieID=row[0])
        if row[1] != '':
            movie.imdbId = row[1]
        if row[2] != '':
            movie.tmdbId = row[2]
        movie.save()


for row in tags: # userId,movieId,tag,timestamp
    if row[0] != 'userId':
        tag = Tag()
        tag.content = row[2]
        tag.movie = Movie.objects.get(movieID=row[1])
        tag.save()

for row in ratings: # userId,movieId,rating,timestamp
    if row[0] != 'userId':
        rating = Rating()
        rating.rate = row[2]
        rating.movie = Movie.objects.get(movieID=row[1])
        rating.save()




            
       

