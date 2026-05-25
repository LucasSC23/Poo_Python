from Personajes.Peleador import Peleador
from Personajes.Taekwondista import Taekwondista
from Personajes.KickBoxer import KickBoxer
from Personajes.Boxeador import Boxeador
import random

class MotorJuego():
    def __init__(self):
        self.jugador=None
        self.enemigo=None
        
    def eleccionPersonaje(self,nombreJugador,claseElegida):
        if claseElegida=="1":
            self.jugador=Boxeador(nombreJugador)
        elif claseElegida=="2":
            self.jugador=KickBoxer(nombreJugador)
        else:
            self.jugador=Taekwondista(nombreJugador)
        
        claseIa= random.choice(["Boxeador","KickBoxer","Taekwondista"])
        if claseIa=="Boxeador":
            self.enemigo=Boxeador("MikeTyson")
        elif claseIa=="KickBoxer":
            self.enemigo=KickBoxer("McGregor")
        else:
            self.enemigo=Taekwondista("BruceLee")
            
    def ataqueJugador(self, opcionAtaque):
        if opcionAtaque == 1:
            print(f"{self.jugador.nombre} utiliza su ataque basico")
            danio = self.jugador.ataqueBasico()
        else:
            print(f"{self.jugador.nombre} utiliza su ataque especial")
            danio = self.jugador.ataqueEspecial()
        
        # 🟢 CORREGIDO: Si hay daño real, el enemigo lo recibe
        if danio and danio > 0:
            self.enemigo.recibirDanio(danio)
        return danio
        
    def ataqueIa(self):
        if self.enemigo.energia >= 20 and random.random() > 0.5:
            print(f"{self.enemigo.nombre} utiliza su ataque especial")
            danio = self.enemigo.ataqueEspecial()
        else:
            print(f"{self.enemigo.nombre} utiliza su ataque basico")
            danio = self.enemigo.ataqueBasico()
            
        # 🟢 CORREGIDO: Paréntesis agregados para que el jugador reciba el impacto
        if danio and danio > 0:
            self.jugador.recibirDanio(danio)
        return danio
    
    def verificarGanador(self):
        if not self.jugador.estaVivo():  
            return "Enemigo"
        if not self.enemigo.estaVivo():
            return "Jugador"
        return "Continuar"