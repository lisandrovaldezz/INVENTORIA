from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.lista import Lista
from schemas.lista import ListaBase, ListaDB
from crud.lista_crud import agregarAnime, verLista, quitarAnime
from database import get_db

router = APIRouter()

@router.post("/listas", response_model=ListaDB)
def agregar_anime(lista: ListaBase, db: Session = Depends(get_db)):
    return agregarAnime(db, lista)

@router.delete("/listas", response_model=dict)
def quitar_anime(id_usuario: int, id_anime: int, db: Session = Depends(get_db)):
    lista = quitarAnime(db, id_usuario, id_anime)
    if lista is None:
        raise HTTPException(status_code=404, detail="Anime no encontrado en la lista")
    return {"msg": "Anime eliminado de la lista"}

@router.get("/listas/{id_usuario}", response_model=list[ListaDB])
def ver_lista(id_usuario: int, db: Session = Depends(get_db)):
    return verLista(db, id_usuario)
