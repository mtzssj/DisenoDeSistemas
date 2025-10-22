"""
Implementacion de la interfaz Strategy (US-TECH-004).
Define el contrato para las estrategias de absorcion de agua.
"""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """Interfaz abstracta Strategy (Estrategia)."""

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua absorbida por un cultivo.

        Args:
            fecha: Fecha actual (para estrategias estacionales).
            cultivo: El cultivo que absorbe el agua.

        Returns:
            Cantidad de agua (en litros) absorbida.
        """
        pass