"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion
Fecha de generacion: 2025-10-22 01:20:00
Total de archivos integrados: 66
Total de directorios procesados: 19
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   13. __init__.py
#   14. apto_medico.py
#   15. estado_tarea.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades\terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#   29. tipo_operacion_persistencia.py
#
# DIRECTORIO: patrones
#   30. __init__.py
#
# DIRECTORIO: patrones\factory
#   31. __init__.py
#   32. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   33. __init__.py
#   34. evento_sensor.py
#   35. observable.py
#   36. observer.py
#   37. tipo_evento_sensor.py
#
# DIRECTORIO: patrones\strategy
#   38. __init__.py
#   39. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   40. __init__.py
#   41. absorcion_constante_strategy.py
#   42. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   43. __init__.py
#
# DIRECTORIO: riego\control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: riego\sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   49. __init__.py
#
# DIRECTORIO: servicios\cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: servicios\negocio
#   58. __init__.py
#   59. fincas_service.py
#   60. paquete.py
#
# DIRECTORIO: servicios\personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: servicios\terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\__init__.py
# ==============================================================================

# Archivo __init__.py para el paquete principal python_forestacion
# Permite que Python trate este directorio como un paquete.

# ==============================================================================
# ARCHIVO 2/66: constantes.py
# Directorio: .
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\constantes.py
# ==============================================================================

"""
Modulo de Constantes.

Centraliza todos los valores magicos y configuraciones del sistema
para cumplir con los principios de Codigo Limpio (Rubrica 3.4).
"""

# --- AGUA Y RIEGO (US-002, US-008, US-012) ---
AGUA_INICIAL_PLANTACION = 500  # Litros
AGUA_MINIMA_RIEGO = 10         # Litros consumidos por riego

# --- CULTIVOS (US-004 a US-007) ---
# Pino
SUPERFICIE_PINO = 2.0        # m²
AGUA_INICIAL_PINO = 2        # Litros
ALTURA_INICIAL_ARBOL = 1.0   # Metros (usado por Pino)
CRECIMIENTO_PINO = 0.10      # Metros por riego

# Olivo
SUPERFICIE_OLIVO = 3.0       # m²
AGUA_INICIAL_OLIVO = 5       # Litros
ALTURA_INICIAL_OLIVO = 0.5   # Metros (mas bajo que pino)
CRECIMIENTO_OLIVO = 0.01     # Metros por riego

# Lechuga
SUPERFICIE_LECHUGA = 0.10    # m²
AGUA_INICIAL_LECHUGA = 1     # Litros

# Zanahoria
SUPERFICIE_ZANAHORIA = 0.15  # m²
AGUA_INICIAL_ZANAHORIA = 0   # Litros

# --- ESTRATEGIAS DE ABSORCION (US-008, US-TECH-004) ---
# Seasonal (Arboles)
ABSORCION_SEASONAL_VERANO = 5    # Litros
ABSORCION_SEASONAL_INVIERNO = 2  # Litros
MES_INICIO_VERANO = 3            # Marzo
MES_FIN_VERANO = 8               # Agosto

# Constante (Hortalizas)
ABSORCION_CONSTANTE_LECHUGA = 1  # Litros
ABSORCION_CONSTANTE_ZANAHORIA = 2 # Litros

# --- SISTEMA DE RIEGO (US-010, US-011, US-012, US-013) ---
# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25               # °C
SENSOR_TEMP_MAX = 50                # °C

INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
SENSOR_HUMEDAD_MIN = 0              # %
SENSOR_HUMEDAD_MAX = 100            # %

# Control
INTERVALO_CONTROL_RIEGO = 2.5       # segundos
TEMP_MIN_RIEGO = 8                  # °C
TEMP_MAX_RIEGO = 15                 # °C
HUMEDAD_MAX_RIEGO = 50              # %

# Threading
THREAD_JOIN_TIMEOUT = 2.0           # segundos

# --- PERSISTENCIA (US-021) ---
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/66: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/66: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/66: arbol.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/66: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/66: hortaliza.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/66: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/66: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 10/66: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 11/66: tipo_aceituna.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

"""Define el Enum para los tipos de aceituna (US-005)."""

# Standard library
from enum import Enum, auto


class TipoAceituna(Enum):
    """Tipos de aceituna disponibles para Olivos."""
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ==============================================================================
# ARCHIVO 12/66: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 13/66: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/66: apto_medico.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

"""Entidad AptoMedico (US-015)."""

# Standard library
from datetime import date
from typing import Optional


class AptoMedico:
    """Entidad que certifica la aptitud medica de un trabajador."""

    def __init__(
        self,
        esta_apto: bool,
        fecha_emision: date,
        observaciones: Optional[str] = None
    ):
        """
        Inicializa el Apto Medico.

        Args:
            esta_apto: True si esta apto, False si no.
            fecha_emision: Fecha de emision del certificado.
            observaciones: Observaciones medicas (opcional).
        """
        self._esta_apto = esta_apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._esta_apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> Optional[str]:
        return self._observaciones

# ==============================================================================
# ARCHIVO 15/66: estado_tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\estado_tarea.py
# ==============================================================================

"""Define el Enum para el estado de una Tarea (US-014)."""

# Standard library
from enum import Enum, auto


class EstadoTarea(Enum):
    """Estado de ejecucion de una tarea."""
    PENDIENTE = auto()
    COMPLETADA = auto()

# ==============================================================================
# ARCHIVO 16/66: herramienta.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

"""Entidad Herramienta (US-016)."""

