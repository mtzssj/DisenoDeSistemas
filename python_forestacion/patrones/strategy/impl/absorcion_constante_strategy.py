"""Implementacion Concreta 1: Absorcion Constante (US-TECH-004)."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia para hortalizas: absorbe siempre la misma cantidad."""

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia.

        Args:
            cantidad_constante: Cantidad fija de agua a absorber.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna la cantidad constante.

        Args:
            fecha: No utilizada en esta estrategia.
            cultivo: No utilizado en esta estrategia.

        Returns:
            Cantidad de agua (en litros) configurada.
        """
        return self._cantidad