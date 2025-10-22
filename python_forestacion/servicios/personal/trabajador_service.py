"""Servicio para la entidad Trabajador."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.estado_tarea import EstadoTarea
from python_forestacion.entidades.personal.tarea import Tarea

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.trabajador import Trabajador


class TrabajadorService:
    """Servicio con logica de negocio para Trabajador."""

    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        """
        Crea y asigna un AptoMedico a un trabajador (US-015).

        Args:
            trabajador: El trabajador a certificar.
            apto: Si esta apto o no.
            fecha_emision: Fecha del certificado.
            observaciones: Comentarios medicos.
        """
        apto_medico = AptoMedico(
            esta_apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )
        trabajador.set_apto_medico(apto_medico)

    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """
        Metodo helper estatico para el ordenamiento (US-016).
        Evita el uso de lambdas (Rubrica 3.4).
        """
        return tarea.get_id_tarea()

    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas al trabajador (US-016).

        Args:
            trabajador: El trabajador que ejecuta.
            fecha: Fecha actual.
            util: Herramienta a utilizar.

        Returns:
            True si pudo trabajar, False si no tenia apto medico.
        """
        apto_medico = trabajador.get_apto_medico()

        # 1. Validar apto medico (US-016)
        if apto_medico is None or not apto_medico.esta_apto():
            print(f"\n[PERSONAL] El trabajador {trabajador.get_nombre()} "
                  "NO puede trabajar. Apto medico invalido.")
            return False

        print(f"\n[PERSONAL] El trabajador {trabajador.get_nombre()} "
              "comienza a trabajar con {util.get_nombre()}...")

        # 2. Obtener tareas (copia)
        tareas = trabajador.get_tareas()

        # 3. Ordenar tareas por ID descendente (US-016)
        # Se usa el metodo helper estatico en lugar de lambda
        tareas_ordenadas = sorted(
            tareas,
            key=self._obtener_id_tarea,
            reverse=True
        )

        # 4. Ejecutar tareas
        tareas_ejecutadas_hoy = 0
        for tarea in tareas_ordenadas:
            if (tarea.get_fecha_programada() == fecha and
                    tarea.get_estado() == EstadoTarea.PENDIENTE):

                print(f"  -> Realizando tarea {tarea.get_id_tarea()}: "
                      f"{tarea.get_descripcion()}")
                tarea.completar_tarea()  # Modifica la tarea original
                tareas_ejecutadas_hoy += 1

        if tareas_ejecutadas_hoy == 0:
            print(f"  -> No hay tareas pendientes para hoy ({fecha}).")
        else:
            print(f"[PERSONAL] Tareas de {trabajador.get_nombre()} "
                  "completadas exitosamente.")

        return True