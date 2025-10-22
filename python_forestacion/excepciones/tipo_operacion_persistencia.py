"""Define el Enum para el tipo de operacion de persistencia."""

# Standard library
from enum import Enum, auto


class TipoOperacionPersistencia(Enum):
    """Tipos de operaciones de persistencia para logging de excepciones."""
    LECTURA = auto()
    ESCRITURA = auto()