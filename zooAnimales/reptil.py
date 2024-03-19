from animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas =0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)

        #get
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    #set
    def setColorEscamas(self, new):
        self._colorEscamas = new
    def setLargoCola(self, newl):
        self._largoCola= newl
    

    @classmethod
    def cantidadReptiles(self):
        return len(self._listado)
    
    def movimiento(self):
        pass
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero, colorEscamas= "verde", largoCola = 3, habitat= "humedal"):
        Reptil.iguanas += 1
        cls(nombre, edad, habitat, genero, colorEscamas, largoCola)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad,genero, colorEscamas= "blanco", largoCola= 1, habitat= "junga"):
        Reptil.serpientes +=1
        cls(nombre, edad, habitat, genero, colorEscamas, largoCola)