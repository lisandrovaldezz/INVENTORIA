from sqlalchemy.orm import Session
from model.lista import Lista
from schemas.lista import ListaBase,ListaDB
from fastapi import HTTPException


def agregarAnime(db: Session, lista: ListaBase):
    db_lista = db.query(Lista).filter(
        Lista.id_usuario == lista.id_usuario,
        Lista.id_anime == lista.id_anime
    ).first()
    if db_lista:
        return db_lista
    
    nuevoAnime = Lista(
        id_usuario=lista.id_usuario, 
        id_anime=lista.id_anime,
        visto=lista.visto
    )
    db.add(nuevoAnime)
    db.commit()
    db.refresh(nuevoAnime)
    return nuevoAnime

def quitarAnime(db: Session, id_usuario: int, id_anime: int):
    db_lista = db.query(Lista).filter(
        Lista.id_usuario == id_usuario,
        Lista.id_anime == id_anime
    ).first()
    
    if db_lista:
        db.delete(db_lista)
        db.commit()
        return db_lista
    return None

def verLista(db: Session, id_usuario: int):
    return db.query(Lista).filter(Lista.id_usuario == id_usuario).all()
