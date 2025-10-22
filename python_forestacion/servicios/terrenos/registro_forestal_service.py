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