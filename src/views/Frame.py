import tkinter as tk


class Frame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.update_idletasks()

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        x = (self.width - 800) // 2
        y = (self.height - 600) // 2
        self.window.geometry(f"{800}x{600}+{x}+{y}")
        self.window.title("Meus Favoritos")
    
    def limpar(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    
    def manter_aberto(self):
        self.window.mainloop()