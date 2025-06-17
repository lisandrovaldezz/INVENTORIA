from sqlalchemy.orm import Session
from model.animes import Anime
from schemas.animes import AnimeBase,AnimeDB
from fastapi import HTTPException


def crearAnime(db:Session,  anime: AnimeBase):
    if(anime.nombre==""):
        raise HTTPException(status_code=400, detail="El nombre del anime no puede estar vacío")
    existente = db.query(Anime).filter(Anime.nombre == anime.nombre).first()
    if existente:
        raise HTTPException(status_code=400, detail="El anime ya existe.")
    db_animes = Anime(**anime.model_dump())
    db.add(db_animes)
    db.commit()
    db.refresh(db_animes)
    return db_animes

def getAnimes(db:Session):
    return db.query(Anime).all()