"""Implementacion de Paquete generico (US-020)."""

# Standard library
import uuid
from typing import Generic, List, TypeVar

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# Define el tipo generico T, restringido a subtipos de Cultivo
T = TypeVar('T', bound=Cultivo)


class Paquete(Generic[T]):
    """
    Clase generica para empaquetar cultivos cosechados (US-020).
    Garantiza tipo-seguridad (Rubrica 1.3, 3.3).
    """

    def __init__(self, tipo_contenido: type[T]):
        """
        Inicializa el paquete.

        Args:
            tipo_contenido: El tipo (clase) de cultivo que contendra.
        """
        self._id_paquete: uuid.UUID = uuid.uuid4()
        self._items: List[T] = []
        self._tipo_contenido: type[T] = tipo_contenido

    def agregar_item(self, item: T) -> None:
        """Agrega un cultivo al paquete."""
        if not isinstance(item, self._tipo_contenido):
            raise TypeError(f"Este paquete solo acepta "
                            f"{self._tipo_contenido.__name__}")
        self._items.append(item)

    def get_cantidad(self) -> int:
        return len(self._items)

    def get_tipo_contenido_nombre(self) -> str:
        return self._tipo_contenido.__name__

    def get_items(self) -> List[T]:
        return self._items.copy()

    def mostrar_contenido_caja(self) -> None:
        """Muestra el resumen del paquete (US-020)."""
        print("\nContenido de la caja:")
        print(f"  Tipo: {self.get_tipo_contenido_nombre()}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {str(self._id_paquete)[:8]}")