class Herramienta:
    """Entidad Herramienta utilizada por un trabajador."""

    def __init__(
        self,
        id_herramienta: int,
        nombre: str,
        certificado_hys: bool
    ):
        """
        Inicializa la Herramienta.

        Args:
            id_herramienta: ID unico de la herramienta.
            nombre: Nombre (ej. Pala).
            certificado_hys: Si posee certificacion de Higiene y Seguridad.
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_nombre(self) -> str:
        return self._nombre

# ==============================================================================
# ARCHIVO 17/66: tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

"""Entidad Tarea (US-014)."""

# Standard library
from datetime import date

# Local application
from python_forestacion.entidades.personal.estado_tarea import EstadoTarea


class Tarea:
    """Entidad Tarea asignada a un trabajador."""

    def __init__(
        self,
        id_tarea: int,
        fecha_programada: date,
        descripcion: str
    ):
        """
        Inicializa la Tarea.

        Args:
            id_tarea: ID unico de la tarea.
            fecha_programada: Fecha de ejecucion.
            descripcion: Descripcion.
        """
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._estado: EstadoTarea = EstadoTarea.PENDIENTE

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> EstadoTarea:
        return self._estado

    def completar_tarea(self) -> None:
        """Marca la tarea como completada."""
        self._estado = EstadoTarea.COMPLETADA

# ==============================================================================
# ARCHIVO 18/66: trabajador.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

"""Entidad Trabajador (US-014)."""

# Standard library
from typing import List, Optional

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea


class Trabajador:
    """Entidad Trabajador agricola."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        """
        Inicializa el Trabajador.

        Args:
            dni: DNI unico.
            nombre: Nombre completo.
            tareas: Lista de tareas asignadas.
        """
        self._dni = dni
        self._nombre = nombre
        # Defensive copy (Rubrica 5.2)
        self._tareas: List[Tarea] = tareas.copy()
        self._apto_medico: Optional[AptoMedico] = None  # Sin apto inicial

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        """Retorna copia de la lista de tareas (US-014)."""
        return self._tareas.copy()

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico) -> None:
        """Asigna o actualiza el apto medico."""
        self._apto_medico = apto


################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/66: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/66: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

"""Entidad Plantacion (US-002)."""

# Standard library
from typing import TYPE_CHECKING, List

# Local application
from python_forestacion import constantes
from python_forestacion.excepciones.mensajes_exception import TECH_AGUA_NEGATIVA

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """Entidad Plantacion, gestiona cultivos y recursos."""

    def __init__(self, nombre: str, superficie_maxima: float):
        """
        Inicializa la Plantacion.

        Args:
            nombre: Nombre identificatorio.
            superficie_maxima: Superficie maxima (heredada de Tierra).
        """
        self._nombre = nombre
        self._superficie_maxima = superficie_maxima
        self._superficie_ocupada = 0.0
        self._agua_disponible = constantes.AGUA_INICIAL_PLANTACION  # 500L
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_maxima(self) -> float:
        return self._superficie_maxima

    def get_superficie_ocupada(self) -> float:
        return self._superficie_ocupada

    def set_superficie_ocupada(self, superficie: float) -> None:
        self._superficie_ocupada = superficie

    def get_superficie_disponible(self) -> float:
        """Calcula la superficie restante."""
        return self._superficie_maxima - self._superficie_ocupada

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def set_agua_disponible(self, agua: float) -> None:
        """
        Establece el agua disponible, validando que no sea negativa (US-002).

        Args:
            agua: Nueva cantidad de agua.

        Raises:
            ValueError: Si el agua es < 0.
        """
        if agua < 0:
            raise ValueError(TECH_AGUA_NEGATIVA)
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """
        Retorna una copia de la lista de cultivos (Defensive Copy).
        Cumple con Rubrica 5.2.
        """
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo y actualiza la superficie ocupada."""
        self._cultivos.append(cultivo)
        self._superficie_ocupada += cultivo.get_superficie()

    def remover_cultivo(self, cultivo: 'Cultivo') -> None:
        """Remueve un cultivo (usado en cosecha) y libera superficie."""
        try:
            self._cultivos.remove(cultivo)
            self._superficie_ocupada -= cultivo.get_superficie()
        except ValueError:
            pass  # Ignorar si no esta

    def get_trabajadores(self) -> List['Trabajador']:
        """
        Retorna una copia de la lista de trabajadores (Defensive Copy).
        Cumple con Rubrica 5.2 y US-017.
        """
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """Reemplaza la lista de trabajadores (US-017)."""
        self._trabajadores = trabajadores.copy()

# ==============================================================================
# ARCHIVO 21/66: registro_forestal.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

"""Entidad RegistroForestal (US-003)."""

# Standard library
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """Entidad que vincula Tierra, Plantacion y Propietario."""

    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa el Registro Forestal.

        Args:
            id_padron: ID de padron (de la Tierra).
            tierra: Objeto Tierra.
            plantacion: Objeto Plantacion.
            propietario: Nombre del propietario.
            avaluo: Avaluo fiscal.
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

# ==============================================================================
# ARCHIVO 22/66: tierra.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

"""Entidad Tierra (US-001)."""

# Standard library
from typing import TYPE_CHECKING, Optional

