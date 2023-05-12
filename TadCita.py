"""TAD CITA"""

from datetime import *
from TadPaciente import *

# def crearHorario(hora,minuto):
# Crea un tipo de dato horario a partir de una hora y un minuto.

# def crearFecha(anio,mes,dia):
# Crea un tipo de dato fecha a partir de un año, mes y día.

# def verHora(horario):
# Devuelve la hora de un horario.

# def verMinuto(horario):
# Devuelve el minuto de un horario.

# def verAnio(fecha):
# Devuelve el año de una fecha.

# def verMes(fecha):
# Devuelve el mes de una fecha.

# def verDia(fecha):
# Devuelve el día de una fecha.

# def crearCita():
# Crea una cita vacía.
# Retorna: Cita.

# def cargarCita(cita, fecha, hora, paciente):
# Carga una fecha, una hora y un tipo Paciente a una cita.

# def verFecha(cita):
# Devuelve la fecha de una cita.

# def verHorario(cita):
# Devuelve el horario de una cita.

# def verPaciente(cita):
# Devuelve el tipo Paciente de una cita.

# def modFecha(cita, nuevaFecha):
# Modifica la fecha de una cita.

# def modHora(cita, nuevaHora):
# Modifica la hora de una cita.

# def modPaciente(cita, nuevoPaciente):
# Modifica el tipo Paciente de una cita.

# def existePaciente(cita, paciente):
# Comprueba si un paciente específico está en una cita.
# Retorna: bool.


def crearHorario(hora,minuto):
    return time(hora,minuto)
 
def crearFecha(anio,mes,dia):
    return datetime(anio,mes,dia)

def verHora(horario):
    return str(horario.hour)

def verMinuto(horario):
    return str(horario.minute)

def verAnio(fecha):
    return str(fecha.year)

def verMes(fecha):
    return str(fecha.month)

def verDia(fecha):
    return str(fecha.day)

def crearCita():
    #   retorna cita vacia
    Cita=[datetime,time,[]]
    return Cita

def cargarCita(cita, fecha, hora, paciente):
    cita[0]=fecha
    cita[1]=hora
    cita[2]=paciente 

def verFecha(cita):
    return cita[0]

def verHorario(cita):
    return cita[1]

def verPaciente(cita):
    return cita[2]

def modFecha(cita, nuevaFecha):
    cita[0] = nuevaFecha


def modHora(cita, nuevaHora):
    cita[1] = nuevaHora

def modPaciente(cita, nuevoPaciente):
    cita[2] = nuevoPaciente

    
def existePaciente(cita, paciente):    
    if ( verNombre(cita[2]).lower() == verNombre(paciente).lower() and verApellido(cita[2]).lower() == verApellido(paciente).lower()):
        return True
    else:
        return False

    








