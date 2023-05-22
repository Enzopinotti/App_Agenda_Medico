""" TAD COLA """

# def crearCola():
# Crea una cola vacía.
# Retorna: list.

# def esVacia(cola):
# Comprueba si una cola está vacía.
# Retorna: bool.

# def encolarElemento(cola, cita):
# Agrega un elemento al final de la cola.

# def desencolar(cola):
# Elimina el primer elemento de la cola.

# def tamanioCola(cola):
# Devuelve la cantidad de elementos en la cola.
# Retorna: int.


def crearCola(): 
    cola=[]
    return cola

def esVacia(cola):
    return (len(cola)==0) 

def encolarElemento(cola, cita):
    cola.append(cita)

def desencolar(cola):
    cola.pop()

def tamanioCola(cola):
    return len(cola)

