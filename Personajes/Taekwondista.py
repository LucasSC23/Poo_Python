from Personajes.Peleador import Peleador
class Taekwondista(Peleador):
     #Metodos absstractos
    def __init__(self,nombre):
        super().__init__(nombre)

    def ataqueBasico(self):
        if self.energia >= 18:
            self.usarEnergia(18)
            return 15  # 🟢 RETORNA EL DAÑO REAL (Poné el número que quieras)
        return 0

    def ataqueEspecial(self):
        if self.energia >= 25:
            self.usarEnergia(25)
            return 30  # 🟢 RETORNA EL DAÑO REAL
        return 0