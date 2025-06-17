from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from model.categoria import Categoria
from schemas.categoria import (CategoriaBase,CategoriaDB)
from database import get_db
from crud.categorias_crud import (crearCategoria,getCategorias)

router = APIRouter()

@router.get("/Ver_categorias", response_model=list[CategoriaDB])
def get_categorias(db: Session = Depends(get_db)):
    return getCategorias(db)

@router.post("/categorias/", response_model=CategoriaBase)
def crear_categoria(categoria: CategoriaBase,db: Session = Depends(get_db)):
    return crearCategoria(db,categoria)
