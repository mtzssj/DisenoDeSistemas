"""Entidad Tarea (US-014)."""

# Standard library
from datetime import date

# Local application
from python_forestacion.entidades.personal.estado_tarea import EstadoTarea


class Tarea:
    """Entidad Tarea asignada a un trabajador."""

    def __init__(
        self,
        id_tarea: int,
        fecha_programada: date,
        descripcion: str
    ):
        """
        Inicializa la Tarea.

        Args:
            id_tarea: ID unico de la tarea.
            fecha_programada: Fecha de ejecucion.
            descripcion: Descripcion.
        """
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._estado: EstadoTarea = EstadoTarea.PENDIENTE

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> EstadoTarea:
        return self._estado

    def completar_tarea(self) -> None:
        """Marca la tarea como completada."""
        self._estado = EstadoTarea.COMPLETADA