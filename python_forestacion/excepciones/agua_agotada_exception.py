"""Excepcion especifica para falta de agua (US-008)."""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    TECH_AGUA_AGOTADA,
    USER_AGUA_AGOTADA,
)


class AguaAgotadaException(ForestacionException):
    """Lanzada cuando se intenta regar sin agua suficiente."""

    def __init__(
        self,
        agua_requerida: float,
        agua_disponible: float,
        technical_message: str = TECH_AGUA_AGOTADA,
        user_message: str = USER_AGUA_AGOTADA,
    ):
        """
        Inicializa la excepcion.

        Args:
            agua_requerida: Agua necesaria para la operacion.
            agua_disponible: Agua disponible en la plantacion.
            technical_message: Mensaje tecnico.
            user_message: Mensaje de usuario.
        """
        super().__init__(user_message, technical_message)
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

    def get_agua_requerida(self) -> float:
        return self._agua_requerida

    def get_agua_disponible(self) -> float:
        return self._agua_disponible