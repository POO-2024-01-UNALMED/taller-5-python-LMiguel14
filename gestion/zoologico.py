class Zoologico():
    _zonas =[]
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def getZona(self):
        return Zoologico._zonas
    
    def setNombre(self, newName):
        self._nombre = newName
    def setUbicacion(self, new):
        self._ubicacion = new
    
    @classmethod
    def agregarZonas(cls, zona):
        Zoologico._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        return len(Zoologico._zonas)
