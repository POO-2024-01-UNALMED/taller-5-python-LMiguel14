from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos=0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    #get
    def getPelaje(self):
        return self._pelaje
    def getPatas(self):
        return self._patas
    #set
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def setPatas(self, patas):
        self._patas= patas
    def isPelaje(self):
        return self._pelaje
    
    @classmethod
    def crearCaballo(cls, nombre,edad, genero, pelaje = True, patas = 4, habitat = "pradera"):
        Mamifero.caballos += 1
        return cls(nombre, edad, genero, pelaje, patas, habitat)
    @classmethod
    def crearLeon(cls, nombre, edad, genero, pelaje = True, patas = 4, habitat = "selva"):
        Mamifero.leones += 1
        return cls(nombre, edad, genero, pelaje, patas, habitat)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)
    

