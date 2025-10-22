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