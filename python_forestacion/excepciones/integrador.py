"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: agua_agotada_exception.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

"""Excepcion especifica para falta de agua (US-008)."""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    TECH_AGUA_AGOTADA,
    USER_AGUA_AGOTADA,
)


class AguaAgotadaException(ForestacionException):
    """Lanzada cuando se intenta regar sin agua suficiente."""

    def __init__(
        self,
        agua_requerida: float,
        agua_disponible: float,
        technical_message: str = TECH_AGUA_AGOTADA,
        user_message: str = USER_AGUA_AGOTADA,
    ):
        """
        Inicializa la excepcion.

        Args:
            agua_requerida: Agua necesaria para la operacion.
            agua_disponible: Agua disponible en la plantacion.
            technical_message: Mensaje tecnico.
            user_message: Mensaje de usuario.
        """
        super().__init__(user_message, technical_message)
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

    def get_agua_requerida(self) -> float:
        return self._agua_requerida

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

# ================================================================================
# ARCHIVO 3/7: forestacion_exception.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

"""
Modulo de Excepcion Base.

Define la excepcion base personalizada para el sistema (Rubrica 2.3).
"""

class ForestacionException(Exception):
    """Excepcion base para todos los errores de dominio del sistema."""

    def __init__(self, user_message: str, technical_message: str):
        """
        Inicializa la excepcion base.

        Args:
            user_message: Mensaje claro para el usuario final.
            technical_message: Mensaje tecnico para desarrolladores/logs.
        """
        super().__init__(technical_message)
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        """
        Obtiene el mensaje orientado al usuario.

        Returns:
            Mensaje de error para el usuario.
        """
        return self._user_message

    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje orientado al tecnico.

        Returns:
            Mensaje de error tecnico.
        """
        return self._technical_message

    def get_full_message(self) -> str:
        """
        Obtiene un mensaje combinado para logs.

        Returns:
            Mensaje combinado (Usuario + Tecnico).
        """
        return f"[USUARIO] {self._user_message} [TECNICO] {self._technical_message}"

# ================================================================================
# ARCHIVO 4/7: mensajes_exception.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

"""
Modulo de Mensajes de Excepcion.

Centraliza los mensajes de error para el usuario y tecnico,
cumpliendo con la Rubrica 2.3.
"""

# --- Superficie ---
USER_SUPERFICIE_INSUFICIENTE = "Superficie insuficiente en la plantacion."
TECH_SUPERFICIE_INSUFICIENTE = "Se intento plantar mas alla de la capacidad."

# --- Agua ---
USER_AGUA_AGOTADA = "Agua agotada en la plantacion."
TECH_AGUA_AGOTADA = "Se intento regar sin suficiente agua disponible."

# --- Persistencia ---
USER_ERROR_PERSISTENCIA = "Ocurrio un error al guardar o leer el archivo."
TECH_ERROR_PERSISTENCIA = "Error de I/O (Pickle) al operar en archivo."
USER_ARCHIVO_NO_ENCONTRADO = "El archivo de registro no fue encontrado."
TECH_ARCHIVO_NO_ENCONTRADO = "FileNotFoundError durante la lectura."
USER_ARCHIVO_CORRUPTO = "El archivo de registro esta corrupto."
TECH_ARCHIVO_CORRUPTO = "EOFError o UnpicklingError durante la lectura."

# --- Validacion ---
USER_VALOR_INVALIDO = "El valor proporcionado es invalido."
TECH_SUPERFICIE_NEGATIVA = "La superficie debe ser mayor a cero."
TECH_AGUA_NEGATIVA = "El agua disponible no puede ser negativa."
TECH_PROPIETARIO_NULO = "El nombre del propietario no puede ser nulo o vacio."

# ================================================================================
# ARCHIVO 5/7: persistencia_exception.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/7: superficie_insuficiente_exception.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

"""Excepcion especifica para falta de superficie (US-004)."""

# Standard library
from typing import Optional

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    TECH_SUPERFICIE_INSUFICIENTE,
    USER_SUPERFICIE_INSUFICIENTE,
)


class SuperficieInsuficienteException(ForestacionException):
    """Lanzada cuando se intenta plantar sin superficie suficiente."""

    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        technical_message: str = TECH_SUPERFICIE_INSUFICIENTE,
        user_message: str = USER_SUPERFICIE_INSUFICIENTE,
    ):
        """
        Inicializa la excepcion.

        Args:
            superficie_requerida: Superficie necesaria para la operacion.
            superficie_disponible: Superficie disponible en la plantacion.
            technical_message: Mensaje tecnico.
            user_message: Mensaje de usuario.
        """
        super().__init__(user_message, technical_message)
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

# ================================================================================
# ARCHIVO 7/7: tipo_operacion_persistencia.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\tipo_operacion_persistencia.py
# ================================================================================

"""Define el Enum para el tipo de operacion de persistencia."""

# Standard library
from enum import Enum, auto


class TipoOperacionPersistencia(Enum):
    """Tipos de operaciones de persistencia para logging de excepciones."""
    LECTURA = auto()
    ESCRITURA = auto()

