"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\humedad_reader_task.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\riego\sensores\temperatura_reader_task.py
# ================================================================================

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

