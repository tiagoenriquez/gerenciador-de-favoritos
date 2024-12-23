from src.connections.DatabaseConnection import con
from src.models.Favorito import Favorito


def atualizar(favorito: Favorito):
    with con:
        con.execute("update favoritos set nome = ?, url = ? where id = ?", favorito.data_updated())
        con.commit()

def excluir(id: int):
    with con:
        con.execute("delete from favoritos where id = ?", [id])
        con.commit()

def inserir(favorito: Favorito):
    with con:
        con.execute("insert into favoritos (nome, url) values (?, ?)", favorito.data_inserted())
        con.commit()

def listar():
    with con:
        cur = con.cursor()
        cur.execute("select * from favoritos order by nome")
        favoritos: list[Favorito] = []
        [favoritos.append(Favorito(row[1], row[2], row[0])) for row in cur.fetchall()]
        return favoritos

def procurar(id: int):
    with con:
        cur = con.cursor()
        cur.execute("select * from favoritos where id = ?", [id])
        res = cur.fetchone()
        return Favorito(res[1], res[2], res[0])