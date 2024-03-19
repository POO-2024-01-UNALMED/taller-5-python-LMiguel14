#from gestion.zona import Zona

class Animal():
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.totalAnimales += 1
    
    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getHabitat(self):
        return self._habitat
    def getGenero(self):
        return self._genero
    
    

    def movimiento(self):
        pass    
    def totalPorTipo(self):
        #cadena = f"Mamiferos: {}\nAves: {}\nReptiles: {}\nPeses: {}\Anfibios: {}"
        #return cadena
        pass
    def toString(self):
        formato = f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad()} y mi genero es {self.getGenero()}, la zona en que me ubico es "
        return formato 




    
        
    