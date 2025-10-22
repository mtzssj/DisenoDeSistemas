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