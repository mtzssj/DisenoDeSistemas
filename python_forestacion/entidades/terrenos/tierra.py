"""Entidad Tierra (US-001)."""

# Standard library
from typing import TYPE_CHECKING, Optional

# Local application
from python_forestacion.excepciones.mensajes_exception import (
    TECH_SUPERFICIE_NEGATIVA,
)

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """Entidad Tierra, representa el terreno catastral."""

    def __init__(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str
    ):
        """
        Inicializa la Tierra.

        Args:
            id_padron_catastral: Numero unico.
            superficie: Superficie en m².
            domicilio: Ubicacion.
        """
        self._id_padron_catastral = id_padron_catastral
        self._superficie = 0.0  # Inicializa en 0
        self.set_superficie(superficie)  # Usa el setter para validar
        self._domicilio = domicilio
        self._finca: Optional['Plantacion'] = None

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie, validando que sea positiva (US-001).

        Args:
            superficie: Nueva superficie.

        Raises:
            ValueError: Si la superficie es <= 0.
        """
        if superficie <= 0:
            raise ValueError(TECH_SUPERFICIE_NEGATIVA)
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional['Plantacion']:
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """Asocia una plantacion (finca) a este terreno."""
        self._finca = finca