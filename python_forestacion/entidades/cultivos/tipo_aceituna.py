"""Define el Enum para los tipos de aceituna (US-005)."""

# Standard library
from enum import Enum, auto


class TipoAceituna(Enum):
    """Tipos de aceituna disponibles para Olivos."""
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()