from fastapi import FastAPI
from routers import usuarios, animes,categoria,categoriaAnime,lista
#from auth import auth
from database import Base, engine
from model.animes import Anime
from model.categoria import Categoria
from model.categoriaAnime import CategoriaAnime
from model.lista import Lista
from model.usuarios import Usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



def startup():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)

app.add_event_handler("startup", startup)




app.include_router(usuarios.router,tags=["Usuarios"])
app.include_router(animes.router,tags=["Animes"])
app.include_router(categoria.router,tags=["Categorias"])
app.include_router(categoriaAnime.router,tags=["CategoriasAnimes"])
app.include_router(lista.router,tags=["Listas"])
#app.include_router(auth.router,tags=["Autenticación"])

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)