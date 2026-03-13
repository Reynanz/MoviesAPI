from pydantic import BaseModel, ConfigDict


# Movie creation schema
class MovieCreate(BaseModel):
    title: str
    year: int
    genre: str


# Movie update schema
class MovieUpdate(BaseModel):
    title: str | None = None
    year: int | None = None
    genre: str | None = None


# Movie response schema
class MovieResponse(MovieCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
