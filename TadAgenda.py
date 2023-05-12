"""TAD AGENDA"""
from TadPaciente import *
from TadCita import *

"""ATRIBUTOS:"""
# cita: Cita

def crearAgenda():
    #retorna agenda vacia
    
    agenda=[]
    return agenda

def existeCita(agenda,cita):
    #retorna verdadero si existe la cita en la agenda
    
    return cita in agenda

def agregarCita(agenda, cita):
    #agrega tipo Cita en Agenda
    
    agenda.append(cita)

def eliminarCita(agenda):
    #eliminar tipo Cita en Agenda
    nombrePaciente = input("Ingrese el nombre del paciente al que desea eliminarle la cita: ")
    apellidoPaciente = input("Ingrese el apellido del paciente al que desea elimnarle la cita: ")

    #Creo un paciente vacio para poder cargar los datos pedidos anteriormente
    pacienteAuxiliar = crearPaciente()
    cargarPaciente(pacienteAuxiliar, nombrePaciente, apellidoPaciente, "", "")

    eliminada = False

    for cita in agenda:

        if(existePaciente(cita, pacienteAuxiliar)):
            agenda.remove(cita)
            eliminada = True
    
    return eliminada

    

    
def eliminarCitaPorOS(agenda, obraSocial):
    #eliminar tipo Cita en Agenda por obra social
    eliminadas = False
    for cita in agenda:
        if(verObraSocial(cita).lower() == obraSocial.lower()):
            agenda.remove(cita)
            eliminadas = True
            
    return eliminadas
    

def listarCitas(agenda):
    #retorna listado de citas de la agenda
    if(tamanioAgenda(agenda) > 0):
        return agenda
    else:
        print("La agenda no posee citas")       


def tamanioAgenda(agenda): 
    #retorna cantidad de citas que posee la agenda

    return len(agenda)

def modificarAgenda(agenda, fechaActual, fechaDestino, horaDestino):
    #modificar todas las citas con fechaActual a fechaDestino 
    for cita in agenda: 
        if(verFecha(cita)==fechaActual):
            modFecha(cita, fechaDestino)
            modHora(cita, horaDestino)




