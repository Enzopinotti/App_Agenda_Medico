"""TAD PACIENTE"""

# def crearPaciente():
# Crea un paciente vacío.
# Retorna: Paciente.

# def cargarPaciente(paciente, nombre, apellido, obraSocial):
# Carga un nombre, un apellido y una obra social a un paciente.

# def verNombre(paciente):
# Devuelve el nombre de un paciente.

# def verApellido(paciente):
# Devuelve el apellido de un paciente.

# def verObraSocial(paciente):
# Devuelve la obra social de un paciente.

# def modNombre(paciente, nombre):
# Modifica el nombre de un paciente.

# def modApellido(paciente, apellido):
# Modifica el apellido de un paciente.

# def modObraSocial(paciente, obraSocial):
# Modifica la obra social de un paciente.

# def asignarPaciente(paciente1, paciente2):
# Asigna un paciente a otro paciente.



def crearPaciente():
    paciente = ["","",""]   
    return paciente

def cargarPaciente(paciente, nombre, apellido, obraSocial):    
    paciente[0] = nombre
    paciente[1] = apellido
    paciente[2] = obraSocial 
    

def verNombre(paciente):
    return paciente[0]

def verApellido(paciente):
    return paciente[1]

def verObraSocial(paciente):
    return paciente[2]


def modNombre(paciente, nombre):
    paciente[0] = nombre

def modApellido(paciente, apellido):
    paciente[1] = apellido

def modObraSocial(paciente, obraSocial):
    paciente[2] = obraSocial


def asignarPaciente(paciente1, paciente2):
    paciente1[0] = paciente2[0]
    paciente1[1] = paciente2[1]
    paciente1[2] = paciente2[2]
    