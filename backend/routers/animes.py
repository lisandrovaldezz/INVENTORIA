from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from model.animes import Anime
from schemas.animes import AnimeBase,AnimeDB
from crud.animes_crud import (crearAnime,getAnimes)
from database import get_db

router = APIRouter()

@router.get("/animes/", response_model=list[AnimeDB])
def get_animes(db: Session = Depends(get_db)):
    return getAnimes(db)

@router.post("/animes/",response_model=AnimeBase)
def crear_anime(anime: AnimeBase,db: Session = Depends(get_db)):
    return crearAnime(db,anime)

