from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    nombreCategoria = Column(String, primary_key=True)
    
    categorias_animes = relationship("CategoriaAnime", back_populates="categoria")