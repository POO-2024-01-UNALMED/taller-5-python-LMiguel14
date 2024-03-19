from animal import Animal

class Mamifero(Animal):
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self.caballos=0
        self.leones = 0
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

        return cls(nombre, edad, genero, pelaje, patas, habitat)

    @classmethod
    def crearLeon(cls, nombre, edad, genero, pelaje = True, patas = 4, habitat = "selva"):
        return cls(nombre, edad, genero, pelaje, patas, habitat)
    
    def cantidadMamiferos(self):
        return len(Mamifero._listado)       

