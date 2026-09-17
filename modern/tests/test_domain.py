from __future__ import annotations

import unittest
from datetime import date, time

from agenda_medica import Agenda, Cita, ColaCitas, Paciente


class PacienteTests(unittest.TestCase):
    def test_normaliza_espacios_y_exige_campos(self) -> None:
        paciente = Paciente("  Ana  María ", "  Pérez ", "  OSDE  210 ")
        self.assertEqual(paciente.nombre, "Ana María")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.obra_social, "OSDE 210")

        with self.assertRaises(ValueError):
            Paciente("", "Pérez", "OSDE")


class ColaCitasTests(unittest.TestCase):
    def test_desencolar_es_fifo_y_no_lifo(self) -> None:
        fecha = date(2026, 9, 17)
        primera = Cita(Paciente("Ana", "Pérez", "OSDE"), fecha, time(9, 0))
        segunda = Cita(Paciente("Juan", "Gómez", "IOMA"), fecha, time(10, 0))
        cola = ColaCitas(iter((primera, segunda)))

        self.assertIs(cola.desencolar(), primera)
        self.assertIs(cola.desencolar(), segunda)
        self.assertTrue(cola.es_vacia())

    def test_desencolar_vacia_es_error_explicito(self) -> None:
        with self.assertRaisesRegex(IndexError, "vacía"):
            ColaCitas().desencolar()


class AgendaTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fecha = date(2026, 9, 17)
        self.otra_fecha = date(2026, 9, 18)
        self.ana = Paciente("Ana", "Pérez", "OSDE")
        self.juan = Paciente("Juan", "Gómez", "IOMA")
        self.agenda = Agenda(
            iter(
                (
                    Cita(self.ana, self.fecha, time(9, 0)),
                    Cita(self.juan, self.fecha, time(10, 30)),
                    Cita(self.ana, self.otra_fecha, time(15, 0)),
                )
            )
        )

    def test_listar_devuelve_snapshot_inmutable(self) -> None:
        snapshot = self.agenda.listar()
        self.assertIsInstance(snapshot, tuple)
        self.agenda.agregar(Cita(self.juan, self.otra_fecha, time(17, 0)))
        self.assertEqual(len(snapshot), 3)
        self.assertEqual(len(self.agenda), 4)

    def test_buscar_por_paciente_es_case_insensitive(self) -> None:
        citas = self.agenda.buscar_por_paciente("ANA", "péREZ")
        self.assertEqual(len(citas), 2)
        self.assertTrue(all(cita.paciente == self.ana for cita in citas))

    def test_reprogramar_paciente_actualiza_todas_sus_citas(self) -> None:
        nueva_fecha = date(2026, 10, 1)
        nuevo_horario = time(8, 15)
        cantidad = self.agenda.reprogramar_paciente(
            "ana", "PÉREZ", nueva_fecha, nuevo_horario
        )

        self.assertEqual(cantidad, 2)
        citas = self.agenda.buscar_por_paciente("Ana", "Pérez")
        self.assertTrue(all(cita.fecha == nueva_fecha for cita in citas))
        self.assertTrue(all(cita.horario == nuevo_horario for cita in citas))

    def test_eliminar_paciente_elimina_todas_sus_citas(self) -> None:
        cantidad = self.agenda.eliminar_paciente("Ana", "Pérez")
        self.assertEqual(cantidad, 2)
        self.assertEqual(len(self.agenda), 1)
        self.assertEqual(self.agenda.listar()[0].paciente, self.juan)

    def test_eliminar_por_obra_social_es_case_insensitive(self) -> None:
        cantidad = self.agenda.eliminar_por_obra_social("osde")
        self.assertEqual(cantidad, 2)
        self.assertEqual(len(self.agenda), 1)

    def test_trasladar_fecha_preserva_horario(self) -> None:
        destino = date(2026, 9, 30)
        antes = {
            (cita.paciente.identidad, cita.horario)
            for cita in self.agenda.listar()
            if cita.fecha == self.fecha
        }

        cantidad = self.agenda.trasladar_fecha(self.fecha, destino)
        despues = {
            (cita.paciente.identidad, cita.horario)
            for cita in self.agenda.listar()
            if cita.fecha == destino
        }

        self.assertEqual(cantidad, 2)
        self.assertEqual(antes, despues)

    def test_cola_del_dia_filtra_y_preserva_orden_de_alta(self) -> None:
        cola = self.agenda.cola_del_dia(self.fecha)
        self.assertEqual(len(cola), 2)
        self.assertEqual(cola.desencolar().paciente, self.ana)
        self.assertEqual(cola.desencolar().paciente, self.juan)

    def test_operaciones_sin_coincidencia_retornan_cero(self) -> None:
        self.assertEqual(
            self.agenda.reprogramar_paciente(
                "Nadie", "Existe", self.otra_fecha, time(12, 0)
            ),
            0,
        )
        self.assertEqual(self.agenda.eliminar_paciente("Nadie", "Existe"), 0)
        self.assertEqual(self.agenda.eliminar_por_obra_social("Otra"), 0)
        self.assertEqual(
            self.agenda.trasladar_fecha(date(2025, 1, 1), date(2025, 1, 2)), 0
        )


if __name__ == "__main__":
    unittest.main()
