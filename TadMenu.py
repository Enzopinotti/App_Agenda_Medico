""" TAD MENU """

import os

""" def verMenu(): """

# despliega menú en pantalla

""" def borrarMenu(): """

# limpia el menú de la pantalla

def verMenu():
    print("\n" + "=" * 60)
    print(" " * 20 + "Menú de opciones")
    print("=" * 60 + "\n")

    print("a) Agregar cita")
    print("b) Modificar fecha y hora de la cita con un nombre dado")
    print("c) Eliminar cita")
    print("d) Listado de citas")
    print("e) Pasar todas las citas de un día determinado a otro dado")
    print("f) Eliminar las citas de una obra social dada")
    print("g) Generar una cola con todos los nombres y obra social de los pacientes que se atiendan en un día específico")
    print("q) Salir\n")

    print("-" * 60)

def borrarMenu():
    os.system("cls")


    








