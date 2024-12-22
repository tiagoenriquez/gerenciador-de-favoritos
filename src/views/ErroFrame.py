import tkinter as tk
from src.views.Frame import Frame as MyFrame
from src.views.Menu import Menu


class ErroFrame:
    def __init__(self, frame: MyFrame, erro: str):
        self._frame = frame
        self._frame.limpar()
        window = frame.window
        window.title("Erro")
        Menu(frame)

        panel = tk.Frame(window)
        panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(panel, text=erro)
        label.grid(row=0, column=0, padx=8, pady=8)

        self._frame.manter_aberto()