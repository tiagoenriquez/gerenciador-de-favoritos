from functools import partial
from PIL import ImageTk, Image
import tkinter as tk

from src.controllers import AssuntoController
from src.controllers import FavoritoController
from src.models.Assunto import Assunto
from src.views.Frame import Frame as MyFrame


class SeletorFrame:
    def __init__(self, frame: MyFrame, assuntos: list[Assunto]) -> None:
        self._my_frame = frame
        self._assuntos = assuntos
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        if assuntos:
            self._titulo_label = tk.Label(
                self._panel,
                text="Selecione um Assunto",
                bg=frame.background,
                fg=frame.foreground,
                font=(frame.font_family, frame.font_size * 2)
            )
            self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

            self._canvas = tk.Canvas(
                self._panel,
                highlightthickness=0,
                width=frame.width - 128,
                height=frame.height - 256 if len(assuntos) * 80 + 16 > frame.height - 256 else len(assuntos) * 80 + 16
            )
            self._canvas.grid(row=1, column=0, padx=16, pady=16, sticky="news")
            self._canvas.configure(bg=frame.background)
            self._vertical_scrollbar = tk.Scrollbar(
                self._panel,
                orient=tk.VERTICAL,
                bg="black",
                command=self._canvas.yview
            )
            self._vertical_scrollbar.grid(row=1, column=1, sticky="ns")
            self._canvas.config(yscrollcommand=self._vertical_scrollbar.set)
            self._assuntos_panel = tk.Frame(self._canvas)
            self._assuntos_panel.configure(bg=frame.background)
            self._canvas.create_window((0, 0), window=self._assuntos_panel, anchor="center")
            self._selecionar_images = []
            self._editar_images = []
            self._excluir_images = []
            for i, assunto in enumerate(self._assuntos):
                self._favorito_label = tk.Label(
                    self._assuntos_panel,
                    text=assunto.nome,
                    bg=frame.background,
                    fg=frame.foreground,
                    font=(frame.font_family, frame.font_size)
                )
                self._favorito_label.grid(row=i, column=0, padx=16, pady=16)

                self._selecionar_images.append(ImageTk.PhotoImage(Image.open("img/favorito.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._selecionar_button = tk.Button(
                    self._assuntos_panel,
                    image=self._selecionar_images[i],
                    command=partial(self._selecionar, assunto),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._selecionar_button.grid(row=i, column=1, padx=16, pady=16)

                self._cadastrar_favorito_button = tk.Button(
                    self._assuntos_panel,
                    text="+F",
                    command=partial(self._cadastrar_favorito, assunto),
                    bg=frame.background,
                    fg=frame.foreground,
                    font=(frame.font_family, frame.font_size)
                )
                self._cadastrar_favorito_button.grid(row=i, column=2, padx=16, pady=16)

                self._editar_images.append(ImageTk.PhotoImage(Image.open("img/caneta.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._editar_button = tk.Button(
                    self._assuntos_panel,
                    image=self._editar_images[i],
                    command=partial(self._editar, assunto),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._editar_button.grid(row=i, column=3, padx=16, pady=16)

                self._excluir_images.append(ImageTk.PhotoImage(Image.open("img/lixeira.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._excluir_button = tk.Button(
                    self._assuntos_panel,
                    image=self._excluir_images[i],
                    command=partial(self._excluir, assunto),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._excluir_button.grid(row=i, column=4, padx=16, pady=16)
            self._assuntos_panel.update_idletasks()
            self._canvas.create_window(
                (self._canvas.winfo_width() / 2, self._canvas.winfo_height() / 2),
                window=self._assuntos_panel,
                anchor="center"
            )
        else:
            self._titulo_label = tk.Label(
                self._panel,
                text="Não há assunto cadastrado.",
                bg=frame.background,
                fg=frame.foreground,
                font=(frame.font_family, frame.font_size * 2)
            )
            self._titulo_label.grid(row=0, column=0, padx=16, pady=16)
        
        self._my_frame.manter_aberto()
    

    def _selecionar(self, assunto: Assunto) -> None:
        FavoritoController.listar(self._my_frame, assunto)
    

    def _cadastrar_favorito(self, assunto: Assunto) -> None:
        FavoritoController.cadastrar(self._my_frame, assunto)
    
    
    def _editar(self, assunto: Assunto) -> None:
        AssuntoController.editar(self._my_frame, assunto)
    

    def _excluir(self, assunto: Assunto) -> None:
        AssuntoController.ameacar(self._my_frame, assunto)