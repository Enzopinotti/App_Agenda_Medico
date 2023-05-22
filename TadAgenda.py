"""TAD AGENDA"""
from TadPaciente import *
from TadCita import *

# def crearAgenda():
# Crea una nueva agenda vacía.
# Retorna: list vacía.

# def existeCita(agenda,cita):
# Comprueba si una cita existe en la agenda.
# Parámetros: agenda (list), cita (Cita).
# Retorna: bool.

# def agregarCita(agenda, cita):
# Agrega una cita a la agenda.
# Parámetros: agenda (list), cita (Cita).

# def eliminarCita(agenda):
# Solicita el nombre y apellido del paciente y elimina su cita de la agenda.
# Parámetro: agenda (list).
# Retorna: bool.

# def eliminarCitaPorOS(agenda, obraSocial):
# Elimina todas las citas de la agenda que pertenezcan a una obra social específica.
# Parámetros: agenda (list), obraSocial (str).
# Retorna: bool.

# def listarCitas(agenda):
# Devuelve la lista de citas en la agenda.
# Parámetro: agenda (list).
# Retorna: list.

# def tamanioAgenda(agenda):
# Devuelve la cantidad de citas en la agenda.
# Parámetro: agenda (list).
# Retorna: int.

# def modificarAgenda(agenda, fechaActual, fechaDestino):
# Modifica todas las citas con una fecha específica a una nueva fecha y hora.
# Parámetros: agenda (list), fechaActual (datetime), fechaDestino (datetime).
# Retorna: bool.

# def borrarCita(agenda, cita):
# Elimina una cita específica de la agenda.
# Parámetros: agenda (list), cita (Cita).



def crearAgenda():    
    agenda=[]
    return agenda

def existeCita(agenda,cita):
    return cita in agenda

def agregarCita(agenda, cita):    
    agenda.append(cita)

def eliminarCita(agenda, nombrePaciente, apellidoPaciente):
    
    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "")
    eliminada = False
    for cita in agenda:
        if(existePaciente(cita, pacienteAuxiliar)):
            agenda.remove(cita)
            eliminada = True   
    return eliminada

 
def eliminarCitaPorOS(agenda, obraSocial):
    eliminadas = False
    for cita in agenda.copy():
        if(verObraSocial(verPaciente(cita)).lower() == obraSocial.lower()):
            borrarCita(agenda, cita)
            eliminadas = True
    return eliminadas
    

def listarCitas(agenda):
    return agenda       


def tamanioAgenda(agenda): 
    return len(agenda)

def modificarAgenda(agenda, fechaActual, fechaDestino):
    existeFecha = False
    for cita in agenda: 
        if(verFecha(cita)==fechaActual):
            modFecha(cita, fechaDestino)
            existeFecha=True
    return existeFecha

def borrarCita(agenda, cita):
    agenda.remove(cita)

