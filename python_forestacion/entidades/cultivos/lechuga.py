"""Entidad Lechuga (US-006)."""

# Local application
from python_forestacion import constantes
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Lechuga(Hortaliza):
    """Entidad Lechuga."""

    def __init__(self, variedad: str):
        """
        Inicializa la Lechuga usando constantes.

        Args:
            variedad: Variedad de la lechuga (ej. Crespa).
        """
        super().__init__(
            agua=constantes.AGUA_INICIAL_LECHUGA,
            superficie=constantes.SUPERFICIE_LECHUGA,
            invernadero=True  # US-006: siempre en invernadero
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad