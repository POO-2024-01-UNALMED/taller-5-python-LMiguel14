from animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas =0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)


        #get
    def getColorPiel(self):
        return self._colorPiel
    def getVenenoso(self):
        return self._venenoso
    #set
    def setColorPiel(self, newColor):
        self._colorPiel = newColor
    def setVenenoso(self, Vene):
        self._venenoso= Vene
    
    @classmethod
    def cantidadAnfibios(self):
        return len(Anfibio._listado)
    @classmethod
    def crearRana(cls, nombre, edad, gener, colorPiel = "rojo", venenoso = True, habitat= "selva"):
        Anfibio.ranas +=1
        cls(nombre, edad, gener, habitat, colorPiel, venenoso)
        

    @classmethod
    def crearSalamandra(cls, nombre, edad, gener, colorPiel = "negro y amarillo", venenoso = False, habitat= "selva"):
        Anfibio.salamandras +=1
        cls(nombre, edad, gener, habitat, colorPiel, venenoso)
        