import tkinter as tk
from src.views.Frame import Frame as MyFrame


class CadastroFrame:
    def __init__(self, frame: MyFrame):
        self._frame = frame
        self._frame.limpar()
        window = frame.window
        window.title("Cadastro de Favorito")

        panel = tk.Frame(window)
        panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        nome_label = tk.Label(panel, text="Nome")
        nome_label.grid(row=0, column=0, padx=8, pady=8)

        self._nome_entry = tk.Entry(panel)
        self._nome_entry.grid(row=0, column=1, padx=8, pady=8)

        url_label = tk.Label(panel, text="URL")
        url_label.grid(row=1, column=0, padx=8, pady=8)

        self._url_entry = tk.Entry(panel)
        self._url_entry.grid(row=1, column=1, padx=8, pady=8)
        
        button = tk.Button(panel, text="Salvar")
        button.grid(row=2, column=0, columnspan=2, padx=8, pady=8)

        self._frame.manter_aberto()