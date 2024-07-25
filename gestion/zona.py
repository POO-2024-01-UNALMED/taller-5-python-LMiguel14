class Zona ():
    _animales = []
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
    def getNombre(self):
        return self._nombre
    def getZoo (self):
        return self._zoo
    #def getAnimales (self):
    #    return self._animales

    @classmethod
    def agregarAnimales(cls, newAnimal):
        Zona._animales.append(newAnimal)
    @classmethod
    def cantidadAnimales(cls):
        return len(Zona._animales)
    