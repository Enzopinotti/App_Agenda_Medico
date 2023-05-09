from TadMenu import *
from TadAgenda import *
from TadCita import *
from TadPaciente import * 
from TadCola import *

#Primero creo la agenda vacia
agenda = crearAgenda()

verMenu()

opcion = input("\nIngrese opción seleccionada: ")

borrarMenu()


if(opcion == "a"):

    #Primero creo el paciente vacio
    paciente = crearPaciente()
    

    #Luego cargo los datos del paciente
    nombrePaciente = input("Ingrese el nombre del paciente: ")
    apellidoPaciente = input("Ingrese el apellido del paciente: ")
    obraSocialPaciente = input("Ingrese la obra social del paciente: ")
    dniPaciente = input("Ingrese el dni del paciente: ")
    cargarPaciente(paciente, nombrePaciente, apellidoPaciente, obraSocialPaciente, dniPaciente)

    #creo la cita vacia

    cita = crearCita()

    #Luego cargo los datos a la cita
    fechaCita = input("Ingrese fecha de la cita:")
    horaCita = input("Ingrese hora de la cita:")
    cargarCita(cita,fechaCita, horaCita, paciente)

    #cargo la cita en la agenda

    agregarCita(agenda, cita)
    print("La cita fue agregada exitosamente...")

    
elif(opcion == "b"):

    #Pido los datos del paciente a modificar
    nombrePaciente = input("Ingrese el nombre del paciente al que desea modificarle la cita: ")
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea modificarle la cita: ")

    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "", "")

    for cita in agenda:
        if(existePaciente(cita, pacienteAuxiliar)):
            nuevaFecha = input("Ingrese La nueva fecha")
            modFecha(cita, nuevaFecha)
            print("La cita fue modificada exitosamente...")
        else:
            print("El paciente no tiene citas asignadas...")
            

    
elif(opcion == "c"):
    #Deseo eliminar la ultima cita cargada
    eliminarCita(agenda)
    print("La cita fue eliminada exitosamente...")


    
elif(opcion == "d"):
    print("Hola")



elif(opcion == "e"):
    #primero ingreso la fecha que quiero modificar

    fechaActual = input("Ingrese la fecha que desea modificar: ")

    #Luego ingreso la nueva fecha

    nuevaFecha = input("Ingrese la nueva fecha: ")

    #modifico todas las citas con la fecha actual a la nueva fecha

    modificarAgenda(agenda, fechaActual, nuevaFecha)
    print("La fecha fue modificada exitosamente...")
    



elif(opcion == "f"):
    #primero pido la obra social para eliminar la cita
    obraSocial = input("Ingrese la obra social de la cita que desea eliminar: ")
    eliminarCitaPorOS(agenda, obraSocial)
    print("Las citas fueron eliminadas exitosamente...")

elif(opcion == "g"):
    #primero creo una cola vacia
    cola = crearCola()
    #luego pido la fecha para la cual quiero generar la cola
    fecha = input("Ingrese la fecha de la cita que desea generar la cola: ")
    #genero la cola con la fecha ingresada


elif(opcion == "q"):
    print("Hola")
else:
    print("Opción invalida.")









