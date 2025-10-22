"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================

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

