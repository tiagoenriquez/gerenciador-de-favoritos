from src.daos.connection import con
from src.models.Favorito import Favorito


def listar(assunto_id: int) -> list[Favorito]:
    favoritos: list[Favorito] = []
    with con:
        data = [assunto_id]
        cur = con.execute("SELECT * FROM favoritos WHERE assunto_id = ? ORDER BY nome", data)
        result = cur.fetchall()
        for row in result:
            favoritos.append(Favorito(row[1], row[2], row[3], id=row[0]))
    return favoritos


def ha_com_nome(favorito: Favorito) -> bool:
    with con:
        data = [favorito.nome]
        cur = con.execute("SELECT * FROM favoritos WHERE nome = ? LIMIT 1", data)
        result = cur.fetchone()
        if result != None and result[0] != favorito.id:
            return True
    return False


def ha_com_url(favorito: Favorito) -> bool:
    with con:
        data = [favorito.url]
        cur = con.execute("SELECT * FROM favoritos WHERE url = ? LIMIT 1", data)
        result = cur.fetchone()
        if result != None and result[0] != favorito.id:
            return True
    return False


def inserir(favorito: Favorito) -> None:
    with con:
        data = [favorito.nome, favorito.url, favorito.assunto_id]
        con.execute("INSERT INTO favoritos (nome, url, assunto_id) VALUES (?, ?, ?)", data)
        con.commit()


def atualizar(favorito: Favorito) -> None:
    with con:
        data = [favorito.nome, favorito.url, favorito.assunto_id, favorito.id]
        con.execute("UPDATE favoritos SET nome = ?, url = ?, assunto_id = ? WHERE id = ?", data)
        con.commit()


def excluir(id: int) -> None:
    with con:
        data = [id]
        con.execute("DELETE FROM favoritos WHERE id = ?", data)
        con.commit()


def excluir_por_assunto(assunto_id: int) -> None:
    with con:
        data = [assunto_id]
        con.execute("DELETE FROM favoritos WHERE assunto_id = ?", data)