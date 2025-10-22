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