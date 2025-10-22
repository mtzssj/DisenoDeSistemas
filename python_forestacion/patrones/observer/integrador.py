"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: evento_sensor.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\evento_sensor.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: observable.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: observer.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\observer.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: tipo_evento_sensor.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\observer\tipo_evento_sensor.py
# ================================================================================

"""Define el Enum para los tipos de eventos de sensor."""

# Standard library
from enum import Enum, auto


class TipoEventoSensor(Enum):
    """Tipos de eventos de sensor para el patron Observer."""
    TEMPERATURA = auto()
    HUMEDAD = auto()

