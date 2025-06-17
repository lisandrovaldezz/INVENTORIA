from sqlalchemy.orm import Session
from model.usuarios import Usuario
from schemas.usuarios import UsuarioBase,UsuarioDB
from fastapi import HTTPException
#from auth.auth import get_password_hash


def crearUsuario(db:Session,  usuario: UsuarioBase):
    if(usuario.username==""):
        raise HTTPException(status_code=400, detail="El username no puede estar vacío")
    existente = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    
    nueva_cuenta = Usuario(
        username=usuario.username,
        password=usuario.password
    )

    db.add(nueva_cuenta)
    db.commit()
    db.refresh(nueva_cuenta)
    return nueva_cuenta

def getUsuarios(db:Session,skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def getUsuarioByUsername(db:Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()