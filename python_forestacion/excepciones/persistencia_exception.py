"""Excepcion especifica para errores de persistencia (US-021, US-022)."""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    TECH_ERROR_PERSISTENCIA,
    USER_ERROR_PERSISTENCIA,
)
from python_forestacion.excepciones.tipo_operacion_persistencia import (
    TipoOperacionPersistencia,
)


class PersistenciaException(ForestacionException):
    """Lanzada cuando ocurre un error de I/O con Pickle."""

    def __init__(
        self,
        nombre_archivo: str,
        tipo_operacion: TipoOperacionPersistencia,
        technical_message: str = TECH_ERROR_PERSISTENCIA,
        user_message: str = USER_ERROR_PERSISTENCIA,
        causa_original: Optional[Exception] = None,
    ):
        """
        Inicializa la excepcion.

        Args:
            nombre_archivo: Archivo que causo el error.
            tipo_operacion: Si fue LECTURA o ESCRITURA.
            technical_message: Mensaje tecnico.
            user_message: Mensaje de usuario.
            causa_original: Excepcion original (p.ej. IOError).
        """
        super().__init__(user_message, technical_message)
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
        self._causa_original = causa_original

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacionPersistencia:
        return self._tipo_operacion

    def get_causa_original(self) -> Optional[Exception]:
        return self._causa_original