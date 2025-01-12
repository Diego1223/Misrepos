#Programa que nos ayuda para saber nuestro IMC
#Tienes un problema en la linea de codigo de los errores y los botones
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
#Centrar la pantalla

class Main:
    def __init__(self, root):
        self.root = root
        self.ConfigApp(root)
        self.ImagenSalud()
             
        Label(root, text='Peso', font=("verdana", 14)).pack(pady=20)
        self.peso = StringVar()
        self.peso= Entry(root, textvariable=self.peso, font=("Verdana", 11))
        self.peso.pack()


        Label(root, text='Estatura', font =("Verdana", 14)).pack(pady=10)
        self.estatura = StringVar()
        self.estatura = Entry(root, textvariable=self.estatura, font=("Verdana", 11))
        self.estatura.pack()

        
        #raised hace que el elemento que encierra este por encima del nivel de la superficie
        self.boton = Button(root, text='Calcular IMC', relief="raised", borderwidth=5, cursor="hand1", command=self.CalcularIMC) 
        self.boton.pack(pady=10)
    def ConfigApp(self,root):
        #Esta parte centra la aplicacion
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 500
        alto_ventana = 300
        posX = (ancho_pantalla - ancho_ventana) // 2
        posY = (alto_pantalla - alto_ventana) // 2

        root.geometry(f"{ancho_ventana}x{alto_ventana}+{posX}+{posY}")

        
    def ImagenSalud(self):
        #Configuracion de la imagen
        self.img = Image.open("imgs/icono.ico")                         
        self.img = self.img.resize((100, 100), Image.Resampling.NEAREST)
        self.imgTk = ImageTk.PhotoImage(self.img)                       
        self.imgEtiqueta ultado = 'desnutricion'
    
            Label(self.root, text=f'IMC: {round(self.imc, 2)} - {self.resultado}', font=("Bold", 13)).pack(pady=5)

        except V= Label(self.root, image=self.imgTk)                
        self.imgEtiqueta.place(relwidth= 0.3, relheight=1)        


    def CalcularIMC(self):
        try:
            self.peso1 = float(self.peso.get())
            self.estatura1 = float(self.estatura.get())
            self.cuadrado = self.estatura1 * self.estatura1
            self.imc = self.peso1 / self.cuadrado
            self.resultado = 'no detectado'

            if self.imc <= 24.9 and self.imc >= 18.5:
                self.resultado = 'saludable'
            elif self.imc >= 25 and self.imc <= 29.9:
                self.resultado = 'sobrepeso'
            elif self.imc >= 30:
                self.resultado = 'obesidad'
            L
            elif self.imc <= 18.5:
                self.resultado = 'desnutricion'
    
            Label(self.root, text=f'IMC: {round(self.imc, 2)} - {self.resultado}', font=("Bold", 13)).pack(pady=5)

        except ValueError:
            messagebox.showerror(message='Error. Tienes que ingresar valores numericos')
root = Tk()
root.title('IMC')
mn = Main(root)

root.mainloop()

                                
                                                              
