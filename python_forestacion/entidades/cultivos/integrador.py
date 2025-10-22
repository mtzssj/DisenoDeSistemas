"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

"""Entidad Lechuga (US-006)."""

# Local application
from python_forestacion import constantes
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Lechuga(Hortaliza):
    """Entidad Lechuga."""

    def __init__(self, variedad: str):
        """
        Inicializa la Lechuga usando constantes.

        Args:
            variedad: Variedad de la lechuga (ej. Crespa).
        """
        super().__init__(
            agua=constantes.AGUA_INICIAL_LECHUGA,
            superficie=constantes.SUPERFICIE_LECHUGA,
            invernadero=True  # US-006: siempre en invernadero
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

"""Define el Enum para los tipos de aceituna (US-005)."""

# Standard library
from enum import Enum, auto


class TipoAceituna(Enum):
    """Tipos de aceituna disponibles para Olivos."""
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

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

