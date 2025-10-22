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