# Local application
from python_forestacion.excepciones.mensajes_exception import (
    TECH_SUPERFICIE_NEGATIVA,
)

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """Entidad Tierra, representa el terreno catastral."""

    def __init__(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str
    ):
        """
        Inicializa la Tierra.

        Args:
            id_padron_catastral: Numero unico.
            superficie: Superficie en m².
            domicilio: Ubicacion.
        """
        self._id_padron_catastral = id_padron_catastral
        self._superficie = 0.0  # Inicializa en 0
        self.set_superficie(superficie)  # Usa el setter para validar
        self._domicilio = domicilio
        self._finca: Optional['Plantacion'] = None

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie, validando que sea positiva (US-001).

        Args:
            superficie: Nueva superficie.

        Raises:
            ValueError: Si la superficie es <= 0.
        """
        if superficie <= 0:
            raise ValueError(TECH_SUPERFICIE_NEGATIVA)
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional['Plantacion']:
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """Asocia una plantacion (finca) a este terreno."""
        self._finca = finca


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/66: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/66: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/66: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 26/66: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 27/66: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 28/66: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 29/66: tipo_operacion_persistencia.py
# Directorio: excepciones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\excepciones\tipo_operacion_persistencia.py
# ==============================================================================

"""Define el Enum para el tipo de operacion de persistencia."""

# Standard library
from enum import Enum, auto


class TipoOperacionPersistencia(Enum):
    """Tipos de operaciones de persistencia para logging de excepciones."""
    LECTURA = auto()
    ESCRITURA = auto()


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 30/66: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 31/66: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/66: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

"""
Implementacion del Patron Factory Method (US-TECH-002).
Centraliza la creacion de cultivos, desacoplando al cliente.
"""

# Standard library
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para crear instancias de Cultivo.
    Usa un diccionario de factories (Rubrica 1.2)
    en lugar de if/elif.
    """

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """Metodo de factory privado para Pino."""
        # Imports locales para evitar dependencia circular
        # y cargar solo cuando es necesario.
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")  # Variedad por defecto

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """Metodo de factory privado para Olivo."""
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)  # Default

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """Metodo de factory privado para Lechuga."""
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")  # Default

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """Metodo de factory privado para Zanahoria."""
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=False)  # Default

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Metodo Factory principal (publico).

        Args:
            especie: El nombre del tipo de cultivo a crear.

        Returns:
            Una instancia de un subtipo de Cultivo.

        Raises:
            ValueError: Si la especie es desconocida.
        """
        # Diccionario de factories (US-TECH-002)
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        # Dispatch
        factory_method = factories.get(especie)

        if not factory_method:
            raise ValueError(f"Especie desconocida: {especie}")

        # Retorna el tipo base (Cultivo) para desacoplar
        return factory_method()


################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 33/66: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/66: evento_sensor.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\evento_sensor.py
# ==============================================================================

"""
Define el objeto de evento para el patron Observer.

Esto es necesario para cumplir con la US-012 (observar ambos sensores)
y la US-TECH-003 (usar Generics) de forma robusta.
En lugar de Observable[float], usaremos Observable[EventoSensor].
"""

# Standard library
from dataclasses import dataclass

# Local application
from python_forestacion.patrones.observer.tipo_evento_sensor import TipoEventoSensor


@dataclass(frozen=True)
class EventoSensor:
    """Objeto de datos inmutable que representa un evento de sensor."""
    tipo: TipoEventoSensor
    valor: float

# ==============================================================================
# ARCHIVO 35/66: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\observable.py
# ==============================================================================

"""
Implementacion de la clase base Observable (US-TECH-003).
Usa Generics (TypeVar) y es Thread-Safe (Rubrica 1.3).
"""

# Standard library
from abc import ABC
from threading import Lock
from typing import Generic, List, TypeVar

# Local application
from python_forestacion.patrones.observer.observer import Observer

# Define el tipo generico T
T = TypeVar('T')


class Observable(Generic[T], ABC):
    """Clase base Observable (Sujeto)."""

    def __init__(self):
        """Inicializa el observable con una lista vacia de observadores y un Lock."""
        self._observadores: List[Observer[T]] = []
        self._lock = Lock()  # Para thread-safety (Rubrica 1.3)

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista de notificaciones.

        Args:
            observador: Instancia que implementa la interfaz Observer[T].
        """
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Instancia a eliminar.
        """
        with self._lock:
            try:
                self._observadores.remove(observador)
            except ValueError:
                pass  # Ignorar si no esta en la lista

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores suscritos sobre un evento.
        Crea una copia de la lista para notificar (thread-safe).

        Args:
            evento: El objeto de evento (T) a enviar.
        """
        # Se notifica sobre una copia de la lista para evitar problemas
        # de concurrencia si un observador intenta desuscribirse
        # durante la notificacion.
        with self._lock:
            observadores_a_notificar = self._observadores[:]

        for observador in observadores_a_notificar:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 36/66: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\observer.py
# ==============================================================================

"""
Implementacion de la interfaz Observer (US-TECH-003).
Usa Generics (TypeVar) para tipo-seguridad.
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Local application
# (Usamos EventoSensor como T, en lugar de float, para distinguir fuentes)
from python_forestacion.patrones.observer.evento_sensor import EventoSensor

# Define el tipo generico T
T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz abstracta Observer (Observador)."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado por el Observable cuando hay un cambio.

        Args:
            evento: El objeto de evento (T) con los datos del cambio.
        """
        pass

# ==============================================================================
# ARCHIVO 37/66: tipo_evento_sensor.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\tipo_evento_sensor.py
# ==============================================================================

"""Define el Enum para los tipos de eventos de sensor."""

# Standard library
from enum import Enum, auto


class TipoEventoSensor(Enum):
    """Tipos de eventos de sensor para el patron Observer."""
    TEMPERATURA = auto()
    HUMEDAD = auto()


################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/66: absorcion_agua_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ==============================================================================

