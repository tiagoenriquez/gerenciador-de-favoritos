import tkinter as tk
from tkinter import ttk

from src.controllers import FavoritoController
from src.models.Assunto import Assunto
from src.models.Favorito import Favorito
from src.views.Frame import Frame as MyFrame


class EdicaoFrame:
    def __init__(self, frame: MyFrame, favorito: Favorito, assuntos: list[Assunto]) -> None:
        self._my_frame = frame
        self._favorito = favorito
        self._assuntos = assuntos
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._titulo_label = tk.Label(
            self._panel,
            text="Cadastro de Favorito",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size * 2)
        )
        self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

        self._assunto_panel = tk.Frame(self._panel)
        self._assunto_panel.configure(bg=frame.background)
        self._assunto_panel.grid(row=1, column=0, padx=16, pady=16)

        self._assunto_label = tk.Label(
            self._assunto_panel,
            text="Assunto",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._assunto_label.grid(row=0, column=0, padx=16, pady=16)

        self._assuntos_combobox = ttk.Combobox(
            self._assunto_panel,
            values=[(assunto.nome) for assunto in assuntos]
        )
        self._assuntos_combobox.configure(font=(frame.font_family, frame.font_size))
        self._assuntos_combobox.grid(row=0, column=1, padx=16, pady=16)
        self._assuntos_combobox.set(favorito.assunto.nome)

        self._nome_panel = tk.Frame(self._panel)
        self._nome_panel.configure(bg=frame.background)
        self._nome_panel.grid(row=2, column=0, padx=16, pady=16)

        self._nome_label = tk.Label(
            self._nome_panel,
            text="Nome",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._nome_label.grid(row=0, column=0, padx=16, pady=16)

        self._nome_entry = tk.Entry(self._nome_panel, font=(frame.font_family, frame.font_size))
        self._nome_entry.insert(0, favorito.nome)
        self._nome_entry.grid(row=0, column=1, padx=16, pady=16)

        self._url_panel = tk.Frame(self._panel)
        self._url_panel.configure(bg=frame.background)
        self._url_panel.grid(row=3, column=0, padx=16, pady=16)

        self._url_label = tk.Label(
            self._url_panel,
            text="URL",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._url_label.grid(row=0, column=0, padx=16, pady=16)

        self._url_entry = tk.Entry(self._url_panel, font=(frame.font_family, frame.font_size))
        self._url_entry.insert(0, favorito.url)
        self._url_entry.grid(row=0, column=1, padx=16, pady=16)

        self._button = tk.Button(
            self._panel,
            text="Atualizar",
            command=self._atualizar,
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._button.grid(row=4, column=0, padx=16, pady=16)
        self._button.bind("<Return>", self._atualizar)

        self._my_frame.manter_aberto()


    def _atualizar(self, event = None) -> None:
        assunto_atualizado = self._favorito.assunto
        for assunto in self._assuntos:
            if self._assuntos_combobox.get() == assunto.nome:
                assunto_atualizado = assunto
                break
        FavoritoController.atualizar(self._my_frame, Favorito(
            self._nome_entry.get(),
            self._url_entry.get(),
            assunto_atualizado.id,
            assunto_atualizado,
            self._favorito.id
        ))