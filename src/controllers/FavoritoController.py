from src.controllers import AssuntoController
from src.controllers import ErroController
from src.models.Assunto import Assunto
from src.models.Favorito import Favorito
from src.services import AssuntoService
from src.services import FavoritoService
from src.views.Frame import Frame as MyFrame


def listar(frame: MyFrame, assunto: Assunto) -> None:
    from src.views.favorito.DoAssuntoFrame import DoAssuntoFrame
    try:
        DoAssuntoFrame(frame, FavoritoService.listar(assunto.id), assunto)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def cadastrar(frame: MyFrame, assunto: Assunto) -> None:
    from src.views.favorito.CadastroFrame import CadastroFrame
    CadastroFrame(frame, assunto)


def inserir(frame: MyFrame, favorito: Favorito) -> None:
    try:
        FavoritoService.inserir(favorito)
        AssuntoController.abrir_seletor(frame)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def abrir(url: str) -> None:
    FavoritoService.abrir(url)


def editar(frame: MyFrame, favorito: Favorito) -> None:
    from src.views.favorito.EdicaoFrame import EdicaoFrame
    try:
        EdicaoFrame(frame, favorito, AssuntoService.listar())
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def atualizar(frame: MyFrame, favorito: Favorito) -> None:
    try:
        FavoritoService.atualizar(favorito)
        listar(frame, favorito.assunto)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def ameacar(frame: MyFrame, favorito: Favorito) -> None:
    from src.views.favorito.AmeacaFrame import AmeacaFrame
    AmeacaFrame(frame, favorito)


def excluir(frame: MyFrame, favorito: Favorito) -> None:
    try:
        FavoritoService.excluir(favorito.id)
        listar(frame, favorito.assunto)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])