from animal import Animal

class Pez(Animal):
    _listado = []
    salmones =0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscama, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscama = colorEscama
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)


        #get
    def getColorEscama(self):
        return self._colorEscama
    def getCantidadAletas(self):
        return self._cantidadAletas
    #set
    def setColorEscama(self, newColor):
        self._colorEscama = newColor
    def setCantidadAletas(self, num):
        self._cantidadAletas= num
    
    def movimiento(self):
        pass
    
    @classmethod
    def cantidadAnfibios(self):
        return len(Pez._listado)
    @classmethod
    def crearSalmon(cls, nombre, edad, gener, colorEscamas = "rojo", cantidadAletas =6, habitat= "oceano"):
        Pez.salmones +=1
        cls(nombre, edad, gener, habitat, colorEscamas, cantidadAletas)
        

    @classmethod
    def crearBacalao(cls, nombre, edad, gener, colorEscamas = "gris", cantidadAletas =6, habitat= "oceano"):
        Pez.bacalaos +=1
        cls(nombre, edad, gener, habitat, colorEscamas, cantidadAletas)
        