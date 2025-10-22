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