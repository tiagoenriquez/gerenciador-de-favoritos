from src.connections.DatabaseConnection import con
from src.models.Favorito import Favorito


def inserir(favorito: Favorito):
    with con:
        con.execute("insert into favoritos (nome, url) values (?, ?)", favorito.data_inserted())
        con.commit()