"""TAD PACIENTE"""

"""ATRIBUTOS:"""
# nombre: string
# apellido: string
# obraSocial: string
# dni: string

def crearPaciente():
    #retorna paciente vacio
    
    paciente = ["","","",""]   
    return paciente

def cargarPaciente(paciente, nombre, apellido, obraSocial, dni):
    # Rargar nombre, apellido y obra social del paciente
    
    paciente[0] = nombre
    paciente[1] = apellido
    paciente[2] = obraSocial 
    paciente[3] = dni 

def verNombre(paciente):
    # Retorna el nombre del paciente
    
    return paciente[0]

def verApellido(paciente):
    # Retorna el apellido del paciente
    
     return paciente[1]

def verObraSocial(paciente):
    # Retorna nombre de la obra social del paciente

    return paciente[2]

def verDni(paciente):
    # Retorna Dni del paciente

    return paciente[3]

def modNombre(paciente, nombre):
    #Cambia el nombre del paciente enviado por parametro

    paciente[0] = nombre

def modApellido(paciente, apellido):
    #Cambia el apellido del paciente enviado por parametro

    paciente[1] = apellido

def modObraSocial(paciente, obraSocial):
    #Cambia la obra social del paciente enviado por parametro

    paciente[2] = obraSocial

def modDni(paciente, dni):
    #Cambia la obra social del paciente enviado por parametro

    paciente[3] = dni

def asignarPaciente(paciente1, paciente2):
    #Asigna el paciente1 al paciente 2
    
    paciente1 = paciente2
    