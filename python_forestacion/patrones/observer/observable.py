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