from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    profile_image = Column(String, nullable=True)
    admin = Column(Boolean, default=False)
    fecha_creacion = Column(Date, default=date.today)
    
    listas = relationship("Lista", back_populates="usuarios")