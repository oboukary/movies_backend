# %%
from database import sessionLocal
from models import  Movie, Rating, Tag, Link
# %%
# Test de la connexion à la base de données et récupération des 10 premiers films
db = sessionLocal() # Ouverture de la session
movies = db.query(Movie.movieId, Movie.title, Movie.genres,Rating.rating) \
.join(Rating, Movie.movieId == Rating.movieId) \
.filter(Rating.rating >= 4.0) \
.limit(10) \
.all()  
# %%
# Affichage des résultats
for movie in movies:
    print(f"ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres} , Rating: {movie.rating}")

  # %%
links = db.query(Link).limit(10).all()

# Affichage des résultats
for link in links:
    print(f"Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")
# %%
db.close() # Fermeture de la session

# %%
