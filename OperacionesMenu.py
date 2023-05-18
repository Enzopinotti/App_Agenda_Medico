from TadAgenda import *
from TadCita import *
from TadPaciente import *
from TadCola import *
import os

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

def borrarPantalla():
    os.system("cls")


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
    diaCita = int(input("Ingrese dia de la cita (1-31): "))
    mesCita = int(input("Ingrese mes de la cita (1-12): "))
    anioCita = int(input("Ingrese año de la cita (20xx): "))
    fechaCita = crearFecha(anioCita,mesCita,diaCita)

    horaCita = int(input("Ingrese hora de la cita (0-23): "))
    minutoCita = int(input("Ingrese minuto de la cita (0-59): "))
    horarioCita = crearHorario(horaCita,minutoCita)

    cargarCita(cita,fechaCita, horarioCita, paciente)

    #cargo la cita en la agenda

    agregarCita(agenda, cita)
    print("La cita fue agregada exitosamente...")


def opcionB(agenda):
    #Pido los datos del paciente a modificar
    nombrePaciente = input("Ingrese el nombre del paciente al que desea modificarle la cita: ")
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea modificarle la cita: ")

    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "")

    for cita in agenda:
        if(existePaciente(cita, pacienteAuxiliar)):
            nuevoDia = int(input("Ingrese el nuevo dia (1-31): "))
            nuevoMes = int(input("Ingrese el nuevo mes (1-12): "))
            nuevoAnio = int(input("Ingrese el nuevo año (20xx): "))
            nuevaFecha = crearFecha(nuevoAnio,nuevoMes,nuevoDia)
            modFecha(cita,nuevaFecha)
            nuevaHora = int(input("Ingrese nueva hora de la cita (0-23): "))
            nuevoMinuto = int(input("Ingrese nuevo minuto de la cita (0-59): "))
            nuevoHorario = crearHorario(nuevaHora, nuevoMinuto)
            modHora(cita,nuevoHorario)
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

    if(tamanioAgenda(citasParaListar)==0):
        print("La agenda no posee citas")
        return
    
    for cita in citasParaListar:
        pacienteCita = verPaciente(cita)
        print("El paciente llamado: "+verNombre(pacienteCita) +" "+ verApellido(pacienteCita))
        print("Cuya obra social es " +verObraSocial(pacienteCita))
        print("Posee una cita el dia " +verDia(verFecha(cita))+"-"+verMes(verFecha(cita))+" a las "+verHora(verHorario(cita))+":"+verMinuto(verHorario(cita))+"hs.")
        print("-" * 60 + "\n")


def opcionE(agenda):
    #primero ingreso la fecha que quiero modificar
    diaActual = int(input("Ingrese el dia de la fecha que desea modificar: "))
    mesActual = int(input("Ingrese el mes de la fecha que desea modificar: "))
    anioActual = int(input("Ingrese el año de la fecha que desea modificar: "))
    fechaActual = crearFecha(anioActual,mesActual,diaActual)
    #Luego ingreso la nueva fecha
    diaDestino = int(input("Ingrese el dia de la fecha a la que desea correr sus citas: "))
    mesDestino = int(input("Ingrese el mes de la fecha a la que desea correr sus citas: "))
    anioDestino = int(input("Ingrese el año de la fecha a la que desea correr sus citas: "))
    nuevaFecha = crearFecha(anioDestino,mesDestino,diaDestino)

    #modifico todas las citas con la fecha actual a la nueva fecha
    existeFecha = modificarAgenda(agenda, fechaActual, nuevaFecha)
    if(existeFecha):
        print("Las citas fueron modificadas correctamente")
    else:
        print("No hay citas para la fecha indicada.")


def opcionF(agenda):
    #primero pido la obra social para eliminar la cita
    obraSocial = input("Ingrese la obra social de la cita que desea eliminar: ")
    eliminadas = eliminarCitaPorOS(agenda, obraSocial)
    if(eliminadas):
        print("Las citas de la obra social " +obraSocial+" fueron eliminadas correctamente.")
    else:
        print("No existen citas con esa obra social...")


def opcionG(agenda):
    #primero creo una cola vacia
    if(tamanioAgenda(agenda) == 0):
        print("La agenda no posee citas.")
        return
    
    cola = crearCola()
    #luego pido la fecha para la cual quiero generar la cola
    diaFecha = int(input("Ingrese el dia de la fecha que desea generar la cola (1-31): "))
    mesFecha = int(input("Ingrese el mes de la fecha que desea generar la cola (1-12): "))
    anioFecha = int(input("Ingrese el año de la fecha que desea generar la cola (20xx): "))

    fecha = crearFecha(anioFecha,mesFecha,diaFecha)
    #genero la cola con la fecha ingresada


    for cita in agenda:
        if(verFecha(cita) == fecha):
            encolarElemento(cola, cita)

    if(esVacia(cola)):
        print("No hay citas para la fecha indicada.")
        return

    colaCitas = listarCitas(cola)
    borrarPantalla()
    print("-" * 60 )
    print("Turnos registrados para la fecha: " + verAnio(fecha)+"-"+verMes(fecha)+"-"+verDia(fecha)+ "\n")
    for cita in colaCitas:
        pacienteCita = verPaciente(cita)
        print("El paciente llamado: "+verNombre(pacienteCita) +" "+ verApellido(pacienteCita))
        print("Cuya obra social es " +verObraSocial(pacienteCita))
        print("-" * 60 + "\n")
             
