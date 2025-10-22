"""Define la clase base para cultivos tipo Hortaliza."""

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """Clase base para Hortalizas (Lechuga, Zanahoria)."""

    def __init__(self, agua: float, superficie: float, invernadero: bool):
        """
        Inicializa la entidad Hortaliza.

        Args:
            agua: Agua inicial.
            superficie: Superficie requerida.
            invernadero: Si requiere invernadero.
        """
        super().__init__(agua, superficie)
        self._invernadero: bool = invernadero

    def requiere_invernadero(self) -> bool:
        return self._invernadero