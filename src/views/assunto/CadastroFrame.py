import tkinter as tk

from src.controllers import AssuntoController
from src.models.Assunto import Assunto
from src.views.Frame import Frame as MyFrame


class CadastroFrame:
    def __init__(self, frame: MyFrame):
        self._my_frame = frame
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._titulo_label = tk.Label(
            self._panel,
            text="Cadastro de Assunto",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size * 2)
        )
        self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

        self._nome_panel = tk.Frame(self._panel)
        self._nome_panel.configure(bg=frame.background)
        self._nome_panel.grid(row=1, column=0, padx=16, pady=16)

        self._nome_label = tk.Label(
            self._nome_panel,
            text="Nome",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._nome_label.grid(row=0, column=0, padx=16, pady=16)

        self._nome_entry = tk.Entry(self._nome_panel, font=(frame.font_family, frame.font_size))
        self._nome_entry.grid(row=0, column=1, padx=16, pady=16)

        self._button = tk.Button(
            self._panel,
            text="Inserir",
            command=self._inserir,
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._button.grid(row=2, column=0, padx=16, pady=16)
        self._button.bind("<Return>", self._inserir)

        self._my_frame.manter_aberto()
    

    def _inserir(self, event = None) -> None:
        AssuntoController.inserir(self._my_frame, Assunto(self._nome_entry.get()))