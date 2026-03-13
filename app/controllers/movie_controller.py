from fastapi import APIRouter, HTTPException, Path
from app.services.movie_service import create_movie, get_movie, update_movie, delete_movie
from app.schemas.movie_schema import MovieCreate, MovieUpdate, MovieResponse

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/", response_model=MovieResponse)
def add_movie(movie: MovieCreate):
    film = create_movie(movie.title, movie.year, movie.genre)
    return film


@router.get("/{movie_id}", response_model=MovieResponse)
def search_movie(movie_id: int = Path(..., description="ID do filme")):
    film = get_movie(movie_id)
    if not film:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return film


@router.put("/{movie_id}", response_model=MovieResponse)
def edit_movie(movie_id: int, movie: MovieUpdate):
    film = update_movie(movie_id, movie.title, movie.year, movie.genre)
    if not film:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return film


@router.delete("/{movie_id}", response_model=dict)
def remove_movie(movie_id: int):
    film = delete_movie(movie_id)
    if not film:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return {"detail": "Filme deletado com sucesso!"}
