"""Define el Enum para los tipos de eventos de sensor."""

# Standard library
from enum import Enum, auto


class TipoEventoSensor(Enum):
    """Tipos de eventos de sensor para el patron Observer."""
    TEMPERATURA = auto()
    HUMEDAD = auto()