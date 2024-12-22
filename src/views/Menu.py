import tkinter as tk
from src.controllers import FavoritoController
from src.views.Frame import Frame


class Menu:
    def __init__(self, frame: Frame):
        self._frame = frame
        window = frame.window
        menu = tk.Menu(window)
        window.config(menu=menu)
        menu.add_command(label="Cadastrar", command=self._cadastrar)

    def _cadastrar(self):
        FavoritoController.cadastrar(self._frame)