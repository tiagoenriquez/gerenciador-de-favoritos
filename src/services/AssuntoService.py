from src.daos import AssuntoDao, FavoritoDao
from src.models.Assunto import Assunto


def listar() -> list[Assunto]:
    return AssuntoDao.listar()


def inserir(assunto: Assunto) -> None:
    if AssuntoDao.ha_com_nome(assunto.nome):
        raise Exception(f"Já existe assunto com o nome {assunto.nome}.")
    AssuntoDao.inserir(assunto)

def atualizar(assunto: Assunto) -> None:
    if AssuntoDao.ha_com_nome(assunto.nome):
        raise Exception(f"Já existe assunto com o nome {assunto.nome}.")
    AssuntoDao.atualizar(assunto)


def excluir(id: int) -> None:
    FavoritoDao.excluir_por_assunto(id)
    AssuntoDao.excluir(id)