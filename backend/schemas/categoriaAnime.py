from pydantic import BaseModel

class CategoriaAnimeBase(BaseModel):
    id_anime: int
    nombreCategoria: str

class CategoriaAnimeDB(CategoriaAnimeBase):
    class Config:
        from_attributes = True