from src.models.Favorito import Favorito
from src.services import FavoritoService
from src.views.Frame import Frame


def atualizar(frame: Frame, favorito: Favorito):
    try:
        FavoritoService.atualizar(favorito)
        listar(frame)
    except Exception as e:
        mostrar_erro(frame, e.args[0])

def cadastrar(frame: Frame):
    from src.views.CadastroFrame import CadastroFrame
    CadastroFrame(frame)

def editar(frame: Frame, id: int):
    from src.views.EdicaoFrame import EdicaoFrame
    EdicaoFrame(frame, FavoritoService.procurar(id))

def inserir(frame: Frame, favorito: Favorito):
    try:
        FavoritoService.inserir(favorito)
        listar(frame)
    except Exception as e:
        mostrar_erro(frame, e.args[0])

def listar(frame: Frame):
    from src.views.ListaFrame import ListaFrame
    ListaFrame(frame, FavoritoService.listar())
        
def mostrar_erro(frame: Frame, erro: str):
    from src.views.ErroFrame import ErroFrame
    ErroFrame(frame, erro)