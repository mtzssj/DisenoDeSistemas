"""
Define el objeto de evento para el patron Observer.

Esto es necesario para cumplir con la US-012 (observar ambos sensores)
y la US-TECH-003 (usar Generics) de forma robusta.
En lugar de Observable[float], usaremos Observable[EventoSensor].
"""

# Standard library
from dataclasses import dataclass

# Local application
from python_forestacion.patrones.observer.tipo_evento_sensor import TipoEventoSensor


@dataclass(frozen=True)
class EventoSensor:
    """Objeto de datos inmutable que representa un evento de sensor."""
    tipo: TipoEventoSensor
    valor: float