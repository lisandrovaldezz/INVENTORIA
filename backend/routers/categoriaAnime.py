from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.categoriaAnime import CategoriaAnime
from schemas.categoriaAnime import (CategoriaAnimeBase,CategoriaAnimeDB)
from crud.categoriaAnime_crud import agregarCategoriaAnime, verCategoriaAnime, quitarCategoriaAnime
from database import get_db

router = APIRouter()

@router.post("/categoriaAnime", response_model=CategoriaAnimeDB)
def addCategoriaAnime(categoriaAnime: CategoriaAnimeBase, db: Session = Depends(get_db)):
    return agregarCategoriaAnime(db, categoriaAnime)

@router.delete("/categoriaAnime", response_model=dict)
def eliminarCategoriaAnime(nombreCategoria: str, id_anime: int, db: Session = Depends(get_db)):
    categoriaAnime = quitarCategoriaAnime(db, nombreCategoria, id_anime)
    if not categoriaAnime:
        raise HTTPException(status_code=404, detail=f"No se encontró la relación entre la categoría '{nombreCategoria}' y el anime con ID {id_anime}")
    return {"msg": "Relación eliminada exitosamente"}


@router.get("/categoriaAnime/{nombreCategoria}", response_model=list[CategoriaAnimeDB])
def getCategoriaAnime(nombreCategoria: str, db: Session = Depends(get_db)):
    return verCategoriaAnime(db, nombreCategoria)