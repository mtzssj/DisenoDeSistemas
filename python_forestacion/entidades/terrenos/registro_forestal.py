"""Entidad RegistroForestal (US-003)."""

# Standard library
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """Entidad que vincula Tierra, Plantacion y Propietario."""

    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa el Registro Forestal.

        Args:
            id_padron: ID de padron (de la Tierra).
            tierra: Objeto Tierra.
            plantacion: Objeto Plantacion.
            propietario: Nombre del propietario.
            avaluo: Avaluo fiscal.
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo