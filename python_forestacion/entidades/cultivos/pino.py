"""Entidad Pino (US-004)."""

# Local application
from python_forestacion import constantes
from python_forestacion.entidades.cultivos.arbol import Arbol


class Pino(Arbol):
    """Entidad Pino."""

    def __init__(self, variedad: str):
        """
        Inicializa el Pino usando constantes.

        Args:
            variedad: Variedad del pino (ej. Parana).
        """
        super().__init__(
            agua=constantes.AGUA_INICIAL_PINO,
            superficie=constantes.SUPERFICIE_PINO,
            altura=constantes.ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad