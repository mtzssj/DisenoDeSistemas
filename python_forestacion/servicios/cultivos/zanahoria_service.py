"""Servicio especifico para Zanahoria."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio con logica de negocio para Zanahorias."""

    def __init__(self):
        """Inyecta la estrategia Constante (US-TECH-004)."""
        super().__init__(
            AbsorcionConstanteStrategy(constantes.ABSORCION_CONSTANTE_ZANAHORIA)
        )

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos especificos de Zanahoria (US-009)."""
        super().mostrar_datos(cultivo)
        tipo = "Baby Carrot" if cultivo.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")