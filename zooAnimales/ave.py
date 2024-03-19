from animal import Animal

class Ave(Animal):

    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero) 
        self._colorPlumas = color
    def getColorPlumas(self):
        return self._colorPlumas
