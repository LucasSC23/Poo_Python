from Peleador import Peleador
class Boxeador(Peleador):
     #Metodos absstractos
    def __init__(self,nombre):
        super().__init__(nombre)

    def ataqueBasico(self):
        self.usarEnergia(15)
        return 14 #Daño causado
    

    def ataqueEspecial(self):
        if self.energia>=26:
            self.usarEnergia(26)
            return 35#El ataque se realizo con exito
        else:
            return 0#El ataque no se realizo