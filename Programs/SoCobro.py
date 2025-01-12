#Sistema de cobro sucursal Carniceria, tiene como funcion pasarle el producto, despues el peso
#con esos datos va a calcular cuanto va a costar, ingresamos el dinero que nos dio el cliente y luego
#el programa nos dira cuanto tenemos que darle de cambio
import os
from os import system
class Program:
    def __init__(self):

        system("clear")
        self.anchoTerminal = os.get_terminal_size().columns
        self.bienvenida = "SISTEMA DE COBRO"
        #Hacemos que el texto se ponga justo en medio de la terminal
        print(" " * (self.anchoTerminal // 2 - len(self.bienvenida)) + f"\t{self.bienvenida}")
        self.Productos()

    def Productos(self):
        self.productosExistentes = {
            "Cachete": 269,
            "Tripa": 320,
            "Bofe": 160,
        }    
        self.lista = list(self.productosExistentes.keys())
        self.listaPrecios = list(self.productosExistentes.values())
        for x in range(len(self.lista)):
            print(f"{x + 1}. {self.lista[x]}")

        self.intentos = 1
        while self.intentos <= 3:    
            try:
                self.opcion = int(input("-> "))
                self.peso = int(input("Cuanto producto llevo gr -> "))
                self.costo = (self.listaPrecios[self.opcion - 1] * self.peso) / 1000

                print(f"\nCobrar: {self.costo} al cliente")
                self.pagar = int(input("Pagara con: "))
                self.cambio = float(self.pagar -self.costo)
                if self.cambio < 0.0:
                    print("Error, no alcanza el monto para pagar")
                    monedaError = True
                else:
                    print(f"El cambio del cliente es: {self.cambio}")

                self.ticket = input("\nDeseas imprimir el ticket? (y/n)\n")

                if self.ticket == "y" or self.ticket == "Y":
                    if monedaError:
                        print("+--------------------+----------+")
                        print("| Producto           |Pago")
                        print("+--------------------+----------+")
                        print(f"| {self.lista[self.opcion - 1]}            |{self.pagar}")
                        print(f"|$         No se realizo el pago+")    
                    else:
                        print("+--------------------+----------+")
                        print("| Producto           |Pago")
                        print("+--------------------+----------+")
                        print(f"| {self.lista[self.opcion - 1]}            |{self.pagar}")
                        print(f"| Cambio             |${self.cambio}")
                    break                  
                elif self.ticket == "n" or self.ticket == "N":
                    break
                else:
                    print("Error") 
            except:
                if self.intentos >= 3:
                    print("ERROR. Saliendo del programa")
                else:
                    print("Ocurrio un error, vuelve a intentarlo")
            self.intentos += 1
programa = Program()
