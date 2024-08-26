import tkinter as tk

from src.controllers import FavoritoController
from src.models.Favorito import Favorito
from src.views.Frame import Frame as MyFrame


class AmeacaFrame:
    def __init__(self, frame: MyFrame, favorito: Favorito) -> None:
        self._my_frame = frame
        self._favorito = favorito
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._titulo_label = tk.Label(
            self._panel,
            text=f"Tem certeza de que deseja excluir o favorito {favorito.nome}?",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size * 2)
        )
        self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

        self._buttons_panel = tk.Frame(self._panel)
        self._buttons_panel.grid(row=1, column=0, padx=16, pady=16)
        self._buttons_panel.configure(bg=frame.background)

        self._nao_button = tk.Button(
            self._buttons_panel,
            text="Não",
            command=self._desistir,
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._nao_button.grid(row=0, column=0, padx=16, pady=16)

        self._sim_button = tk.Button(
            self._buttons_panel,
            text="Sim",
            command=self._excluir,
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._sim_button.grid(row=0, column=1, padx=16, pady=16)
        
        self._my_frame.manter_aberto()
    

    def _desistir(self) -> None:
        FavoritoController.listar(self._my_frame, self._favorito.assunto)
    

    def _excluir(self) -> None:
        FavoritoController.excluir(self._my_frame, self._favorito)