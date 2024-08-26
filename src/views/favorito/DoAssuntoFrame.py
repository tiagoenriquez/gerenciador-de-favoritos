from functools import partial
from PIL import ImageTk, Image
import tkinter as tk

from src.controllers import FavoritoController
from src.models.Assunto import Assunto
from src.models.Favorito import Favorito
from src.views.Frame import Frame as MyFrame


class DoAssuntoFrame:
    def __init__(self, frame: MyFrame, favoritos: list[Favorito], assunto: Assunto) -> None:
        self._my_frame = frame
        self._favoritos = favoritos
        self._assunto = assunto
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        if favoritos:
            self._titulo_label = tk.Label(
                self._panel,
                text=f"Favoritos de {assunto.nome}",
                bg=frame.background,
                fg=frame.foreground,
                font=(frame.font_family, frame.font_size * 2)
            )
            self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

            self._canvas = tk.Canvas(
                self._panel,
                highlightthickness=0,
                width=frame.width - 128,
                height=frame.height - 256 if len(favoritos) * 80 + 16 > frame.height - 256 else len(favoritos) * 80 + 16
            )
            self._canvas.grid(row=1, column=0, sticky="news")
            self._canvas.configure(bg=frame.background)
            self._vertical_scrollbar = tk.Scrollbar(
                self._panel,
                orient=tk.VERTICAL,
                bg="black",
                command=self._canvas.yview
            )
            self._vertical_scrollbar.grid(row=1, column=1, sticky="ns")
            self._canvas.config(yscrollcommand=self._vertical_scrollbar.set)
            self._favoritos_panel = tk.Frame(self._canvas)
            self._favoritos_panel.configure(bg=frame.background)
            self._canvas.create_window((0, 0), window=self._favoritos_panel, anchor="center")
            self._abrir_images = []
            self._editar_images = []
            self._excluir_images = []
            for i, favorito in enumerate(self._favoritos):
                self._favorito_label = tk.Label(
                    self._favoritos_panel,
                    text=favorito.nome,
                    bg=frame.background,
                    fg=frame.foreground,
                    font=(frame.font_family, frame.font_size)
                )
                self._favorito_label.grid(row=i, column=0, padx=16, pady=16)

                self._abrir_images.append(ImageTk.PhotoImage(Image.open("img/navegador.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._abrir_button = tk.Button(
                    self._favoritos_panel,
                    image=self._abrir_images[i],
                    command=partial(self._abrir, favorito.url),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._abrir_button.grid(row=i, column=1, padx=16, pady=16)

                self._editar_images.append(ImageTk.PhotoImage(Image.open("img/caneta.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._editar_button = tk.Button(
                    self._favoritos_panel,
                    image=self._editar_images[i],
                    command=partial(self._editar, favorito),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._editar_button.grid(row=i, column=2, padx=16, pady=16)

                self._excluir_images.append(ImageTk.PhotoImage(Image.open("img/lixeira.png").resize(
                    (32, 32),
                    Image.Resampling.LANCZOS
                )))
                self._excluir_button = tk.Button(
                    self._favoritos_panel,
                    image=self._excluir_images[i],
                    command=partial(self._excluir, favorito),
                    bg=frame.background,
                    font=(frame.font_family, frame.font_size)
                )
                self._excluir_button.grid(row=i, column=3, padx=16, pady=16)
            self._favoritos_panel.update_idletasks()
            self._canvas.create_window(
                (self._canvas.winfo_width() / 2, self._canvas.winfo_height() / 2),
                window=self._favoritos_panel,
                anchor="center"
            )
        else:
            self._titulo_label = tk.Label(
                self._panel,
                text=f"Não há favorito de {assunto.nome} cadastrado.",
                bg=frame.background,
                fg=frame.foreground,
                font=(frame.font_family, frame.font_size * 2)
            )
            self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

        self._my_frame.manter_aberto()

    
    def _abrir(self, url: str) -> None:
        FavoritoController.abrir(url)
        
    
    def _editar(self, favorito: Favorito) -> None:
        FavoritoController.editar(self._my_frame, Favorito(
            favorito.nome,
            favorito.url,
            favorito.assunto_id,
            self._assunto,
            favorito.id
        ))
        
    
    def _excluir(self, favorito: Favorito) -> None:
        FavoritoController.ameacar(self._my_frame, Favorito(
            favorito.nome,
            favorito.url,
            favorito.assunto_id,
            self._assunto,
            favorito.id
        ))