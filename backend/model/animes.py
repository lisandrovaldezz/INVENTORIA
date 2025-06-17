from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Anime(Base): 
    __tablename__ = "animes"
    
    id_anime = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    imagen = Column(String(255), nullable=True)

    listas = relationship("Lista", back_populates="anime")
    categorias_animes = relationship("CategoriaAnime", back_populates="anime")