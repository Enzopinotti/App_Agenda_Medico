from TadAgenda import *
from TadCita import *
from TadPaciente import *
from TadCola import *
from Validaciones import *
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

    paciente = crearPaciente()

    nombrePaciente = input("Ingrese el nombre del paciente: ")
    while not validarNombreApellido(nombrePaciente):
        borrarPantalla()
        print("El nombre ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el nombre del paciente: ")

    apellidoPaciente = input("Ingrese el apellido del paciente: ")
    while not validarNombreApellido(nombrePaciente):
        borrarPantalla()
        print("El apellido ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el apellido del paciente: ")

    obraSocialPaciente = input("Ingrese la obra social del paciente: ")
    while not validarObraSocial(obraSocialPaciente):
        borrarPantalla()
        print("La obra social ingresada no es válida. Por favor, inténtelo de nuevo.")
        obraSocialPaciente = input("Ingrese la obra social del paciente: ")

    
    cargarPaciente(paciente, nombrePaciente, apellidoPaciente, obraSocialPaciente)

    cita = crearCita()

    diaCita = input("Ingrese dia de la cita (1-31): ")
    while not validarDia(diaCita):
        borrarPantalla()
        print("Dia ingresado no es válido. Por favor, inténtelo de nuevo.")
        diaCita = input("Ingrese el dia de la fecha que desea asignar un turno (1-31): ")
    mesCita = input("Ingrese mes de la cita (1-12): ")
    while not validarMes(mesCita):
        borrarPantalla()
        print("Mes ingresado no es válido. Por favor, inténtelo de nuevo.")
        mesCita = input("Ingrese el mes de la fecha que desea asignar un turno (1-12): ")
    anioCita = input("Ingrese año de la cita: ")
    while not validarAnio(anioCita):
        borrarPantalla()
        print("Año ingresado no es válido. Por favor, inténtelo de nuevo.")
        anioCita = input("Ingrese el año de la fecha que desea asignar un turno (1-31): ")

    diaCita = int(diaCita)
    mesCita = int(mesCita)
    anioCita = int(anioCita)
    fechaCita = crearFecha(anioCita,mesCita,diaCita)

    horaCita = input("Ingrese hora de la cita (0-23): ")
    while not validarHora(horaCita):
        borrarPantalla()
        print("La hora ingresada no es válida. Por favor, inténtelo de nuevo.")
        horaCita = input("Ingrese hora de la cita (0-23): ")

    minutoCita = input("Ingrese minuto de la cita (0-59): ")
    while not validarMinutos(minutoCita):
        borrarPantalla()
        print("Los minutos ingresados no son válidos. Por favor, inténtelo de nuevo.")
        horaCita = input("Ingrese minuto de la cita (0-59): ")

    horaCita = int(horaCita)
    minutoCita = int(minutoCita)
        
    horarioCita = crearHorario(horaCita,minutoCita)

    cargarCita(cita,fechaCita, horarioCita, paciente)

    #cargo la cita en la agenda

    agregarCita(agenda, cita)
    print("La cita fue agregada exitosamente...")


def opcionB(agenda):

    nombrePaciente = input("Ingrese el nombre del paciente al que desea modificarle la cita: ")
    while not validarNombreApellido(nombrePaciente):
        borrarPantalla()
        print("El nombre ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el nombre del paciente: ")
    
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea modificarle la cita: ")
    while not validarNombreApellido(apellidoPaciente):
        borrarPantalla()
        print("El apellido ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el apellido del paciente: ")

    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "")

    existeCita = False

    for cita in agenda:
        if(existePaciente(cita, pacienteAuxiliar)):
            existeCita = True
            nuevoDia = input("Ingrese el nuevo dia (1-31): ")
            while not validarDia(nuevoDia):
                borrarPantalla()
                print("Dia ingresado no es válido. Por favor, inténtelo de nuevo.")
                nuevoDia = input("Ingrese el nuevo dia (1-31): ")        
            nuevoMes = input("Ingrese el nuevo mes (1-12): ")
            while not validarMes(nuevoMes):
                borrarPantalla()
                print("Mes ingresado no es válido. Por favor, inténtelo de nuevo.")
                nuevoMes = input("Ingrese el nuevo mes (1-12): ")
            nuevoAnio = input("Ingrese el nuevo año: ")
            while not validarAnio(nuevoAnio):
                borrarPantalla()
                print("Año ingresado no es válido. Por favor, inténtelo de nuevo.")
                nuevoAnio = input("Ingrese el nuevo año: ")
            
            nuevoDia = int(nuevoDia)
            nuevoMes = int(nuevoMes)
            nuevoAnio = int(nuevoAnio)

            nuevaFecha = crearFecha(nuevoAnio,nuevoMes,nuevoDia)
            modFecha(cita,nuevaFecha)

            nuevaHora = input("Ingrese nueva hora de la cita (0-23): ")
            while not validarHora(nuevaHora):
                borrarPantalla()
                print("Hora ingresada no es válida. Por favor, inténtelo de nuevo.")
                nuevaHora = input("Ingrese nueva hora de la cita (0-23): ")
            nuevoMinuto = input("Ingrese nuevo minuto de la cita (0-59): ")
            while not validarMinutos(nuevoMinuto):
                borrarPantalla()
                print("Minuto ingresado no es válido. Por favor, inténtelo de nuevo.")
                nuevoMinuto = input("Ingrese nuevo minuto de la cita (0-59): ")

            nuevaHora = int(nuevaHora)
            nuevoMinuto = int(nuevoMinuto)

            nuevoHorario = crearHorario(nuevaHora, nuevoMinuto)
            modHora(cita,nuevoHorario)

        else:
            print("El paciente no tiene citas asignadas...")
    if(existeCita == False):
        print("El paciente ingresado no posee citas agendadas.")

