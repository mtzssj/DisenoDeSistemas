"""
Implementacion de la interfaz Observer (US-TECH-003).
Usa Generics (TypeVar) para tipo-seguridad.
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Local application
# (Usamos EventoSensor como T, en lugar de float, para distinguir fuentes)
from python_forestacion.patrones.observer.evento_sensor import EventoSensor

# Define el tipo generico T
T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz abstracta Observer (Observador)."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado por el Observable cuando hay un cambio.

        Args:
            evento: El objeto de evento (T) con los datos del cambio.
        """
        pass