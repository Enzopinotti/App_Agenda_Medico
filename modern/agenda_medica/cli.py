from __future__ import annotations

from datetime import date, time

from .models import Agenda, Cita, Paciente


def _fecha(prompt: str) -> date:
    while True:
        raw = input(f"{prompt} (AAAA-MM-DD): ").strip()
        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("Fecha inválida. Use una fecha real en formato AAAA-MM-DD.")


def _horario(prompt: str) -> time:
    while True:
        raw = input(f"{prompt} (HH:MM): ").strip()
        try:
            return time.fromisoformat(raw)
        except ValueError:
            print("Horario inválido. Use HH:MM en formato de 24 horas.")


def _paciente() -> Paciente:
    while True:
        try:
            return Paciente(
                nombre=input("Nombre: "),
                apellido=input("Apellido: "),
                obra_social=input("Obra social: "),
            )
        except ValueError as exc:
            print(f"Datos inválidos: {exc}")


def _listar(agenda: Agenda) -> None:
    citas = agenda.listar()
    if not citas:
        print("La agenda no posee citas.")
        return
    for cita in citas:
        print(
            f"{cita.fecha.isoformat()} {cita.horario.strftime('%H:%M')} — "
            f"{cita.paciente.nombre} {cita.paciente.apellido} — "
            f"{cita.paciente.obra_social}"
        )


def _menu() -> None:
    print(
        "\nAgenda Médica — autoridad 2026\n"
        "a) Agregar cita\n"
        "b) Reprogramar citas de un paciente\n"
        "c) Eliminar citas de un paciente\n"
        "d) Listar citas\n"
        "e) Trasladar todas las citas de una fecha\n"
        "f) Eliminar citas por obra social\n"
        "g) Generar cola de un día\n"
        "q) Salir"
    )


def ejecutar() -> None:
    agenda = Agenda()

    while True:
        _menu()
        opcion = input("Opción: ").strip().lower()

        if opcion == "q":
            return
        if opcion == "a":
            paciente = _paciente()
            agenda.agregar(Cita(paciente, _fecha("Fecha"), _horario("Horario")))
            print("Cita agregada.")
        elif opcion == "b":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            cantidad = agenda.reprogramar_paciente(
                nombre,
                apellido,
                _fecha("Nueva fecha"),
                _horario("Nuevo horario"),
            )
            print(f"Citas reprogramadas: {cantidad}")
        elif opcion == "c":
            cantidad = agenda.eliminar_paciente(
                input("Nombre: "), input("Apellido: ")
            )
            print(f"Citas eliminadas: {cantidad}")
        elif opcion == "d":
            _listar(agenda)
        elif opcion == "e":
            cantidad = agenda.trasladar_fecha(
                _fecha("Fecha origen"), _fecha("Fecha destino")
            )
            print(f"Citas trasladadas: {cantidad}")
        elif opcion == "f":
            try:
                cantidad = agenda.eliminar_por_obra_social(input("Obra social: "))
            except ValueError as exc:
                print(f"Dato inválido: {exc}")
            else:
                print(f"Citas eliminadas: {cantidad}")
        elif opcion == "g":
            cola = agenda.cola_del_dia(_fecha("Fecha"))
            if cola.es_vacia():
                print("No hay citas para esa fecha.")
                continue
            print("Cola FIFO:")
            while not cola.es_vacia():
                cita = cola.desencolar()
                print(
                    f"- {cita.horario.strftime('%H:%M')} "
                    f"{cita.paciente.nombre} {cita.paciente.apellido} "
                    f"({cita.paciente.obra_social})"
                )
        else:
            print("Opción inválida.")
