"""Servicio para la entidad Tierra."""

# Standard library
from typing import TYPE_CHECKING

# Local application
# Entidades
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra

if TYPE_CHECKING:
    pass


class TierraService:
    """Servicio con logica de negocio para Tierra."""

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una Tierra y una Plantacion asociada (US-001, US-002).

        Args:
            id_padron_catastral: ID de la tierra.
            superficie: Superficie en m².
            domicilio: Ubicacion.
            nombre_plantacion: Nombre de la finca a crear.

        Returns:
            La entidad Tierra creada y vinculada.
        """
        # 1. Crear Tierra
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # 2. Crear Plantacion
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_maxima=tierra.get_superficie()
        )

        # 3. Vincularlas
        tierra.set_finca(plantacion)

        return tierra