"""
Implementacion de la interfaz Strategy (US-TECH-004).
Define el contrato para las estrategias de absorcion de agua.
"""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """Interfaz abstracta Strategy (Estrategia)."""

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua absorbida por un cultivo.

        Args:
            fecha: Fecha actual (para estrategias estacionales).
            cultivo: El cultivo que absorbe el agua.

        Returns:
            Cantidad de agua (en litros) absorbida.
        """
        pass


################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 40/66: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/66: absorcion_constante_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

"""Implementacion Concreta 1: Absorcion Constante (US-TECH-004)."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia para hortalizas: absorbe siempre la misma cantidad."""

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia.

        Args:
            cantidad_constante: Cantidad fija de agua a absorber.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna la cantidad constante.

        Args:
            fecha: No utilizada en esta estrategia.
            cultivo: No utilizado en esta estrategia.

        Returns:
            Cantidad de agua (en litros) configurada.
        """
        return self._cantidad

# ==============================================================================
# ARCHIVO 42/66: absorcion_seasonal_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

"""Implementacion Concreta 2: Absorcion Estacional (US-TECH-004)."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia para arboles: absorbe segun la estacion (verano/invierno)."""

    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la absorcion basada en el mes actual.

        Args:
            fecha: Fecha actual para determinar el mes.
            cultivo: No utilizado en esta estrategia.

        Returns:
            Cantidad de agua (en litros) segun la estacion.
        """
        mes = fecha.month
        if constantes.MES_INICIO_VERANO <= mes <= constantes.MES_FIN_VERANO:
            return constantes.ABSORCION_SEASONAL_VERANO
        else:
            return constantes.ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: riego
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego\control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: riego\control
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: riego\control
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

"""Implementacion del Control de Riego Automatizado (US-012)."""

# Standard library
import threading
import time
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
# Excepciones
from python_forestacion.excepciones.agua_agotada_exception import (
    AguaAgotadaException,
)
# Patrones
from python_forestacion.patrones.observer.evento_sensor import EventoSensor
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.tipo_evento_sensor import TipoEventoSensor

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.riego.sensores.humedad_reader_task import (
        HumedadReaderTask,
    )
    from python_forestacion.riego.sensores.temperatura_reader_task import (
        TemperaturaReaderTask,
    )
    from python_forestacion.servicios.terrenos.plantacion_service import (
        PlantacionService,
    )


class ControlRiegoTask(threading.Thread, Observer[EventoSensor]):
    """
    Controlador de Riego.
    Es un Thread daemon y un Observer (US-012, US-TECH-003).
    """

    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa el controlador.
        Inyecta dependencias (sensores y servicios).

        Args:
            sensor_temperatura: Observable de temperatura.
            sensor_humedad: Observable de humedad.
            plantacion: La plantacion a regar.
            plantacion_service: Servicio para ejecutar el riego.
        """
        threading.Thread.__init__(self, daemon=True)
        self._detenido = threading.Event()
        self._lock = threading.Lock()  # Lock para actualizar valores

        # Dependencias inyectadas
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad

        # Estado interno (ultimas lecturas)
        self._ultima_temperatura = sensor_temperatura.get_ultima_lectura()
        self._ultima_humedad = sensor_humedad.get_ultima_lectura()

        # Suscripcion a los Observables (US-012)
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: EventoSensor) -> None:
        """
        Metodo del Observer (US-012).
        Actualiza el estado interno de forma thread-safe.

        Args:
            evento: Objeto EventoSensor (distingue temp/hum).
        """
        with self._lock:
            if evento.tipo == TipoEventoSensor.TEMPERATURA:
                self._ultima_temperatura = evento.valor
                print(f"[CONTROL] Nueva Temp: {evento.valor:.1f}°C")
            elif evento.tipo == TipoEventoSensor.HUMEDAD:
                self._ultima_humedad = evento.valor
                print(f"[CONTROL] Nueva Hum: {evento.valor:.1f}%")

    def run(self) -> None:
        """
        Bucle principal del thread.
        Evalua condiciones de riego periodicamente (US-012).
        """
        while not self._detenido.is_set():
            # 1. Leer valores actuales (thread-safe)
            with self._lock:
                temp = self._ultima_temperatura
                hum = self._ultima_humedad

            # 2. Logica de decision (US-012)
            if (constantes.TEMP_MIN_RIEGO <= temp <= constantes.TEMP_MAX_RIEGO
                    and hum < constantes.HUMEDAD_MAX_RIEGO):
                
                print(f"[CONTROL] CONDICION CUMPLIDA (Temp: {temp:.1f}°C, "
                      f"Hum: {hum:.1f}%). Intentando regar...")
                try:
                    # 3. Regar
                    self._plantacion_service.regar(self._plantacion)
                    print("[CONTROL] Riego automatico ejecutado.")
                except AguaAgotadaException as e:
                    print(f"[CONTROL] NO SE PUDO REGAR: {e.get_user_message()}")
            else:
                # 4. No regar
                print(f"[CONTROL] Condicion NO cumplida (Temp: {temp:.1f}°C, "
                      f"Hum: {hum:.1f}%). No se riega.")

            # 5. Esperar intervalo
            self._detenido.wait(constantes.INTERVALO_CONTROL_RIEGO)

    def detener(self) -> None:
        """Establece la bandera para detener el thread (US-013)."""
        print("\n[CONTROL] Deteniendo sistema de riego...")
        self._detenido.set()
        # Desuscribirse (buena practica)
        self._sensor_temperatura.eliminar_observador(self)
        self._sensor_humedad.eliminar_observador(self)


################################################################################
# DIRECTORIO: riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

"""Implementacion del Sensor de Humedad (US-011)."""

# Standard library
import random
import threading
import time
from typing import Optional

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.observer.evento_sensor import EventoSensor
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.tipo_evento_sensor import TipoEventoSensor


class HumedadReaderTask(threading.Thread, Observable[EventoSensor]):
    """
    Sensor de Humedad.
    Es un Thread daemon y un Observable (US-011, US-TECH-003).
    """

    def __init__(self):
        """Inicializa el thread y el observable."""
        threading.Thread.__init__(self, daemon=True)  # Thread daemon
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_lectura: float = (
            constantes.SENSOR_HUMEDAD_MIN + constantes.SENSOR_HUMEDAD_MAX
        ) / 2

    def _leer_humedad(self) -> float:
        """Simula la lectura de un sensor real."""
        # Simula una fluctuacion suave
        cambio = random.uniform(-3.0, 3.0)
        nueva_hum = self._ultima_lectura + cambio
        # Mantiene la humedad dentro de los limites
        self._ultima_lectura = max(
            constantes.SENSOR_HUMEDAD_MIN,
            min(constantes.SENSOR_HUMEDAD_MAX, nueva_hum)
        )
        return self._ultima_lectura

    def run(self) -> None:
        """
        Bucle principal del thread.
        Lee humedad y notifica a observadores (US-011).
        """
        while not self._detenido.is_set():
            # 1. Leer humedad
            hum = self._leer_humedad()

            # 2. Crear evento
            evento = EventoSensor(tipo=TipoEventoSensor.HUMEDAD, valor=hum)

            # 3. Notificar observadores (thread-safe)
            self.notificar_observadores(evento)

            # 4. Esperar intervalo
            self._detenido.wait(constantes.INTERVALO_SENSOR_HUMEDAD)

    def detener(self) -> None:
        """Establece la bandera para detener el thread (US-013)."""
        self._detenido.set()

    def get_ultima_lectura(self) -> float:
        """Permite a los 'pollers' obtener el ultimo valor."""
        return self._ultima_lectura

# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

"""Implementacion del Sensor de Temperatura (US-010)."""

# Standard library
import random
import threading
import time
from typing import Optional

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.observer.evento_sensor import EventoSensor
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.tipo_evento_sensor import TipoEventoSensor


class TemperaturaReaderTask(threading.Thread, Observable[EventoSensor]):
    """
    Sensor de Temperatura.
    Es un Thread daemon y un Observable (US-010, US-TECH-003).
    """

    def __init__(self):
        """Inicializa el thread y el observable."""
        threading.Thread.__init__(self, daemon=True)  # Thread daemon
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_lectura: float = (
            constantes.SENSOR_TEMP_MIN + constantes.SENSOR_TEMP_MAX
        ) / 2

    def _leer_temperatura(self) -> float:
        """Simula la lectura de un sensor real."""
        # Simula una fluctuacion suave
        cambio = random.uniform(-1.5, 1.5)
        nueva_temp = self._ultima_lectura + cambio
        # Mantiene la temperatura dentro de los limites
        self._ultima_lectura = max(
            constantes.SENSOR_TEMP_MIN,
            min(constantes.SENSOR_TEMP_MAX, nueva_temp)
        )
        return self._ultima_lectura

    def run(self) -> None:
        """
        Bucle principal del thread.
        Lee temperatura y notifica a observadores (US-010).
        """
        while not self._detenido.is_set():
            # 1. Leer temperatura
            temp = self._leer_temperatura()

            # 2. Crear evento
            evento = EventoSensor(tipo=TipoEventoSensor.TEMPERATURA, valor=temp)

            # 3. Notificar observadores (thread-safe)
            self.notificar_observadores(evento)

            # 4. Esperar intervalo
            self._detenido.wait(constantes.INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        """Establece la bandera para detener el thread (US-013)."""
        self._detenido.set()

    def get_ultima_lectura(self) -> float:
        """Permite a los 'pollers' obtener el ultimo valor."""
        return self._ultima_lectura


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

"""Servicio base para todos los cultivos."""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import (
    AbsorcionAguaStrategy,
)

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para la logica de negocio de Cultivos.
    Implementa la inyeccion del patron Strategy (US-TECH-004).
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio inyectando la estrategia de absorcion.

        Args:
            estrategia_absorcion: Instancia de la estrategia a usar.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Delega el calculo de absorcion a la estrategia inyectada.

        Args:
            cultivo: El cultivo que absorbe.

        Returns:
            Cantidad de agua absorbida.
        """
        # Fecha actual (simplificado, podria inyectarse)
        fecha = date.today()

        # Delegacion al patron Strategy (US-TECH-004)
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha,
            cultivo
        )

        # Actualizar estado de la entidad
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Metodo abstracto para mostrar datos especificos.
        Implementa la base para el dispatch del Registry (US-009).
        """
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

"""
Implementacion de patrones Singleton y Registry (US-TECH-001, US-TECH-005).

- Singleton: Garantiza una unica instancia thread-safe del registro.
- Registry: Elimina cascadas de isinstance() mediante dispatch polimorfico.
"""

# Standard library
from threading import Lock
from typing import TYPE_CHECKING, Any, Callable, Dict, Optional, Type

# Local application
# Entidades (para las llaves del diccionario)
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
# Servicios (para instanciar)
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.zanahoria_service import (
    ZanahoriaService,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoServiceRegistry:
    """
    Implementa Singleton (thread-safe) y Registry.
    Mapea tipos de Cultivo a sus servicios correspondientes.
    """
    # --- Implementacion de Singleton (US-TECH-001, Rubrica 1.1) ---
    _instance: Optional['CultivoServiceRegistry'] = None
    _lock: Lock = Lock()

    def __new__(cls) -> 'CultivoServiceRegistry':
        """Controla la instanciacion (Singleton)."""
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    # Inicializacion perezosa: inicializar servicios
                    # solo la primera vez que se crea la instancia.
                    cls._instance._inicializar_servicios_y_registro()
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """Metodo de acceso publico al Singleton."""
        if cls._instance is None:
            cls()  # Llama a __new__ si no existe
        return cls._instance  # type: ignore

    # --- Implementacion de Registry (US-TECH-005, Rubrica 1.5) ---
    def _inicializar_servicios_y_registro(self) -> None:
        """
        Inicializa los servicios y construye los diccionarios de handlers.
        Se llama una unica vez desde __new__.
        """
        # 1. Instanciar servicios
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # 2. Construir handlers para 'absorber_agua'
        self._absorber_agua_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        # 3. Construir handlers para 'mostrar_datos'
        self._mostrar_datos_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def _dispatch(
        self,
        cultivo: 'Cultivo',
        handlers: Dict[Type['Cultivo'], Callable]
    ) -> Any:
        """Metodo de dispatch generico."""
        tipo_cultivo = type(cultivo)
        handler = handlers.get(tipo_cultivo)

        if not handler:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo_cultivo}")

        return handler(cultivo)

    # --- Metodos publicos del Registry (Dispatch) ---

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """Dispatch polimorfico para absorber agua."""
        return self._dispatch(cultivo, self._absorber_agua_handlers)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Dispatch polimorfico para mostrar datos (US-009)."""
        self._dispatch(cultivo, self._mostrar_datos_handlers)

    # --- Handlers privados (NO lambdas - Rubrica 3.4) ---

    # Handlers para absorber_agua
    def _absorber_agua_pino(self, cultivo: 'Cultivo') -> int:
        return self._pino_service.absorver_agua(cultivo)  # type: ignore

    def _absorber_agua_olivo(self, cultivo: 'Cultivo') -> int:
        return self._olivo_service.absorver_agua(cultivo)  # type: ignore

    def _absorber_agua_lechuga(self, cultivo: 'Cultivo') -> int:
        return self._lechuga_service.absorver_agua(cultivo)  # type: ignore

    def _absorber_agua_zanahoria(self, cultivo: 'Cultivo') -> int:
        return self._zanahoria_service.absorver_agua(cultivo)  # type: ignore

    # Handlers para mostrar_datos
    def _mostrar_datos_pino(self, cultivo: 'Cultivo') -> None:
        self._pino_service.mostrar_datos(cultivo)  # type: ignore

    def _mostrar_datos_olivo(self, cultivo: 'Cultivo') -> None:
        self._olivo_service.mostrar_datos(cultivo)  # type: ignore

    def _mostrar_datos_lechuga(self, cultivo: 'Cultivo') -> None:
        self._lechuga_service.mostrar_datos(cultivo)  # type: ignore

    def _mostrar_datos_zanahoria(self, cultivo: 'Cultivo') -> None:
        self._zanahoria_service.mostrar_datos(cultivo)  # type: ignore

# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

"""Servicio especifico para Lechuga."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio con logica de negocio para Lechugas."""

    def __init__(self):
        """Inyecta la estrategia Constante (US-TECH-004)."""
        super().__init__(
            AbsorcionConstanteStrategy(constantes.ABSORCION_CONSTANTE_LECHUGA)
        )

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos especificos de Lechuga (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.requiere_invernadero()}")

# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

"""Servicio especifico para Olivo."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio con logica de negocio para Olivos."""

    def __init__(self):
        """Inyecta la estrategia Seasonal (US-TECH-004)."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Olivo') -> int:
        """Sobrescribe para agregar crecimiento (US-008)."""
        agua_absorvida = super().absorver_agua(cultivo)
        if agua_absorvida > 0:
            self.crecer(cultivo, constantes.CRECIMIENTO_OLIVO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos especificos de Olivo (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")

# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

"""Servicio especifico para Pino."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import (
    AbsorcionSeasonalStrategy,
)
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio con logica de negocio para Pinos."""

    def __init__(self):
        """Inyecta la estrategia Seasonal (US-TECH-004)."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Pino') -> int:
        """Sobrescribe para agregar crecimiento (US-008)."""
        agua_absorvida = super().absorver_agua(cultivo)
        if agua_absorvida > 0:
            self.crecer(cultivo, constantes.CRECIMIENTO_PINO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos especificos de Pino (US-009)."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")

# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

"""Servicio especifico para Zanahoria."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import (
    AbsorcionConstanteStrategy,
)
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio con logica de negocio para Zanahorias."""

    def __init__(self):
        """Inyecta la estrategia Constante (US-TECH-004)."""
        super().__init__(
            AbsorcionConstanteStrategy(constantes.ABSORCION_CONSTANTE_ZANAHORIA)
        )

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos especificos de Zanahoria (US-009)."""
        super().mostrar_datos(cultivo)
        tipo = "Baby Carrot" if cultivo.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")


################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/66: fincas_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

"""Servicio de alto nivel para gestionar multiples fincas (US-018)."""

# Standard library
from typing import Dict, Generic, Optional, Type, TypeVar

# Local application
# Entidades
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import (
    RegistroForestal,
)
# Servicios
from python_forestacion.servicios.negocio.paquete import Paquete

# Tipo generico para cosecha (US-020)
T_Cultivo = TypeVar('T_Cultivo', bound=Cultivo)


class FincasService:
    """Servicio de negocio para operar sobre multiples fincas."""

    def __init__(self):
        """Inicializa el servicio con un diccionario de fincas."""
        self._fincas: Dict[int, RegistroForestal] = {}

    def add_finca(self, registro: RegistroForestal) -> None:
        """Agrega una finca (RegistroForestal) al servicio (US-018)."""
        id_padron = registro.get_id_padron()
        if id_padron not in self._fincas:
            self._fincas[id_padron] = registro
            print(f"[NEGOCIO] Finca con padron {id_padron} agregada.")
        else:
            print(f"[NEGOCIO] Finca con padron {id_padron} actualizada.")

    def buscar_finca(self, id_padron: int) -> Optional[RegistroForestal]:
        """Busca una finca por ID de padron (US-018)."""
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga una plantacion especifica (US-019)."""
        finca = self.buscar_finca(id_padron)
        if finca:
            print(f"\n[NEGOCIO] Fumigando plantacion "
                  f"'{finca.get_plantacion().get_nombre()}' "
                  f"con: {plaguicida}")
            # Logica de fumigacion (aqui solo imprimimos)
        else:
            print(f"[NEGOCIO] Error: Finca {id_padron} no encontrada.")

    def cosechar_y_empaquetar(
        self,
        tipo_cultivo: Type[T_Cultivo]
    ) -> Paquete[T_Cultivo]:
        """
        Cosecha todos los cultivos de un tipo especifico de
        TODAS las fincas gestionadas (US-020).

        Args:
            tipo_cultivo: La clase del cultivo a cosechar (ej. Lechuga).

        Returns:
            Un Paquete[T_Cultivo] tipo-seguro con los items cosechados.
        """
        print(f"\n[NEGOCIO] Iniciando cosecha de: {tipo_cultivo.__name__}...")
        paquete = Paquete(tipo_cultivo)
        cultivos_a_remover = []

        # 1. Buscar en todas las fincas
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            # Iteramos sobre una copia para poder modificar la lista original
            for cultivo in plantacion.get_cultivos():
                # 2. Cosechar por tipo (US-020)
                if isinstance(cultivo, tipo_cultivo):
                    # Aseguramos el tipo para el Paquete generico
                    cultivo_especifico = cultivo  # type: T_Cultivo
                    paquete.agregar_item(cultivo_especifico)
                    # Marcar para remover (no modificar lista mientras se itera)
                    cultivos_a_remover.append((plantacion, cultivo))

        # 3. Remover de las plantaciones
        for plantacion, cultivo in cultivos_a_remover:
            plantacion.remover_cultivo(cultivo)

        print(f"[NEGOCIO] COSECHANDO {paquete.get_cantidad()} unidades "
              f"de {tipo_cultivo.__name__}")

        return paquete

