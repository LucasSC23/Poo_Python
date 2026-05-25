from Personajes.Peleador import Peleador

class KickBoxer(Peleador):
    
     #Metodos absstractos
    def __init__(self,nombre):
        super().__init__(nombre)

    def ataqueBasico(self):
        if self.energia >= 18:
            self.usarEnergia(18)
            danio = 15  # O el daño base que quieras ponerle
            return danio  # 🟢 CRUCIAL: Devolver el número para que el motor lo use
        return 0

    def ataqueEspecial(self):
        if self.energia >= 25:
            self.usarEnergia(25)
            danio = 30  # Daño especial
            return danio  # 🟢 CRUCIAL: Devolver el daño
        return 0