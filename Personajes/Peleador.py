from abc  import ABC, abstractmethod

class Peleador (ABC):
    def __init__(self,nombre):
        self.nombre=nombre
        #Aplico el encapsulamiento, nade puede tocarlo fuera, solo dentro de esta clase
        self.__salud=100
        self.__energia=100
        
 
    #Decorador:Getters limpios para poder consultar el estado desde afuera
    @property#CON PROPERTY LO CONVIERTO EN SOLO LECTURA
    def salud(self):
        return self.__salud
    @property
    def energia(self):
        return self.__energia
    
    #Metodos comunes
    def recibirDanio(self,cantidad):
        self.__salud=max(0,self.__salud - cantidad)
        print(f"El {self.nombre} recibio:{cantidad} de daño. Le queda {self.__salud} de salud")    
    
    
    def estaVivo(self):
        return self.__salud > 0 
    
    def usarEnergia(self,uso):
        self.__energia=max(0,self.__energia-uso)
        return 
    
    #Metodos absstractos
    @abstractmethod
    def ataqueBasico(self):
        pass
    
    
    @abstractmethod
    def ataqueEspecial(self):
        pass
    