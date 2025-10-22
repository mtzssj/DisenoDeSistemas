"""Implementacion Concreta 2: Absorcion Estacional (US-TECH-004)."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia para arboles: absorbe segun la estacion (verano/invierno)."""

    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la absorcion basada en el mes actual.

        Args:
            fecha: Fecha actual para determinar el mes.
            cultivo: No utilizado en esta estrategia.

        Returns:
            Cantidad de agua (en litros) segun la estacion.
        """
        mes = fecha.month
        if constantes.MES_INICIO_VERANO <= mes <= constantes.MES_FIN_VERANO:
            return constantes.ABSORCION_SEASONAL_VERANO
        else:
            return constantes.ABSORCION_SEASONAL_INVIERNO