import tkinter as tk
from PySimpleGUI import popup_get_file


class MenuBar():
    def __init__(self, app):
        self.root = app

        self.menubar = tk.Menu(self.root)

        # MENUS #
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.impressao_menu = tk.Menu(self.menubar, tearoff=0)


        # OPÇÕES DO MENU DE ARQUIVO #

        self.file_menu.add_command(label='Abrir', command=self.getFile)
        self.file_menu.add_command(label='Salvar')
        self.file_menu.add_command(label='Excluir', )
        self.file_menu.add_command(label='Localizar')


        # OPÇÕES DO MENU DE IMPRESSÃO #
        self.impressao_menu.add_command(label='Com Preço')
        self.impressao_menu.add_separator()
        self.impressao_menu.add_command(label='Sem Preço')



        self.menubar.add_cascade(label='Nota', menu=self.file_menu)
        self.menubar.add_cascade(label='Impressão', menu=self.impressao_menu)
        self.root.config(menu=self.menubar)

    @classmethod
    def getFile(cls):
        path_file = popup_get_file("Selecione o arquivo:")
        return path_file
