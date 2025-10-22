"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

"""Entidad Plantacion (US-002)."""

# Standard library
from typing import TYPE_CHECKING, List

# Local application
from python_forestacion import constantes
from python_forestacion.excepciones.mensajes_exception import TECH_AGUA_NEGATIVA

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """Entidad Plantacion, gestiona cultivos y recursos."""

    def __init__(self, nombre: str, superficie_maxima: float):
        """
        Inicializa la Plantacion.

        Args:
            nombre: Nombre identificatorio.
            superficie_maxima: Superficie maxima (heredada de Tierra).
        """
        self._nombre = nombre
        self._superficie_maxima = superficie_maxima
        self._superficie_ocupada = 0.0
        self._agua_disponible = constantes.AGUA_INICIAL_PLANTACION  # 500L
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_maxima(self) -> float:
        return self._superficie_maxima

    def get_superficie_ocupada(self) -> float:
        return self._superficie_ocupada

    def set_superficie_ocupada(self, superficie: float) -> None:
        self._superficie_ocupada = superficie

    def get_superficie_disponible(self) -> float:
        """Calcula la superficie restante."""
        return self._superficie_maxima - self._superficie_ocupada

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def set_agua_disponible(self, agua: float) -> None:
        """
        Establece el agua disponible, validando que no sea negativa (US-002).

        Args:
            agua: Nueva cantidad de agua.

        Raises:
            ValueError: Si el agua es < 0.
        """
        if agua < 0:
            raise ValueError(TECH_AGUA_NEGATIVA)
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """
        Retorna una copia de la lista de cultivos (Defensive Copy).
        Cumple con Rubrica 5.2.
        """
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo y actualiza la superficie ocupada."""
        self._cultivos.append(cultivo)
        self._superficie_ocupada += cultivo.get_superficie()

    def remover_cultivo(self, cultivo: 'Cultivo') -> None:
        """Remueve un cultivo (usado en cosecha) y libera superficie."""
        try:
            self._cultivos.remove(cultivo)
            self._superficie_ocupada -= cultivo.get_superficie()
        except ValueError:
            pass  # Ignorar si no esta

    def get_trabajadores(self) -> List['Trabajador']:
        """
        Retorna una copia de la lista de trabajadores (Defensive Copy).
        Cumple con Rubrica 5.2 y US-017.
        """
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """Reemplaza la lista de trabajadores (US-017)."""
        self._trabajadores = trabajadores.copy()

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

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

