"""Servicio especifico para Olivo."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio con logica de negocio para Olivos."""

    def __init__(self):
        """Inyecta la estrategia Seasonal (US-TECH-004)."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Olivo') -> int:
        """Sobrescribe para agregar crecimiento (US-008)."""
        agua_absorvida = super().absorver_agua(cultivo)
        if agua_absorvida > 0:
            self.crecer(cultivo, constantes.CRECIMIENTO_OLIVO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos especificos de Olivo (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")