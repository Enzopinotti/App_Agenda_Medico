INTRODUCCIÓN

Este documento se centra en proporcionar especificaciones detalladas de los Tipos Abstractos de Datos (TADs) que se utilizan en esta apliación de gestión de agendas médicas codificada en lenguaje Python.

En este documento se tratarán los siguientes TADs:
1. TAD Paciente
2. TAD Cita
3. TAD Cola
4. TAD Agenda

Para cada uno de estos TADs, se proporcionará una descripción detallada de sus métodos, incluyendo su propósito, los parámetros que requieren, y los valores que devuelven.

**(Aclaración)**   '->' : tipo de dato que retorna el método, en caso de hacerlo ('None' por ej. no retorna uno).

-----------------------------------------------------------------------------------------------------------------

1. TAD Paciente

Este módulo define un Tipo Abstracto de Datos (TAD) que representa a un paciente. El TAD Paciente proporciona una serie de operaciones para la gestión de un paciente.

Métodos:

crearPaciente() -> list
Este método crea e inicializa un paciente como una lista vacía con tres elementos.
Retorna: Una lista que representa a un paciente con campos para el nombre, apellido y obra social, inicializados a una cadena de caracteres vacía.

cargarPaciente(paciente: list, nombre: str, apellido: str, obraSocial: str) -> None
Este método carga la información del paciente (nombre, apellido y obra social) en la lista que representa a un paciente.
paciente: La lista que representa a un paciente.
nombre: El nombre del paciente a cargar.
apellido: El apellido del paciente a cargar.
obraSocial: La obra social del paciente a cargar.

verNombre(paciente: list) -> str
Este método devuelve el nombre del paciente.
paciente: La lista que representa a un paciente.
Retorna: El nombre del paciente.

verApellido(paciente: list) -> str
Este método devuelve el apellido del paciente.
paciente: La lista que representa a un paciente.
Retorna: El apellido del paciente.

verObraSocial(paciente: list) -> str
Este método devuelve la obra social del paciente.
paciente: La lista que representa a un paciente.
Retorna: La obra social del paciente.

modNombre(paciente: list, nombre: str) -> None
Este método modifica el nombre del paciente.
paciente: La lista que representa a un paciente.
nombre: El nuevo nombre del paciente.

modApellido(paciente: list, apellido: str) -> None
Este método modifica el apellido del paciente.
paciente: La lista que representa a un paciente.
apellido: El nuevo apellido del paciente.

modObraSocial(paciente: list, obraSocial: str) -> None
Este método modifica la obra social del paciente.
paciente: La lista que representa a un paciente.
obraSocial: La nueva obra social del paciente.

asignarPaciente(paciente1: list, paciente2: list) -> None
Este método asigna la información de un paciente a otro paciente.
paciente1: La lista que representa al primer paciente.
paciente2: La lista que representa al segundo paciente, cuya información se asignará al primer paciente.

-----------------------------------------------------------------------------------------------------------------

2. TAD Cita

Este módulo define un Tipo Abstracto de Datos (TAD) que representa a una cita en un sistema de salud. El TAD Cita proporciona una serie de operaciones para la gestión de una cita.

Métodos

crearHorario(hora: int, minuto: int) -> datetime.time
Este método crea e inicializa un horario con una hora y un minuto especificados.
Retorna: Un objeto time de la biblioteca datetime que representa el horario de la cita.

crearFecha(anio: int, mes: int, dia: int) -> datetime.datetime
Este método crea e inicializa una fecha con un año, mes y día especificados.
Retorna: Un objeto datetime de la biblioteca datetime que representa la fecha de la cita.

verHora(horario: datetime.time) -> str
Este método devuelve la hora de un horario.
Retorna: Una cadena que representa la hora de un horario.

verMinuto(horario: datetime.time) -> str
Este método devuelve el minuto de un horario.
Retorna: Una cadena que representa el minuto de un horario.

verAnio(fecha: datetime.datetime) -> str
Este método devuelve el año de una fecha.
Retorna: Una cadena que representa el año de una fecha.

verMes(fecha: datetime.datetime) -> str
Este método devuelve el mes de una fecha.
Retorna: Una cadena que representa el mes de una fecha.

verDia(fecha: datetime.datetime) -> str
Este método devuelve el día de una fecha.
Retorna: Una cadena que representa el día de una fecha.

crearCita() -> list
Este método crea e inicializa una cita como una lista vacía con tres elementos.
Retorna: Una lista que representa a una cita con campos para la fecha, hora y paciente.

cargarCita(cita: list, fecha: datetime.datetime, hora: datetime.time, paciente: list) -> None
Este método carga la información de una cita (fecha, hora y paciente) en la lista que representa a una cita.

