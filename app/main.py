from fastapi import FastAPI
from app.controllers.movie_controller import router as movie_router
from app.services.movie_service import show_all_movies


app = FastAPI()
app.include_router(movie_router)


@app.get("/")
def all_movies():
    films = show_all_movies()
    return films
