from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.usuarios import Usuario
from database import get_db
from crud.usuarios_crud import (crearUsuario,getUsuarios,getUsuarioByUsername)
from schemas.usuarios import (UsuarioBase,UsuarioDB,UsuarioCreate,LoginRequest,LoginResponse)
from fastapi.responses import JSONResponse
from auth.auth import create_access_token,hash_password,verify_password
from datetime import timedelta

router = APIRouter()

@router.get("/Ver_usuarios", response_model=list[UsuarioDB])
def get_usuarios(db: Session = Depends(get_db)):
    return getUsuarios(db)

@router.post("/register/", response_model=dict)
def register_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if getUsuarioByUsername(db, usuario.username):
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    if len(usuario.password) < 8:
        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 8 caracteres")
    
    if not any(char.isdigit() for char in usuario.password):
        raise HTTPException(status_code=400, detail="La contraseña debe contener al menos un número")
    
    if not any(char.isupper() for char in usuario.password):
        raise HTTPException(status_code=400, detail="La contraseña debe contener al menos una letra mayúscula")
    
    usuario.password = hash_password(usuario.password)
    nueva_cuenta = crearUsuario(db, usuario)
    return {"message": f"Usuario {nueva_cuenta.username} registrado exitosamente"}

@router.post("/login/")
async def login_usuario(form: LoginRequest, db: Session = Depends(get_db)):
    db_usuario = getUsuarioByUsername(db, form.username)

    if not db_usuario:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if not (verify_password(form.password, db_usuario.password)):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    access_token = create_access_token(
        data={"sub": form.username}, 
        expires_delta=timedelta(minutes=43200)
    )
    
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"})

