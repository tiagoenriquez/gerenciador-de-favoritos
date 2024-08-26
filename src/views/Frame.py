import tkinter as tk

from src.controllers import AssuntoController


class Frame:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.update_idletasks()
        self.background = "black"
        self.foreground = "yellow"
        self.font_family = "serif"
        self.font_size = 12

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        x = (self.width - 800) // 2
        y = (self.height - 800) // 2
        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.window.title("Meus Favoritos")
        self.window.configure(background=self.background)

        self._menu = tk.Menu(
            self.window,
            bg=self.background,
            fg=self.foreground,
            font=(self.font_family, self.font_size)
        )
        self.window.config(menu=self._menu)
        self._menu.add_command(label='Listar Assuntos', command=self._listar_assuntos)
        self._menu.add_command(label='Cadastrar Assunto', command=self._cadastrar_assunto)

        icon = "img/favorito.png"
        self.window.iconphoto(False, tk.PhotoImage(file=icon))


    def limpar(self):
        for widget in self.window.winfo_children():
            if (str(type(widget)) != "<class 'tkinter.Menu'>"):
                widget.destroy()
    

    def manter_aberto(self):
        self.window.mainloop()
    

    def _listar_assuntos(self) -> None:
        AssuntoController.abrir_seletor(self)
    

    def _cadastrar_assunto(self) -> None:
        AssuntoController.cadastrar(self)