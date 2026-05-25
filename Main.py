# Archivo: Main.py (En la raíz de tu proyecto)
from UI.UIConsola import UIConsola

if __name__ == "__main__":
    # 1. Creamos el objeto de la consola (Acá se ejecuta su __init__)
    interfaz = UIConsola()
    
    # 2. Encendemos el juego llamando al método con sus paréntesis ()
    interfaz.iniciarJuego()