from zooAnimales.animal import Animal

class Mamifero(Animal):
    self_listado = []

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)



animal = Animal("liz", 5, "medellin", "f")

mamifero = Mamifero("perro", 1,1,1)

print(mamifero._nombre)