# ==============================================================================
# ARCHIVO 60/66: paquete.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\negocio\paquete.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

"""Servicio para la entidad Trabajador."""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.estado_tarea import EstadoTarea
from python_forestacion.entidades.personal.tarea import Tarea

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.trabajador import Trabajador


class TrabajadorService:
    """Servicio con logica de negocio para Trabajador."""

    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        """
        Crea y asigna un AptoMedico a un trabajador (US-015).

        Args:
            trabajador: El trabajador a certificar.
            apto: Si esta apto o no.
            fecha_emision: Fecha del certificado.
            observaciones: Comentarios medicos.
        """
        apto_medico = AptoMedico(
            esta_apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )
        trabajador.set_apto_medico(apto_medico)

    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """
        Metodo helper estatico para el ordenamiento (US-016).
        Evita el uso de lambdas (Rubrica 3.4).
        """
        return tarea.get_id_tarea()

    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas al trabajador (US-016).

        Args:
            trabajador: El trabajador que ejecuta.
            fecha: Fecha actual.
            util: Herramienta a utilizar.

        Returns:
            True si pudo trabajar, False si no tenia apto medico.
        """
        apto_medico = trabajador.get_apto_medico()

        # 1. Validar apto medico (US-016)
        if apto_medico is None or not apto_medico.esta_apto():
            print(f"\n[PERSONAL] El trabajador {trabajador.get_nombre()} "
                  "NO puede trabajar. Apto medico invalido.")
            return False

        print(f"\n[PERSONAL] El trabajador {trabajador.get_nombre()} "
              "comienza a trabajar con {util.get_nombre()}...")

        # 2. Obtener tareas (copia)
        tareas = trabajador.get_tareas()

        # 3. Ordenar tareas por ID descendente (US-016)
        # Se usa el metodo helper estatico en lugar de lambda
        tareas_ordenadas = sorted(
            tareas,
            key=self._obtener_id_tarea,
            reverse=True
        )

        # 4. Ejecutar tareas
        tareas_ejecutadas_hoy = 0
        for tarea in tareas_ordenadas:
            if (tarea.get_fecha_programada() == fecha and
                    tarea.get_estado() == EstadoTarea.PENDIENTE):

                print(f"  -> Realizando tarea {tarea.get_id_tarea()}: "
                      f"{tarea.get_descripcion()}")
                tarea.completar_tarea()  # Modifica la tarea original
                tareas_ejecutadas_hoy += 1

        if tareas_ejecutadas_hoy == 0:
            print(f"  -> No hay tareas pendientes para hoy ({fecha}).")
        else:
            print(f"[PERSONAL] Tareas de {trabajador.get_nombre()} "
                  "completadas exitosamente.")

        return True


################################################################################
# DIRECTORIO: servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

"""Servicio para la entidad Plantacion."""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion import constantes
# Excepciones
from python_forestacion.excepciones.agua_agotada_exception import (
    AguaAgotadaException,
)
from python_forestacion.excepciones.superficie_insuficiente_exception import (
    SuperficieInsuficienteException,
)
# Patrones
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
# Servicios (Registry)
from python_forestacion.servicios.cultivos.cultivo_service_registry import (
    CultivoServiceRegistry,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """Servicio con logica de negocio para Plantacion."""

    def __init__(self):
        """Inicializa el servicio obteniendo el Registry Singleton."""
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(
        self,
        plantacion: 'Plantacion',
        especie: str,
        cantidad: int
    ) -> None:
        """
        Planta multiples cultivos en la plantacion (US-004 a US-007).
        Usa Factory Method para crear cultivos.
        Verifica la superficie disponible.

        Args:
            plantacion: La plantacion donde plantar.
            especie: El tipo de cultivo (ej. "Pino").
            cantidad: Numero de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay espacio.
            ValueError: Si la especie es desconocida (desde Factory).
        """
        # 1. Crear un cultivo temporal para saber su superficie
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie_disponible()

        # 2. Validar superficie (US-004)
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=superficie_disponible
            )

        # 3. Plantar (usando Factory)
        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantacion (US-008).
        Usa el patron Strategy (via Registry) para la absorcion.

        Args:
            plantacion: La plantacion a regar.

        Raises:
            AguaAgotadaException: Si no hay agua para el riego.
        """
        agua_requerida = constantes.AGUA_MINIMA_RIEGO
        agua_disponible = plantacion.get_agua_disponible()

        # 1. Validar agua disponible (US-008)
        if agua_disponible < agua_requerida:
            raise AguaAgotadaException(
                agua_requerida=agua_requerida,
                agua_disponible=agua_disponible
            )

        # 2. Consumir agua de la plantacion
        plantacion.set_agua_disponible(agua_disponible - agua_requerida)
        print(f"\n[RIEGO] Consumidos {agua_requerida}L. "
              f"Quedan {plantacion.get_agua_disponible()}L.")

        # 3. Distribuir agua a cultivos (usando Registry + Strategy)
        for cultivo in plantacion.get_cultivos():
            try:
                # El Registry despacha al servicio correcto,
                # y el servicio delega a la Estrategia correcta.
                agua_absorvida = self._registry.absorber_agua(cultivo)
                print(f"  -> {type(cultivo).__name__} ID "
                      f"{str(cultivo.get_id())[:4]}... "
                      f"absorbio {agua_absorvida}L.")
            except Exception as e:
                print(f"Error al regar cultivo {cultivo.get_id()}: {e}")

# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

"""Servicio para la entidad RegistroForestal (US-003, US-021, US-022)."""

# Standard library
import os
import pickle
from typing import TYPE_CHECKING, Optional

# Local application
from python_forestacion import constantes
# Excepciones
from python_forestacion.excepciones.mensajes_exception import (
    TECH_ARCHIVO_CORRUPTO,
    TECH_ARCHIVO_NO_ENCONTRADO,
    TECH_PROPIETARIO_NULO,
    USER_ARCHIVO_CORRUPTO,
    USER_ARCHIVO_NO_ENCONTRADO,
    USER_VALOR_INVALIDO,
)
from python_forestacion.excepciones.persistencia_exception import (
    PersistenciaException,
)
from python_forestacion.excepciones.tipo_operacion_persistencia import (
    TipoOperacionPersistencia,
)
# Servicios
from python_forestacion.servicios.cultivos.cultivo_service_registry import (
    CultivoServiceRegistry,
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import (
        RegistroForestal,
    )


class RegistroForestalService:
    """Servicio para logica de RegistroForestal (mostrar, persistir)."""

    def __init__(self):
        """Inicializa el servicio obteniendo el Registry Singleton."""
        self._registry = CultivoServiceRegistry.get_instance()

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """
        Muestra los datos completos del registro (US-003, US-023).
        Usa el Registry para mostrar datos especificos de cultivos.
        """
        tierra = registro.get_tierra()
        plantacion = registro.get_plantacion()
        cultivos = plantacion.get_cultivos()

        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      ${registro.get_avaluo():,.2f}")
        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie:  {tierra.get_superficie()} m²")
        print(f"Superficie Ocupada: {plantacion.get_superficie_ocupada()} m²")
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")

        if cultivos:
            print("Listado de Cultivos plantados")
            print("____________________________")
            for cultivo in cultivos:
                # Dispatch polimorfico (US-009, US-TECH-005)
                self._registry.mostrar_datos(cultivo)
                print("---")  # Separador

    @staticmethod
    def _get_ruta_archivo(propietario: str) -> str:
        """Metodo helper para obtener la ruta completa del archivo."""
        directorio = constantes.DIRECTORIO_DATA
        nombre_archivo = f"{propietario}{constantes.EXTENSION_DATA}"
        return os.path.join(directorio, nombre_archivo)

    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Guarda el objeto RegistroForestal en disco usando Pickle (US-021).

        Args:
            registro: El objeto a serializar.

        Raises:
            PersistenciaException: Si ocurre un error de I/O.
        """
        propietario = registro.get_propietario()
        ruta_archivo = self._get_ruta_archivo(propietario)
        directorio = constantes.DIRECTORIO_DATA

        # Asegurar que el directorio 'data/' exista (US-021)
        os.makedirs(directorio, exist_ok=True)

        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"\n[PERSISTENCIA] Registro de {propietario} "
                  f"persistido exitosamente en {ruta_archivo}")
        except (IOError, pickle.PicklingError) as e:
            raise PersistenciaException(
                nombre_archivo=ruta_archivo,
                tipo_operacion=TipoOperacionPersistencia.ESCRITURA,
                causa_original=e
            )

    @staticmethod
    def leer_registro(propietario: str) -> Optional['RegistroForestal']:
        """
        Recupera un RegistroForestal desde disco (US-022).

        Args:
            propietario: Nombre del propietario (usado para el nombre de archivo).

        Returns:
            El objeto RegistroForestal deserializado.

        Raises:
            ValueError: Si el propietario es nulo o vacio.
            PersistenciaException: Si el archivo no existe o esta corrupto.
        """
        # Validacion de entrada (US-022)
        if not propietario:
            raise ValueError(TECH_PROPIETARIO_NULO)

        ruta_archivo = RegistroForestalService._get_ruta_archivo(propietario)
        registro: Optional['RegistroForestal'] = None

        try:
            with open(ruta_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(f"\n[PERSISTENCIA] Registro de {propietario} "
                  f"recuperado exitosamente desde {ruta_archivo}")
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException(
                nombre_archivo=ruta_archivo,
                tipo_operacion=TipoOperacionPersistencia.LECTURA,
                user_message=USER_ARCHIVO_NO_ENCONTRADO,
                technical_message=TECH_ARCHIVO_NO_ENCONTRADO,
                causa_original=e
            )
        except (EOFError, pickle.UnpicklingError, AttributeError) as e:
            raise PersistenciaException(
                nombre_archivo=ruta_archivo,
                tipo_operacion=TipoOperacionPersistencia.LECTURA,
                user_message=USER_ARCHIVO_CORRUPTO,
                technical_message=TECH_ARCHIVO_CORRUPTO,
                causa_original=e
            )
        except IOError as e:
            raise PersistenciaException(
                nombre_archivo=ruta_archivo,
                tipo_operacion=TipoOperacionPersistencia.LECTURA,
                causa_original=e
            )

# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

"""Servicio para la entidad Tierra."""

# Standard library
from typing import TYPE_CHECKING

# Local application
# Entidades
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra

if TYPE_CHECKING:
    pass


class TierraService:
    """Servicio con logica de negocio para Tierra."""

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una Tierra y una Plantacion asociada (US-001, US-002).

        Args:
            id_padron_catastral: ID de la tierra.
            superficie: Superficie en m².
            domicilio: Ubicacion.
            nombre_plantacion: Nombre de la finca a crear.

        Returns:
            La entidad Tierra creada y vinculada.
        """
        # 1. Crear Tierra
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # 2. Crear Plantacion
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_maxima=tierra.get_superficie()
        )

        # 3. Vincularlas
        tierra.set_finca(plantacion)

        return tierra


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-10-22 01:20:00
################################################################################
