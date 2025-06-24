from sqlalchemy.orm import Session
from model.usuarios import Usuario
from schemas.usuarios import UsuarioBase,UsuarioDB
from fastapi import HTTPException
#from auth.auth import get_password_hash


def crearUsuario(db:Session,  usuario: UsuarioBase):
    
    nueva_cuenta = Usuario(
        email=usuario.email,
        username=usuario.username,
        password=usuario.password
    )

    db.add(nueva_cuenta)
    db.commit()
    db.refresh(nueva_cuenta)
    return nueva_cuenta

def getUsuarios(db:Session):
    return db.query(Usuario).all()

def getUsuarioByUsername(db:Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()

def getUsuarioByEmail(db:Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

