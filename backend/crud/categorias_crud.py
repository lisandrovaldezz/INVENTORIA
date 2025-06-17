from sqlalchemy.orm import Session
from model.categoria import Categoria
from schemas.categoria import CategoriaBase
from fastapi import HTTPException


def crearCategoria(db: Session, categoria: CategoriaBase):
    if(categoria.nombreCategoria==""):
        raise HTTPException(status_code=400, detail="La categoria no puede estar vacía")
    existente = db.query(Categoria).filter(Categoria.nombreCategoria == categoria.nombreCategoria).first()
    if existente:
        raise HTTPException(status_code=400, detail="La categoría ya existe.")
    
    nueva_categoria = Categoria(nombreCategoria=categoria.nombreCategoria)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

def getCategorias(db:Session,skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()