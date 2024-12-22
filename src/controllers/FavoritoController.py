from src.views.Frame import Frame as MyFrame


def cadastrar(frame: MyFrame):
    from src.views.CadastroFrame import CadastroFrame
    CadastroFrame(frame)