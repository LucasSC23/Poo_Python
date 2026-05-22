from Peleador import Peleador
class Taekwondista(Peleador):
     #Metodos absstractos
    def __init__(self,nombre):
        super().__init__(nombre)

    def ataqueBasico(self):
        self.usarEnergia(18)
        return 18 #Daño causado
    

    def ataqueEspecial(self):
        if self.energia>=27:
            self.usarEnergia(27)
            return 36#El ataque se realizo con exito
        else:
            return 0#El ataque no se realizo