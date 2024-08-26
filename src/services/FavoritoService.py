import webbrowser

from src.daos import FavoritoDao
from src.models.Favorito import Favorito


def listar(assunto_id: int) -> list[Favorito]:
    return FavoritoDao.listar(assunto_id)


def inserir(favorito: Favorito) -> None:
    if FavoritoDao.ha_com_nome(favorito):
        raise Exception(f"Já existe favorito com o nome {favorito.nome}.")
    if FavoritoDao.ha_com_url(favorito):
        raise Exception(f"Já existe favorito com a URL {favorito.url}.")
    FavoritoDao.inserir(favorito)


def abrir(url: str) -> None:
    try:
        webbrowser.open(url)
    except Exception as exception:
        raise Exception(f"Impossível abrir {url} no navegador.")


def atualizar(favorito: Favorito) -> None:
    if FavoritoDao.ha_com_nome(favorito):
        raise Exception(f"Já existe favorito com o nome {favorito.nome}.")
    if FavoritoDao.ha_com_url(favorito):
        raise Exception(f"Já existe favorito com a URL {favorito.url}.")
    FavoritoDao.atualizar(favorito)


def excluir(id: int) -> None:
    FavoritoDao.excluir(id)