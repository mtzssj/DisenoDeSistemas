"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ================================================================================

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

