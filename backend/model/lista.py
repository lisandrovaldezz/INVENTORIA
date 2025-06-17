from sqlalchemy import Column, Integer,ForeignKey,Boolean
from database import Base
from sqlalchemy.orm import relationship

class Lista(Base):
    __tablename__ = "listas"
    
    visto = Column(Boolean, default=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    id_anime = Column(Integer, ForeignKey("animes.id_anime"), primary_key=True)
    
    usuarios = relationship("Usuario", back_populates="listas")
    anime = relationship("Anime", back_populates="listas")
