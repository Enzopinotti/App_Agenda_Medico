from TadAgenda import *
from TadCita import *
from TadPaciente import *
from TadCola import *

def opcionA(agenda):
    #Primero creo el paciente vacio
    paciente = crearPaciente()
    

    #Luego cargo los datos del paciente
    nombrePaciente = input("Ingrese el nombre del paciente: ")
    apellidoPaciente = input("Ingrese el apellido del paciente: ")
    obraSocialPaciente = input("Ingrese la obra social del paciente: ")
    
    cargarPaciente(paciente, nombrePaciente, apellidoPaciente, obraSocialPaciente)

    #creo la cita vacia

    cita = crearCita()

    #Luego cargo los datos a la cita
    fechaCita = input("Ingrese fecha de la cita:")
    horaCita = input("Ingrese hora de la cita:")
    cargarCita(cita,fechaCita, horaCita, paciente)

    #cargo la cita en la agenda

    agregarCita(agenda, cita)

def opcionB(agenda):
    #Pido los datos del paciente a modificar
    nombrePaciente = input("Ingrese el nombre del paciente al que desea modificarle la cita: ")
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea modificarle la cita: ")

    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "", "")

    for cita in agenda:
        if(existePaciente(cita, pacienteAuxiliar)):
            nuevaFecha = input("Ingrese La nueva fecha: ")
            modFecha(cita,nuevaFecha)
            nuevaHora = input("Ingrese La nueva hora: ")
            modHora(cita,nuevaHora)
        else:
            print("El paciente no tiene citas asignadas...")

def opcionC(agenda):
    eliminada = eliminarCita(agenda)
    if(eliminada):
        print("La cita fue eliminada correctamente.")
    else:
        print("El paciente no tiene citas asignadas.")

def opcionD(agenda):
    citasParaListar = listarCitas(agenda)
    for cita in citasParaListar:
        pacienteCita = verPaciente(cita)
        print("El paciente llamado: "+verNombre(pacienteCita) +" "+ verApellido(pacienteCita))
        print("Cuya obra social es " +verObraSocial(pacienteCita))
        print("Posee una cita el dia " +verFecha(cita)+ " a las "+verHora(cita)+"hs.")
        print("-" * 60 + "\n")
    input("Ingrese una tecla para continuar")

def opcionE(agenda):
    #primero ingreso la fecha que quiero modificar
    fechaActual = input("Ingrese la fecha que desea modificar: ")
    #Luego ingreso la nueva fecha
    nuevaFecha = input("Ingrese la nueva fecha: ")
    nuevaHora = input("Ingrese la nueva hora: ")
    #modifico todas las citas con la fecha actual a la nueva fecha
    modificarAgenda(agenda, fechaActual, nuevaFecha, nuevaHora)

def opcionF(agenda):
    #primero pido la obra social para eliminar la cita
    obraSocial = input("Ingrese la obra social de la cita que desea eliminar: ")
    eliminadas = eliminarCitaPorOS(agenda, obraSocial)
    if(eliminadas):
        print("Las citas fueron eliminadas exitosamente...")
    else:
        print("No existen citas con esa obra social...")

def opcionG(agenda):
    #primero creo una cola vacia
    cola = crearCola()
    #luego pido la fecha para la cual quiero generar la cola
    fecha = input("Ingrese la fecha de la cita que desea generar la cola: ")
    #genero la cola con la fecha ingresada

    for cita in agenda:
        if(verFecha(cita) == fecha):
            encolarElemento(cola, cita)

    colaCitas = listarCitas(cola)
    
    print("Turnos registrados para la fecha: " + fecha)
    for cita in colaCitas:
        pacienteCita = verPaciente(cita)
        print("El paciente llamado: "+verNombre(pacienteCita) +" "+ verApellido(pacienteCita))
        print("Cuya obra social es " +verObraSocial(pacienteCita))
        print("-" * 60 + "\n")
             
    input("Ingrese una tecla para continuar")