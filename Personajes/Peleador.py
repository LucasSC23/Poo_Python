from abc  import ABC, abstractmethod

class Peleador (ABC):
    def __init__(self,nombre):
        self.nombre=nombre
        #Aplico el encapsulamiento, nade puede tocarlo fuera, solo dentro de esta clase
        self.__salud=100
        self.__energia=100
        
 
    #D0ecorador
    @property
    def salud(self):
        return self.__salud
    
    @property
    def daño(self):
        return self.__daño
    
    @property
    def recibirDanio(self,cantidad):
        self.__salud=max(0,self.__salud - cantidad)
        print(f"El {self.nombre} recibio:{cantidad} de daño. Le queda {self.__salud} de salud")    
    
    @property
    def estaVivo(self):
        return self.__salud > 0 
    
    @property
    def usarEnergia(self,uso):
        self._energia=max(0,self._energia-uso)
        return 
    
    
    @abstractmethod
    def ataqueBasico(self):
        pass
    
    @abstractmethod
    def ataquePatada(self):
        pass
    
    @abstractmethod
    def ataqueEspecial(self):
        pass