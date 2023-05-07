from TadMenu import *
from TadAgenda import *
from TadCita import *
from TadPaciente import * 

agenda = crearAgenda()

verMenu()

opcion = input("\nIngrese opción seleccionada: ")

borrarMenu()


if(opcion == "a"):
    paciente = crearPaciente()
    cita = crearCita()
    nombrePaciente = input("Ingrese el nombre del paciente: ")
    apellidoPaciente = input("Ingrese el apellido del paciente: ")
    obraSocialPaciente = input("Ingrese la obra social del paciente: ")
    cargarPaciente(paciente, nombrePaciente, apellidoPaciente, obraSocialPaciente)
    fechaCita = input("Ingrese fecha de la cita:")
    horaCita = input("Ingrese hora de la cita:")
    cargarCita(cita,fechaCita, horaCita, paciente)
    agregarCita(agenda, cita)
    print("La cita fue agregada exitosamente...")
elif(opcion == "b"):
    nombrePaciente = input("Ingrese el nombre del paciente al que desea modificarle la cita: ")
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea modificarle la cita: ")
    paciente = crearPaciente()
    cargarPaciente(paciente, nombrePaciente, apellidoPaciente, "")
    for cita in agenda:
        if(existePaciente(cita, paciente)):
            nuevaFecha = input("Ingrese La nueva fecha")
            modFecha()
    
elif(opcion == "c"):
elif(opcion == "d"):
elif(opcion == "e"):
elif(opcion == "f"):
elif(opcion == "g"):
elif(opcion == "q"):
else:
    print("Opción invalida.")