def opcionC(agenda):
    nombrePaciente = input("Ingrese el nombre del paciente al que desea eliminarle la cita: ")
    while not validarNombreApellido(nombrePaciente):
        borrarPantalla()
        print("Nombre de paciente ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el nombre del paciente al que desea elminarle la cita: ")

    apellidoPaciente = input("Ingrese el apellido del paciente al que desea elimnarle la cita: ")
    while not validarNombreApellido(apellidoPaciente):
        borrarPantalla()
        print("Apellido de paciente ingresado no es válido. Por favor, inténtelo de nuevo.")
        nombrePaciente = input("Ingrese el apellido del paciente al que desea elminarle la cita: ")

    eliminada = eliminarCita(agenda, nombrePaciente, apellidoPaciente)
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
        print("-" * 110 + "\n")


def opcionE(agenda):
    #primero ingreso la fecha que quiero modificar
    diaActual = input("Ingrese el dia de la fecha que desea modificar: ")
    while not validarDia(diaActual):
        borrarPantalla()
        print("El dia ingresado no es válido. Intentelo nuevamente.")
        diaActual = input("Ingrese el dia de la fecha que desea modificar: ")
    mesActual = input("Ingrese el mes de la fecha que desea modificar: ")
    while not validarMes(mesActual):
        borrarPantalla()
        print("El mes ingresado no es válido. Intentelo nuevamente.")
        mesActual = input("Ingrese el mes de la fecha que desea modificar: ")
    anioActual = input("Ingrese el año de la fecha que desea modificar: ")
    while not validarAnio(anioActual):
        borrarPantalla()
        print("El año ingresado no es válido. Intentelo nuevamente.")
        anioActual = input("Ingrese el año de la fecha que desea modificar: ")
    
    diaActual = int(diaActual)
    mesActual = int(mesActual)
    anioActual = int(anioActual)
    fechaActual = crearFecha(anioActual,mesActual,diaActual)

    #Luego ingreso la nueva fecha
    diaDestino = input("Ingrese el dia de la fecha a la que desea correr sus citas: ")
    while not validarDia(diaDestino):
        borrarPantalla()
        print("El dia ingresado no es válido. Intentelo nuevamente.")
        diaDestino = input("Ingrese el dia de la fecha a la que desea correr sus citas: ")
    mesDestino = input("Ingrese el mes de la fecha a la que desea correr sus citas: ")
    while not validarMes(mesDestino):
        borrarPantalla()
        print("El mes ingresado no es válido. Intentelo nuevamente.")
        mesDestino = input("Ingrese el mes de la fecha a la que desea coorer sus citas: ")
    anioDestino = input("Ingrese el año de la fecha a la que desea correr sus citas: ")
    while not validarAnio(anioDestino):
        borrarPantalla()
        print("El año ingresado no es válido. Intentelo nuevamente.")
        anioDestino = input("Ingrese el año de la fecha a la que desea correr sus citas: ")

    diaDestino = int(diaDestino) 
    mesDestino = int(mesDestino)
    anioDestino = int(anioDestino)
    nuevaFecha = crearFecha(anioDestino,mesDestino,diaDestino)

    #modifico todas las citas con la fecha actual a la nueva fecha
    existeFecha = modificarAgenda(agenda, fechaActual, nuevaFecha)
    if(existeFecha):
        print("Las citas fueron modificadas correctamente")
    else:
        print("No hay citas para la fecha indicada.")


def opcionF(agenda):
    obraSocial = input("Ingrese la obra social de la cita que desea eliminar: ")
    while not validarObraSocial(obraSocial):
        borrarPantalla()
        print("La obra social ingresada no es válida. Por favor, inténtelo de nuevo.")
        obraSocial = input("Ingrese la obra social: ")

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
    diaFecha = input("Ingrese el dia de la fecha que desea generar la cola (1-31): ")
    while not validarDia(diaFecha):
        borrarPantalla()
        print("El dia ingresado no es válido. Intentelo nuevamente.")
        diaFecha = input("Ingrese el dia de la fecha que desea generar la cola (1-31): ")
    mesFecha = input("Ingrese el mes de la fecha que desea generar la cola (1-12): ")
    while not validarMes(mesFecha):
        borrarPantalla()
        print("El mes ingresado no es válido. Intentelo nuevamente.")
        mesFecha = input("Ingrese el mes de la fecha que desea generar la cola (1-12): ")
    anioFecha = input("Ingrese el año de la fecha que desea generar la cola: ")
    while not validarAnio(anioFecha):
        borrarPantalla()
        print("El año ingresado no es válido. Intentelo nuevamente.")
        anioFecha = input("Ingrese el año de la fecha que desea generar la cola: ")

    diaFecha = int(diaFecha)
    mesFecha = int(mesFecha)
    anioFecha = int(anioFecha)
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
    print("-" * 60 + "\n")
    print("-" * 60 + "\n")
    for cita in colaCitas:
        pacienteCita = verPaciente(cita)
        print("Paciente: "+verNombre(pacienteCita) +" "+ verApellido(pacienteCita))
        print("Obra social: " +verObraSocial(pacienteCita))
        print("-" * 60 + "\n")
             
