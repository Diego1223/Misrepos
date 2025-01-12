#Vamos a hacer un inicio de sesion basico 
#Usaremos un diccionario con el correo y la contrasena
from tkinter import *
from PIL import ImageTk, Image


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Inicio de sesion')
        self.root.geometry("500x400")
        self.LogoInicio()        

        
        self.root.mainloop()

    def LogoInicio(self):
        self.logo = Image.open("imgs/logo.ico")
        self.logo = self.logo.resize((100,100), Image.Resampling.NEAREST)
        self.logoTk = ImageTk.PhotoImage(self.logo)
        Label(self.root, image=self.logoTk).pack(pady=10)


root = Main()
