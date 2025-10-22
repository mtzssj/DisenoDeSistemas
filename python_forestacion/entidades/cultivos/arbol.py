"""Define la clase base para cultivos tipo Arbol."""

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """Clase base para Arboles (Pino, Olivo)."""

    def __init__(self, agua: float, superficie: float, altura: float):
        """
        Inicializa la entidad Arbol.

        Args:
            agua: Agua inicial.
            superficie: Superficie requerida.
            altura: Altura inicial.
        """
        super().__init__(agua, superficie)
        self._altura: float = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            self._altura = 0
        else:
            self._altura = altura