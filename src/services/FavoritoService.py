from src.models.Favorito import Favorito
from src.repositories import FavoritoRepository


def inserir(favorito: Favorito):
    FavoritoRepository.inserir(favorito)