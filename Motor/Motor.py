from Personajes.Peleador import Peleador
from Personajes.Taekwondista import Taekwondista
from Personajes.KickBoxer import KickBoxer
from Personajes.Boxeador import Boxeador
import random

class Motor():
    def __init__(self):
        self.jugador==none
        self.enemigo==none
        
    def eleccionPersonaje(self,nombreJugador,claseElegida):
        if claseElegida==1:
            self.jugador=Boxeador(nombreJugador)
        if claseElegida==2:
            self.jugador=KickBoxer(nombreJugador)
        else:
            self.jugador==Taekwondista(nombreJugador)
        
        claseIa= random.choice(["Boxeador","KickBoxer","Taekwondista"])
        if claseIa=="Boxeador":
            self.enemigo=Boxeador(MikeTyson)
        if claseIa=="KickBoxer":
            self.enemigo=KickBoxer(McGregor)
        else:
            self.enemigo=Taekwondista(BruceLee)
            
    def ataqueJugador(self,opcionAtaque):
        if opcionAtaque==1:
            danio=self.jugador.ataqueBasico()
        else:
            danio=self.jugador.ataqueEspecial()
        
        if danio>0:
            return danio
        
    def ataqueIa(self,opcionAtaqueIa):
        if self.enemigo.energia >= 20 and random.random()>0.5:
            self.enemigo.ataqueEspecial()
        else:
            self.enemigo.ataqueBasico()
            
        if danio>0:
            self.jugador.recibirDanio
        return danio
    
    def estaVivo(self):
        if not self.jugador.estaVivo():  
            return "enemigo"
        if not self.enemigo.estaVivo():
            return "jugador"
        return "continuar"