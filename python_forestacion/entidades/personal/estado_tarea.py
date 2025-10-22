"""Define el Enum para el estado de una Tarea (US-014)."""

# Standard library
from enum import Enum, auto


class EstadoTarea(Enum):
    """Estado de ejecucion de una tarea."""
    PENDIENTE = auto()
    COMPLETADA = auto()