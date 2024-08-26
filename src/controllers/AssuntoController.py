from src.controllers import ErroController
from src.models.Assunto import Assunto
from src.services import AssuntoService
from src.views.Frame import Frame as MyFrame


def abrir_seletor(frame: MyFrame) -> None:
    from src.views.assunto.SeletorFrame import SeletorFrame
    try :
        SeletorFrame(frame, AssuntoService.listar())
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def cadastrar(frame: MyFrame) -> None:
    from src.views.assunto.CadastroFrame import CadastroFrame
    CadastroFrame(frame)


def inserir(frame: MyFrame, assunto: Assunto) -> None:
    try: 
        AssuntoService.inserir(assunto)
        abrir_seletor(frame)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def editar(frame: MyFrame, assunto: Assunto) -> None:
    from src.views.assunto.EdicaoFrame import EdicaoFrame
    EdicaoFrame(frame, assunto)


def atualizar(frame: MyFrame, assunto: Assunto) -> None:
    try:
        AssuntoService.atualizar(assunto)
        abrir_seletor(frame)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])


def ameacar(frame: MyFrame, assunto: Assunto) -> None:
    from src.views.assunto.AmeacaFrame import AmeacaFrame
    AmeacaFrame(frame, assunto)


def excluir(frame: MyFrame, id: int) -> None:
    try:
        AssuntoService.excluir(id)
        abrir_seletor(frame)
    except Exception as exception:
        ErroController.mostrar(frame, exception.args[0])