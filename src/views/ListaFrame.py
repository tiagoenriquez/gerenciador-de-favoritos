from functools import partial
import tkinter as tk
from src.controllers import FavoritoController
from src.models.Favorito import Favorito
from src.views.Frame import Frame as MyFrame
from src.views.Menu import Menu


class ListaFrame:
    def __init__(self, frame: MyFrame, favoritos: list[Favorito]):
        self._frame = frame
        self._frame.limpar()
        window = frame.window
        window.title("Lista de Favoritos")
        Menu(frame)

        panel = tk.Frame(window)
        panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        canvas = tk.Canvas(panel, highlightthickness=0, width=frame.width-1152, height=frame.height-512)
        canvas.grid(row=0, column=0, padx=8, pady=8, sticky="news")
        vertical_scrollbar = tk.Scrollbar(panel, orient=tk.VERTICAL, command=canvas.yview)
        vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.config(yscrollcommand=vertical_scrollbar.set)

        favoritos_panel = tk.Frame(canvas)
        canvas.create_window((0, 0), window=favoritos_panel, anchor="center")

        for i, favorito in enumerate(favoritos):
            label = tk.Label(favoritos_panel, text=favorito.nome)
            label.grid(row=i, column=0, padx=8, pady=8)

            abrir_button = tk.Button(favoritos_panel, text="Abrir", command=partial(self._abrir, favorito.url))
            abrir_button.grid(row=i, column=1, padx=8, pady=8)

            editar_button = tk.Button(favoritos_panel, text="Editar", command=partial(self._editar, favorito.id))
            editar_button.grid(row=i, column=2, padx=8, pady=8)

            excluir_button = tk.Button(favoritos_panel, text="Excluir", command=partial(self._excluir, favorito.id))
            excluir_button.grid(row=i, column=3, padx=8, pady=8)
        
        favoritos_panel.update_idletasks()
        canvas.create_window(
            (canvas.winfo_width() / 2, canvas.winfo_height() / 2),
            window=favoritos_panel,
            anchor="center"
        )

        self._frame.manter_aberto()
    
    def _abrir(self, url: str):
        FavoritoController.abrir(self._frame, url)
    
    def _editar(self, id: int):
        FavoritoController.editar(self._frame, id)
    
    def _excluir(self, id: int):
        FavoritoController.excluir(self._frame, id)