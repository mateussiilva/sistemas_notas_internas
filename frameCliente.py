from tkinter import *
from tkinter.ttk import Combobox

class FrameCliente():
    font_padrao = 'Arial 12'
    pad_x = 10
    pad_y = 10

    def __init__(self, app) -> None:
        self.root = app
        self.frame_cl = Frame(self.root, border=4, relief='sunken',width=700,)

        self.lbl_cliente = Label(self.frame_cl, text='Cliente', font=self.font_padrao)
        self.inp_cliente = Combobox(self.frame_cl, values=['Mateus José da Silva'], width=50, font=self.font_padrao)

        self.lbl_data = Label(self.frame_cl, text='Data Emissão', font=self.font_padrao)
        self.inp_data = Combobox(self.frame_cl, width=8,values=[''])


        # self.frame_cl.place(x=0,y=0, width=740)
        self.frame_cl.pack(fill='x' )
        # self.frame_cl.configure()

        # ELEMENTOS DA LINHA 0
        self.lbl_cliente.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y)
        self.inp_cliente.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y)

        # ELEMENTOS DA LINHA 1 #
        self.lbl_data.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y)
        self.inp_data.grid(row=1, column=1, sticky='W' ,padx=self.pad_x, pady=self.pad_y,)
        
        
        