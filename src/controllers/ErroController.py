from src.views.Frame import Frame as MyFrame


def mostrar(frame: MyFrame, mensagem: str) -> None:
    from src.views.ErroFrame import ErroFrame
    ErroFrame(frame, mensagem)