from sqlalchemy.orm import Session
from model.categoriaAnime import CategoriaAnime
from schemas.categoriaAnime import CategoriaAnimeBase,CategoriaAnimeDB
from model.animes import Anime
from model.categoria import Categoria
from fastapi import HTTPException


def agregarCategoriaAnime(db: Session, categoriaAnime: CategoriaAnimeBase):
    # Verificar si la categoría existe
    categoria = db.query(Categoria).filter(Categoria.nombreCategoria == categoriaAnime.nombreCategoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoría no existe")

    # Verificar si el anime existe
    anime = db.query(Anime).filter(Anime.id_anime == categoriaAnime.id_anime).first()
    if not anime:
        raise HTTPException(status_code=404, detail="El anime no existe")

    # Verificar si ya existe la relación
    db_categoriaAnime = db.query(CategoriaAnime).filter(
        CategoriaAnime.nombreCategoria == categoriaAnime.nombreCategoria,
        CategoriaAnime.id_anime == categoriaAnime.id_anime
    ).first()

    if db_categoriaAnime:
        return db_categoriaAnime  # Ya existe, devolver el objeto existente

    # Crear la nueva relación
    nuevaCategoriaAnime = CategoriaAnime(
        nombreCategoria=categoriaAnime.nombreCategoria,
        id_anime=categoriaAnime.id_anime
    )
    db.add(nuevaCategoriaAnime)
    db.commit()
    db.refresh(nuevaCategoriaAnime)
    return nuevaCategoriaAnime


def quitarCategoriaAnime(db: Session, nombreCategoria: str, id_anime: int):
    db_categoriaAnime = db.query(CategoriaAnime).filter(
        CategoriaAnime.nombreCategoria == nombreCategoria,
        CategoriaAnime.id_anime == id_anime
    ).first()
    
    if db_categoriaAnime:
        db.delete(db_categoriaAnime)
        db.commit()
        return db_categoriaAnime
    return None

def verCategoriaAnime(db: Session, nombreCategoria: str):
    relaciones = db.query(CategoriaAnime).filter(CategoriaAnime.nombreCategoria == nombreCategoria).all()
    if not relaciones:
        raise HTTPException(status_code=404, detail=f"No se encontraron animes para la categoría '{nombreCategoria}'")
    return relaciones