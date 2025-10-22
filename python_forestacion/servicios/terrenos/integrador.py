"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

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

