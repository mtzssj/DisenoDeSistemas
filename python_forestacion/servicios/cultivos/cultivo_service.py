"""Servicio base para todos los cultivos."""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para la logica de negocio de Cultivos.
    Implementa la inyeccion del patron Strategy (US-TECH-004).
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio inyectando la estrategia de absorcion.

        Args:
            estrategia_absorcion: Instancia de la estrategia a usar.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Delega el calculo de absorcion a la estrategia inyectada.

        Args:
            cultivo: El cultivo que absorbe.

        Returns:
            Cantidad de agua absorbida.
        """
        # Fecha actual (simplificado, podria inyectarse)
        fecha = date.today()

        # Delegacion al patron Strategy (US-TECH-004)
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha,
            cultivo
        )

        # Actualizar estado de la entidad
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Metodo abstracto para mostrar datos especificos.
        Implementa la base para el dispatch del Registry (US-009).
        """
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")