from TadMenu import *
from TadAgenda import *
from TadCita import *
from TadPaciente import * 
from TadCola import *
from OperacionesMenu import *

#Primero creo la agenda vacia
agenda = crearAgenda()

while True:

    borrarPantalla()
    verMenu()
    opcion = input("\nIngrese opción seleccionada: ")
    borrarPantalla()

    if(opcion == "a"):
        opcionA(agenda)
        borrarPantalla()
        input("Presione una tecla para continuar...")
    elif(opcion == "b"):
        opcionB(agenda)
        borrarPantalla()
        input("Presione una tecla para continuar...")
    elif(opcion == "c"):
        opcionC(agenda)
        input("Presione una tecla para continuar")
    elif(opcion == "d"):
        opcionD(agenda)
        input("Presione una tecla para continuar")
    elif(opcion == "e"):
        opcionE(agenda)
        input("Presiones una tecla para continuar...")
    elif(opcion == "f"):
        opcionF(agenda) 
        input("Presiones una tecla para continuar...")           
    elif(opcion == "g"):
        opcionG(agenda)
        input("Presiones una tecla para continuar...")
    elif(opcion == "q"):
        break
    else:
        print("Opción invalida.")
        input("Presione una tecla para continuar...")
