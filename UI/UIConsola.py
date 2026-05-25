# Archivo: UI/UIConsola.py
from Motor.MotorJuego import MotorJuego

class UIConsola:
    def __init__(self):
        self.juego = MotorJuego()
    
    def mostrarEstado(self):
        print("", "="*50)
        print(f"Jugador: {self.juego.jugador.nombre}\nSalud: {self.juego.jugador.salud}/100\nEnergía: {self.juego.jugador.energia}/100\n")
        print(f"Enemigo: {self.juego.enemigo.nombre}\nSalud: {self.juego.enemigo.salud}/100\nEnergía: {self.juego.enemigo.energia}/100\n")
        print("="*50)        
        
    def iniciarJuego(self):
        print("Bienvenido al FightCombat, desafío de peleadores \nSolo el mejor queda en pie\n")
        
        nombre = input("Ingrese el nombre del peleador: ")
        print("\nSeleccione el estilo de pelea: ")
        print("[1] Boxeador")
        print("[2] Kickboxer")
        print("[3] Taekwondista")
        clase = input("Opción [1-3]: ")
        
        self.juego.eleccionPersonaje(nombre, clase)
        
        print(f"\nTe enfrentarás a {self.juego.enemigo.nombre}, ¡buena suerte!")      
        
        while self.juego.verificarGanador() == "Continuar":
            self.mostrarEstado()
            
            print("¿Qué acción desea realizar?")
            print("[1] Ataque Básico")
            print("[2] Ataque Especial")
            accion = input("Selecciona [1,2]: ")
            
            # Convertimos a entero para que tu motor lo lea como número (1 o 2)
            if accion in ["1", "2"]:
                accionInt = int(accion)
            else:
                accionInt = 1 # Por defecto ataque básico si mete cualquier cosa
            
            # 🟢 USANDO TU MÉTODO REAL: ataqueJugador
            danioJugador = self.juego.ataqueJugador(accionInt)
            
            # Verificamos si terminó la partida tras tu golpe
            if self.juego.verificarGanador() != "Continuar":
                break

            print(f"\n🤖 Turno de {self.juego.enemigo.nombre}...")
            
            # 🟢 USANDO TU MÉTODO REAL: ataqueIa
            danioIA = self.juego.ataqueIa()

        # Pantalla de fin de partida
        print("\n" + "#"*50)
        if self.juego.verificarGanador() == "Jugador":
            print(f"🏆 ¡FELICITACIONES {nombre}! Has ganado la simulación en Penguin Academy. 🏆")
        else:
            print("💀 Has sido derrotado... GAME OVER. 💀")
        print("#"*50)