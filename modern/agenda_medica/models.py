from __future__ import annotations

from collections import deque
from dataclasses import dataclass, replace
from datetime import date, time
from typing import Iterator


def _texto_requerido(valor: str, campo: str) -> str:
    normalizado = " ".join(valor.strip().split())
    if not normalizado:
        raise ValueError(f"{campo} no puede estar vacío")
    return normalizado


@dataclass(frozen=True, slots=True)
class Paciente:
    nombre: str
    apellido: str
    obra_social: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "nombre", _texto_requerido(self.nombre, "nombre"))
        object.__setattr__(self, "apellido", _texto_requerido(self.apellido, "apellido"))
        object.__setattr__(
            self,
            "obra_social",
            _texto_requerido(self.obra_social, "obra_social"),
        )

    @property
    def identidad(self) -> tuple[str, str]:
        return (self.nombre.casefold(), self.apellido.casefold())


@dataclass(frozen=True, slots=True)
class Cita:
    paciente: Paciente
    fecha: date
    horario: time


class ColaCitas:
    """Cola FIFO explícita para turnos médicos."""

    def __init__(self, citas: Iterator[Cita] | None = None) -> None:
        self._items: deque[Cita] = deque(citas or ())

    def encolar(self, cita: Cita) -> None:
        self._items.append(cita)

    def desencolar(self) -> Cita:
        if not self._items:
            raise IndexError("la cola de citas está vacía")
        return self._items.popleft()

    def es_vacia(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[Cita]:
        return iter(tuple(self._items))


class Agenda:
    """Agenda en memoria que preserva las operaciones centrales del ejercicio 2023."""

    def __init__(self, citas: Iterator[Cita] | None = None) -> None:
        self._citas: list[Cita] = list(citas or ())

    def agregar(self, cita: Cita) -> None:
        self._citas.append(cita)

    def listar(self) -> tuple[Cita, ...]:
        """Devuelve una vista inmutable para no exponer la lista interna."""
        return tuple(self._citas)

    def buscar_por_paciente(self, nombre: str, apellido: str) -> tuple[Cita, ...]:
        identidad = (nombre.strip().casefold(), apellido.strip().casefold())
        return tuple(
            cita for cita in self._citas if cita.paciente.identidad == identidad
        )

    def reprogramar_paciente(
        self,
        nombre: str,
        apellido: str,
        nueva_fecha: date,
        nuevo_horario: time,
    ) -> int:
        identidad = (nombre.strip().casefold(), apellido.strip().casefold())
        modificadas = 0
        actualizadas: list[Cita] = []
        for cita in self._citas:
            if cita.paciente.identidad == identidad:
                actualizadas.append(
                    replace(cita, fecha=nueva_fecha, horario=nuevo_horario)
                )
                modificadas += 1
            else:
                actualizadas.append(cita)
        self._citas = actualizadas
        return modificadas

    def eliminar_paciente(self, nombre: str, apellido: str) -> int:
        identidad = (nombre.strip().casefold(), apellido.strip().casefold())
        anteriores = len(self._citas)
        self._citas = [
            cita for cita in self._citas if cita.paciente.identidad != identidad
        ]
        return anteriores - len(self._citas)

    def eliminar_por_obra_social(self, obra_social: str) -> int:
        objetivo = _texto_requerido(obra_social, "obra_social").casefold()
        anteriores = len(self._citas)
        self._citas = [
            cita
            for cita in self._citas
            if cita.paciente.obra_social.casefold() != objetivo
        ]
        return anteriores - len(self._citas)

    def trasladar_fecha(self, origen: date, destino: date) -> int:
        modificadas = 0
        actualizadas: list[Cita] = []
        for cita in self._citas:
            if cita.fecha == origen:
                actualizadas.append(replace(cita, fecha=destino))
                modificadas += 1
            else:
                actualizadas.append(cita)
        self._citas = actualizadas
        return modificadas

    def cola_del_dia(self, fecha: date) -> ColaCitas:
        """Preserva el orden de alta y lo expresa como una cola FIFO real."""
        return ColaCitas(cita for cita in self._citas if cita.fecha == fecha)

    def __len__(self) -> int:
        return len(self._citas)
