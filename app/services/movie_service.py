from app.models.movie_model import Movie
from app.database.connection import SessionLocal


#show all movies
def show_all_movies():
    db = SessionLocal()
    try:
        films = db.query(Movie).all()
        return films
    finally:
        db.close()

# Create a new movie
def create_movie(title: str, year: int, genre: str):
    db = SessionLocal()  # Start a session in the database

    # Try adding a new movie to the database
    try:
        film = Movie(title=title, year=year, genre=genre)
        db.add(film)
        db.commit()
        db.refresh(film)
        return film
    finally:
        db.close()  # Finish the session


# Update a movie
def update_movie(movie_id: int, title: str = None, year: int = None, genre: str = None):
    db = SessionLocal()  # Start a session in the database

    # Try updating a movie in the database
    try:
        film = db.query(Movie).filter(
            Movie.id == movie_id).first()  # Filter the movie by ID and bring up the first one.
        if not film:
            return None
        if title:
            film.title = title
        if year:
            film.year = year
        if genre:
            film.genre = genre
        db.commit()
        db.refresh(film)
        return film
    finally:
        db.close()  # Finish the session


# Search a movie
def get_movie(movie_id: int):
    db = SessionLocal()  # Start a session in the database

    # Search for a movie by ID.
    try:
        return db.query(Movie).filter(Movie.id == movie_id).first()
    finally:
        db.close()


#Delete a movie
def delete_movie(movie_id: int):
    db = SessionLocal()  # Start a session in the database

    # Try deleting a movie from the database
    try:
        film = db.query(Movie).filter(Movie.id == movie_id).first()
        if not film:
            return None
        db.delete(film)
        db.commit()
        return True
    finally:
        db.close()  # Finish the session
