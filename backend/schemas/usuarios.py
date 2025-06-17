from pydantic import BaseModel

class UsuarioBase(BaseModel):
    id: int
    username: str
    password: str

class UsuarioDB(UsuarioBase):
    class Config:
        from_attributes = True

class LoginResponse(BaseModel): 
    username: str

class LoginRequest(BaseModel):
    username: str    
    password: str

class UsuarioCreate(BaseModel):
    username: str
    password: str