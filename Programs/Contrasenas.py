import secrets
import string
import os
import datetime as dt

class CreacionContras:
    def creacionContrasena(self, caracteres):
        self.caracteres = caracteres

        self.alpabhet = string.ascii_letters + string.digits
        
        print("\nAqui tienes dos opciones de contrasena")
        for x in range(2):
            self.contrasena = ''.join(secrets.choice(self.alpabhet) for j in range(self.caracteres))
            self.ocultar1 = self.contrasena
            self.ocultar2 = self.contrasena
            print(self.contrasena)

        print('Quieres ocultar las contrasenas? (Y/n)')
        self.opcion = input("=> ") 
        self.intentos = 1

        while self.intentos <= 3:
            if self.opcion == "Y" or self.opcion == "y":
                os.system("clear")
                print("Aqui tienes tus contrasenas \n")
                print(len(self.ocultar1) * "*")
                print(len(self.ocultar2) * "*")
            elif self.opcion == "N" or self.opcion == "n":
                print("Saliendo y guardando")
            else:
                print("Elige bien la opcion")
                self.opcion = input("=> ")       
                if self.intentos > 2:
                    print("Saliendo del programa....")                       
            self.intentos += 1

os.system("clear")
dia = dt.datetime.now()

print(f"\t\t\t\t Creacion de crontrasenas \t\t\t{dia.hour}:{dia.minute}")

intentos = 1
while intentos <= 4:
    try:
        caracteres = int(input("\n\nCuantos caracteres quieres que tenga tu contrasena -> "))
        creacion = CreacionContras()
        creacion.creacionContrasena(caracteres)
        break
    except ValueError:
        if intentos <= 3:
            print('Error, vuelve a intentarlo')
        else:
            print("\nSaliendo del programa...")
    except KeyboardInterrupt:
        print("\nFinalizando tarea ")
        break
    intentos += 1
