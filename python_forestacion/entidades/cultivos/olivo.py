"""Entidad Olivo (US-005)."""

# Local application
from python_forestacion import constantes
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class Olivo(Arbol):
    """Entidad Olivo."""

    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa el Olivo usando constantes.

        Args:
            tipo_aceituna: Enum del tipo de aceituna.
        """
        super().__init__(
            agua=constantes.AGUA_INICIAL_OLIVO,
            superficie=constantes.SUPERFICIE_OLIVO,
            altura=constantes.ALTURA_INICIAL_OLIVO
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna