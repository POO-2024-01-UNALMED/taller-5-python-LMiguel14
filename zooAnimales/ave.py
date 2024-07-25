from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    aguilas = 0
    halcones= 0
    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero) 
        self._colorPlumas = color
        self._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, newColor):
        self._colorPlumas = newColor
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero, color = "café glorioso", habitat ="montanas" ):
        Ave.halcones += 1
        cls(nombre, edad, habitat, genero, color)
        
    @classmethod
    def crearAguila(cls, nombre, edad, genero, color = "blanco y amarillo", habitat ="montanas" ):
        Ave.aguilas += 1
        cls(nombre, edad, habitat, genero, color)
    
    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)