cita: La lista que representa a una cita.
fecha: La fecha de la cita.
hora: La hora de la cita.
paciente: La lista que representa a un paciente.
verFecha(cita: list) -> datetime.datetime
Este método devuelve la fecha de una cita.
Retorna: Un objeto datetime que representa la fecha de una cita.

verHorario(cita: list) -> datetime.time
Este método devuelve el horario de una cita.
Retorna: Un objeto time que representa el horario de una cita.

verPaciente(cita: list) -> list
Este método devuelve el paciente de una cita.
Retorna: Una lista que representa al paciente de una cita.

modFecha(cita: list, nuevaFecha: datetime.datetime) -> None
Este método modifica la fecha de una cita.

cita: La lista que representa a una cita.
nuevaFecha: La nueva fecha de la cita.
modHora(cita: list, nuevaHora: datetime.time) -> None
Este método modifica la hora de una cita.

cita: La lista que representa a una cita.
nuevaHora: La nueva hora de la cita.
modPaciente(cita: list, nuevoPaciente: list) -> None
Este método modifica el paciente de una cita.

cita: La lista que representa a una cita.
nuevoPaciente: La nueva lista que representa a un paciente.
existePaciente(cita: list, paciente: list) -> bool
Este método comprueba si un paciente específico está en una cita.
Retorna: True si el paciente está en la cita, False en caso contrario.

-----------------------------------------------------------------------------------------------------------------

3. TAD Cola

Este módulo define un Tipo Abstracto de Datos (TAD) que representa una cola de citas en un sistema de salud. El TAD Cola proporciona una serie de operaciones para la gestión de una cola.

Métodos

crearCola() -> list
Este método crea e inicializa una cola como una lista vacía.
Retorna: Una lista que representa a una cola de citas.

esVacia(cola: list) -> bool
Este método comprueba si una cola está vacía.
Retorna: True si la cola está vacía, False en caso contrario.

encolarElemento(cola: list, cita: list) -> None
Este método agrega un elemento al final de la cola.

cola: La lista que representa a una cola de citas.
cita: La lista que representa a una cita.
desencolar(cola: list) -> None
Este método elimina el primer elemento de la cola.

cola: La lista que representa a una cola de citas.
tamanioCola(cola: list) -> int
Este método devuelve la cantidad de elementos en la cola.
Retorna: Un entero que representa la cantidad de elementos en la cola.

-----------------------------------------------------------------------------------------------------------------

4. TAD Agenda

Este módulo define un Tipo Abstracto de Datos (TAD) que representa una agenda de citas en un sistema de salud. El TAD Agenda proporciona una serie de operaciones para la gestión de una agenda.

Métodos

crearAgenda() -> list
Este método crea e inicializa una agenda como una lista vacía.
Retorna: Una lista que representa a una agenda de citas.

existeCita(agenda: list, cita: list) -> bool
Este método comprueba si una cita existe en la agenda.

agenda: La lista que representa a una agenda de citas.
cita: La lista que representa a una cita.
Retorna: True si la cita existe en la agenda, False en caso contrario.

agregarCita(agenda: list, cita: list) -> None
Este método agrega una cita a la agenda.

agenda: La lista que representa a una agenda de citas.
cita: La lista que representa a una cita.
eliminarCita(agenda: list) -> bool
Este método solicita el nombre y apellido del paciente y elimina su cita de la agenda. Retorna True si se eliminó la cita, False en caso contrario.

agenda: La lista que representa a una agenda de citas.
eliminarCitaPorOS(agenda: list, obraSocial: str) -> bool
Este método elimina todas las citas de la agenda que pertenezcan a una obra social específica. Retorna True si se eliminaron citas, False en caso contrario.

agenda: La lista que representa a una agenda de citas.
obraSocial: La obra social de las citas a eliminar.
listarCitas(agenda: list) -> list
Este método devuelve la lista de citas en la agenda.
Retorna: La lista de citas en la agenda.

tamanioAgenda(agenda: list) -> int
Este método devuelve la cantidad de citas en la agenda.
Retorna: Un entero que representa la cantidad de citas en la agenda.

modificarAgenda(agenda: list, fechaActual: datetime, fechaDestino: datetime) -> bool
Este método modifica todas las citas con una fecha específica a una nueva fecha y hora. Retorna True si se modificaron citas, False en caso contrario.

agenda: La lista que representa a una agenda de citas.
fechaActual: La fecha actual de las citas.
fechaDestino: La nueva fecha para las citas.
borrarCita(agenda: list, cita: list) -> None
Este método elimina una cita específica de la agenda.

agenda: La lista que representa a una agenda de citas.
cita: La lista que representa a una cita.