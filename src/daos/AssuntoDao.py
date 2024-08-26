from src.daos.connection import con
from src.models.Assunto import Assunto


def listar() -> list[Assunto]:
    assuntos: list[Assunto] = []
    with con:
        cur = con.execute("SELECT * FROM assuntos ORDER BY nome")
        result = cur.fetchall()
        for row in result:
            assuntos.append(Assunto(row[1], row[0]))
    return assuntos


def ha_com_nome(nome: str) -> bool:
    with con:
        data = [nome]
        cur = con.execute("SELECT * FROM assuntos WHERE nome = ? LIMIT 1", data)
        if cur.fetchone():
            return True
    return False


def inserir(assunto: Assunto) -> None:
    with con:
        data = [assunto.nome]
        con.execute("INSERT INTO assuntos (nome) VALUES (?)", data)
        con.commit()


def atualizar(assunto: Assunto) -> None:
    with con:
        data = [assunto.nome, assunto.id]
        con.execute("UPDATE assuntos SET nome = ? WHERE id = ?", data)
        con.commit()


def excluir(id: int) -> None:
    with con:
        con.execute("DELETE FROM assuntos WHERE id = ?", (id,))
        con.commit()