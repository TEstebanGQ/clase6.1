import os
import sys

def pausarPantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        input('Presiona Enter para continuar .....')
        
def limpiarPantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system('clear')
