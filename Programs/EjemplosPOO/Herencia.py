#Usaremos la herencia en este ejercicio
class Persona:
    #Se ejecuta sola al crear el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        print(f'Nombre -> {self.nombre}\nEdad -> {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, aula):
        super().__init__(nombre, edad)
        self.aula = aula

    def __str__(self):
        return f'Nombre -> {self.nombre}\nEdad -> {self.edad}\nAula -> {self.aula}'


p1 = Persona('Diego', 19)
p1.imprimir()

print('*********')
es = Estudiante('Diego', 19, 2)
print(es)