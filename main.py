from tkinter import *
from menubar import MenuBar
from frameCliente import FrameCliente


class MainWindow():
    def __init__(self, title) -> None:
        self.root = Tk()

        # CONFIGURAÇÕES DO JANELA PRINCIPAL #
        # self.root.title = title
        self.root.geometry(f"{750}x{600}")
        MenuBar(self.root)
        FrameCliente(self.root)

        self.root.mainloop()



window = MainWindow('Sistemas Notas')