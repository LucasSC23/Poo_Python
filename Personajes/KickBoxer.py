from Peleador import Peleador
class KickBoxer(Peleador):
    
     #Metodos absstractos
    def __init__(self,nombre):
        super().__init__(nombre)

    def ataqueBasico(self):
        self.usarEnergia(15)
        return 16#Daño causado
    

    def ataqueEspecial(self):
        if self.energia>=24:
            self.usarEnergia(24)
            return 34#El ataque se realizo con exito
        else:
            return 0#El ataque no se realizo