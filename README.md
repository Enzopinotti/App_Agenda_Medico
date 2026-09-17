# Agenda Médica — TADs en Python

Proyecto académico colaborativo de 2023 para practicar **Tipos Abstractos de Datos (TADs), estructuras de datos, modularización y validaciones en Python** mediante una agenda de turnos médicos.

La modernización 2026 preserva ese objetivo. No convierte el ejercicio en una aplicación web, no agrega base de datos, autenticación ni infraestructura innecesaria: crea una autoridad mantenible y testeada junto al material histórico.

## Historia y autoridad

### Baseline histórico 2023

La versión original queda fijada por el commit:

```text
390ac3591b089e0aefd6dc5f971c3e8d22e57794
```

Ese commit conserva el trabajo colaborativo original, incluyendo contribuciones de **Francisco L. Sabato**, y los módulos:

- `App.py`
- `OperacionesMenu.py`
- `TadPaciente.py`
- `TadCita.py`
- `TadCola.py`
- `TadAgenda.py`
- `Validaciones.py`
- `readme.md` con la especificación original de TADs

La historia no se reescribe: cualquier diferencia de comportamiento entre 2023 y 2026 debe poder explicarse y probarse.

### Autoridad mantenida 2026

El código mantenido vive bajo:

```text
modern/agenda_medica/
```

Usa únicamente la biblioteca estándar de Python para que el foco siga puesto en estructuras de datos y modelado:

- `dataclass` para entidades explícitas;
- `datetime.date` / `datetime.time` para fechas y horarios válidos;
- `collections.deque` para una cola FIFO real;
- tests con `unittest`;
- GitHub Actions para Python 3.12, 3.13 y 3.14.

## Qué modela la versión 2026

### `Paciente`

Nombre, apellido y obra social con normalización básica de texto y rechazo de campos vacíos.

### `Cita`

Asocia un paciente a una fecha y horario usando tipos estándar de Python, evitando representar una cita como una lista posicional sin contrato.

### `Agenda`

Mantiene las operaciones académicas centrales del ejercicio:

- agregar y listar citas;
- buscar citas por paciente;
- reprogramar citas de un paciente;
- eliminar citas por paciente;
- eliminar citas por obra social;
- trasladar todas las citas de una fecha a otra preservando el horario;
- generar una cola con las citas de un día.

### `ColaCitas`

Implementa FIFO explícitamente con `deque.popleft()`.

Esto corrige un defecto histórico concreto: `TadCola.desencolar()` usaba `pop()` sin índice, por lo que removía el último elemento (LIFO) aunque la estructura se llamaba cola.

## Ejecutar la autoridad 2026

No hay dependencias runtime externas.

Desde la raíz:

```bash
PYTHONPATH=modern python -m unittest discover -s modern/tests -v
```

También se puede ejecutar la interfaz de consola mantenida:

```bash
PYTHONPATH=modern python -m agenda_medica
```

## Ejecutar el ejercicio histórico

Para estudiar el comportamiento original:

```bash
python App.py
```

El código histórico se mantiene por contexto educativo; no se presenta como la implementación recomendada para reutilización actual.

## Diferencias deliberadas 2023 → 2026

| 2023 | 2026 |
| --- | --- |
| Paciente/cita representados mediante listas posicionales | `dataclass` con campos explícitos |
| Cola con `list` + `pop()` | FIFO real con `deque.popleft()` |
| Validaciones manuales de día/mes/hora | tipos `date` / `time` de Python |
| Mutación directa dispersa | operaciones encapsuladas en `Agenda` |
| Sin tests permanentes | regresión y comportamiento con `unittest` |
| `__pycache__` versionado | artefactos Python ignorados |
| README centrado sólo en firma de TADs | portada, historia, ejecución y límites claros |

## No-adopciones deliberadas

Esta modernización **no** agrega:

- Django / Flask / FastAPI;
- frontend web;
- base de datos;
- autenticación;
- Docker;
- servicios cloud.

Ninguno de esos componentes mejora el objetivo académico de este repositorio.

## Seguimiento

- Issue de modernización: [#4](https://github.com/Enzopinotti/App_Agenda_Medico/issues/4)
- Programa central: [`Enzopinotti/Enzopinotti#19`](https://github.com/Enzopinotti/Enzopinotti/issues/19)

## Autoría

Repositorio iniciado y coordinado por **Enzo Pinotti**, con trabajo colaborativo preservado en el historial Git original.
