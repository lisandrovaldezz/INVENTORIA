from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombreCategoria: str

class CategoriaDB(CategoriaBase):
    class Config:
        from_attributes = True