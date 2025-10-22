"""Excepcion especifica para falta de superficie (US-004)."""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    TECH_SUPERFICIE_INSUFICIENTE,
    USER_SUPERFICIE_INSUFICIENTE,
)


class SuperficieInsuficienteException(ForestacionException):
    """Lanzada cuando se intenta plantar sin superficie suficiente."""

    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        technical_message: str = TECH_SUPERFICIE_INSUFICIENTE,
        user_message: str = USER_SUPERFICIE_INSUFICIENTE,
    ):
        """
        Inicializa la excepcion.

        Args:
            superficie_requerida: Superficie necesaria para la operacion.
            superficie_disponible: Superficie disponible en la plantacion.
            technical_message: Mensaje tecnico.
            user_message: Mensaje de usuario.
        """
        super().__init__(user_message, technical_message)
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible