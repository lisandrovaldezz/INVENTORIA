from pydantic import BaseModel

class ListaBase(BaseModel):
    id_usuario: int
    id_anime: int
    visto: bool = False

class ListaDB(ListaBase):
    class Config:
        from_attributes = True