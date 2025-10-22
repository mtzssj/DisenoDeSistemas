"""Servicio base para Arboles (Pino, Olivo)."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio base para logica especifica de Arboles."""

    def crecer(self, arbol: 'Arbol', cantidad_crecimiento: float) -> None:
        """
        Aumenta la altura del arbol (US-008).

        Args:
            arbol: La entidad Arbol a modificar.
            cantidad_crecimiento: Metros a agregar.
        """
        nueva_altura = arbol.get_altura() + cantidad_crecimiento
        arbol.set_altura(nueva_altura)

    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        """Muestra datos comunes de Arbol."""
        super().mostrar_datos(cultivo)  # Llama al padre
        print(f"ID: {str(cultivo.get_id())[:8]}")  # Mostramos ID corto
        print(f"Altura: {cultivo.get_altura():.2f} m")