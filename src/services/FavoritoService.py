import webbrowser
from src.models.Favorito import Favorito
from src.repositories import FavoritoRepository


def abrir(url: str):
    try:
        webbrowser.open(url)
    except:
        raise Exception(f"Impossível abrir {url}.")

def atualizar(favorito: Favorito):
    FavoritoRepository.atualizar(favorito)

def excluir(id: int):
    FavoritoRepository.excluir(id)

def inserir(favorito: Favorito):
    FavoritoRepository.inserir(favorito)

def listar():
    return FavoritoRepository.listar()

def procurar(id: int):
    return FavoritoRepository.procurar(id)