"""Servicio especifico para Pino."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio con logica de negocio para Pinos."""

    def __init__(self):
        """Inyecta la estrategia Seasonal (US-TECH-004)."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Pino') -> int:
        """Sobrescribe para agregar crecimiento (US-008)."""
        agua_absorvida = super().absorver_agua(cultivo)
        if agua_absorvida > 0:
            self.crecer(cultivo, constantes.CRECIMIENTO_PINO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos especificos de Pino (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")