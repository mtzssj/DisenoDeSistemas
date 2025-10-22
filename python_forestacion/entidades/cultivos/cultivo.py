"""Define la clase base abstracta para todos los Cultivos."""

# Standard library
import uuid
from abc import ABC


class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos (Pino, Olivo, etc.).
    Actua como DTO (Data Transfer Object) solo con datos y validaciones.
    """

    def __init__(self, agua: float, superficie: float):
        """
        Inicializa la entidad base del cultivo.

        Args:
            agua: Agua inicial almacenada por el cultivo.
            superficie: Superficie requerida por el cultivo.
        """
        self._id: uuid.UUID = uuid.uuid4()
        self._agua: float = agua
        self._superficie: float = superficie

    def get_id(self) -> uuid.UUID:
        return self._id

    def get_agua(self) -> float:
        return self._agua

    def set_agua(self, agua: float) -> None:
        if agua < 0:
            # Validacion simple, las excepciones de dominio
            # se lanzan en los servicios.
            self._agua = 0
        else:
            self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def __str__(self) -> str:
        return f"Cultivo tipo {type(self).__name__} (ID: {self._id})"

    def __repr__(self) -> str:
        return self.__str__()