def validarDia(dia):
    if not dia.isdigit():
        return False
    dia = int(dia)
    return 1 <= dia <= 31

def validarMes(mes):
    if not mes.isdigit():
        return False
    mes = int(mes)
    return 1 <= mes <= 12

def validarAnio(anio):
    if not anio.isdigit():
        return False
    anio = int(anio)
    return 2000 <= anio <= 2099

def validarNombreApellido(nombre_apellido):
    return nombre_apellido.isalpha()

def validarObraSocial(obra_social):
    return obra_social.replace(' ', '').isalpha()

def validarHora(hora):
    if not hora.isdigit():
        return False
    hora = int(hora)
    return 0 <= hora <= 23

def validarMinutos(minutos):
    if not minutos.isdigit():
        return False
    minutos = int(minutos)
    return 0 <= minutos <= 59
