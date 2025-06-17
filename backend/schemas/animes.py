from pydantic import BaseModel
from typing import Optional

class AnimeBase(BaseModel):
    nombre: str
    imagen: str

class AnimeDB(AnimeBase):
    class Config:
        from_attributes = True