#Ejemplos de herencia en programacion orientada a objetos 
class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Hijo(Person):
    def __init__(self, nombre, edad, padre):
        super().__init__(nombre, edad)
        self.padre = padre

p1 = Person('diego', 12)
print(p1.nombre, p1.edad)
h1 = Hijo('diego', 21, 'Alonso')
print(h1.nombre, h1.edad, h1.padre)


