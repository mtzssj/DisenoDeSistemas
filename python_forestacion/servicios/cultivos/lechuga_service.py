"""Servicio especifico para Lechuga."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio con logica de negocio para Lechugas."""

    def __init__(self):
        """Inyecta la estrategia Constante (US-TECH-004)."""
        super().__init__(
            AbsorcionConstanteStrategy(constantes.ABSORCION_CONSTANTE_LECHUGA)
        )

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos especificos de Lechuga (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.requiere_invernadero()}")