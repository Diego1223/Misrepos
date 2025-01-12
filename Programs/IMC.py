#Crear un programa el cual calcule nuestro IMC
import sys
import time
from os import system

class Programa:
    def Menu(self):
        listaOpciones = ['Calcular IMC', 'Segunda opcion']

        system('clear')
        for z in range(len(listaOpciones)):
            print(f'{z + 1}. {listaOpciones[z]}')
        error = 1
        while error <= 3:
            try:
                op = int(input('-> '))
                match op:
                    case 1: self.IMC()
                break 
            except ValueError:
                if error >= 3:
                    sys.stdout.write('Saliendo del programa')
                    sys.stdout.flush()
                   
                    for x in range(3):
                        sys.stdout.write('.')
                        sys.stdout.flush()
                        time.sleep(0.5)
                else:
                    print('Error, ingresa un numero')
            except KeyboardInterrupt:
                sys.stdout.write('\nSaliendo del programa')
                sys.stdout.flush()

                for x in range(3):
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    time.sleep(0.5)
                break
                error += 1

    def IMC(self):
        peso = int(input('Ingresa tu peso -> ')) 
        estatura = float(input('Ingresa tu estatura -> '))
        cuadrado = estatura * estatura
        resultado = peso / cuadrado
        
        print(f'Tu IMC en base a tu peso {peso} y estatura: {estatura} es de: {round(resultado, 2)}')
        
        if resultado <= 24.9 and resultado >= 18.5:
            print('En base a esto, tu estado nutricio es saludable')
        elif resultado >= 25 and resultado <= 29.9:
            print('En base a esto, tu estado nutricio es de sobrepeso')
        elif resultado >= 30:
            print('Tienes obesidad')

programa = Programa()
programa.Menu()


