import random
import os

# Nombre del archivo que almacenará los números utilizados
FILENAME = "numeros_utilizados.txt"

def obtener_numeros_utilizados():
    """Lee los números utilizados del archivo y los devuelve como un conjunto."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            numeros = {int(line.strip()) for line in file}
    else:
        numeros = set()
    return numeros

def guardar_numero_utilizado(numero):
    """Guarda un número en el archivo de números utilizados."""
    with open(FILENAME, "a") as file:
        file.write(f"{numero}\n")

def obtener_numero_aleatorio():
    """Obtiene un número aleatorio que no ha sido utilizado antes."""
    numeros_utilizados = obtener_numeros_utilizados()
    numeros_disponibles = set(range(1, 366)) - numeros_utilizados
    
    if not numeros_disponibles:
        print("Todos los números del 1 al 365 ya han sido utilizados.")
        return None
    
    numero_aleatorio = random.choice(list(numeros_disponibles))
    guardar_numero_utilizado(numero_aleatorio)
    return numero_aleatorio

# Ejecución del programa
numero = obtener_numero_aleatorio()
if numero is not None:
    print(f"El número aleatorio seleccionado es: {numero}")
