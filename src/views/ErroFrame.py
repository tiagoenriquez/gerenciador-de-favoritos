import tkinter as tk

from src.views.Frame import Frame as MyFrame


class ErroFrame:
    def __init__(self, frame: MyFrame, erro: str) -> None:
        self._my_frame = frame
        self._my_frame.limpar()
        self._window = frame.window

        self._panel = tk.Frame(self._window)
        self._panel.configure(bg=frame.background)
        self._panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._titulo_label = tk.Label(
            self._panel,
            text=f"Erro",
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size * 2)
        )
        self._titulo_label.grid(row=0, column=0, padx=16, pady=16)

        self._titulo_label = tk.Label(
            self._panel,
            text=erro,
            bg=frame.background,
            fg=frame.foreground,
            font=(frame.font_family, frame.font_size)
        )
        self._titulo_label.grid(row=1, column=0, padx=16, pady=16)
        
        self._my_frame.manter_aberto()