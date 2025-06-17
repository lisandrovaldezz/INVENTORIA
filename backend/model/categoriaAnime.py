from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class CategoriaAnime(Base):
    __tablename__ = "categorias_animes"
    
    id_anime = Column(Integer, ForeignKey("animes.id_anime"), primary_key=True)
    nombreCategoria = Column(String, ForeignKey("categorias.nombreCategoria"), primary_key=True)
    
    anime = relationship("Anime", back_populates="categorias_animes")
    categoria = relationship("Categoria", back_populates="categorias_animes")
