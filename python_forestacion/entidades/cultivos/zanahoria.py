"""Entidad Zanahoria (US-007)."""

# Local application
from python_forestacion import constantes
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Zanahoria(Hortaliza):
    """Entidad Zanahoria."""

    def __init__(self, is_baby_carrot: bool):
        """
        Inicializa la Zanahoria usando constantes.

        Args:
            is_baby_carrot: True si es baby carrot, False si es regular.
        """
        super().__init__(
            agua=constantes.AGUA_INICIAL_ZANAHORIA,
            superficie=constantes.SUPERFICIE_ZANAHORIA,
            invernadero=False  # US-007: cultivo a campo abierto
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._is_baby_carrot