from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioBase(BaseModel):
    id: int
    username: str
    password: str
    profile_image: Optional[str] = None
    admin: bool
    email: str
    fecha_creacion: date

class UsuarioDB(UsuarioBase):
    class Config:
        from_attributes = True
        orm_mode = True

class LoginResponse(BaseModel): 
    username: str

class LoginRequest(BaseModel):
    username: str    
    password: str

class UsuarioCreate(BaseModel):
    email: str
    username: str
    password: str