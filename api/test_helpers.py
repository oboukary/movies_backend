# %%
from database import sessionLocal
import helpers

# Créer une session
db = sessionLocal()

# %%
# Tester la récupération de films
movies = helpers.get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()