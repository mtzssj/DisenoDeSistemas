"""Servicio de alto nivel para gestionar multiples fincas (US-018)."""

# Standard library
from typing import Dict, Generic, Optional, Type, TypeVar

# Local application
# Entidades
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import (
    RegistroForestal,
)
# Servicios
from python_forestacion.servicios.negocio.paquete import Paquete

# Tipo generico para cosecha (US-020)
T_Cultivo = TypeVar('T_Cultivo', bound=Cultivo)


class FincasService:
    """Servicio de negocio para operar sobre multiples fincas."""

    def __init__(self):
        """Inicializa el servicio con un diccionario de fincas."""
        self._fincas: Dict[int, RegistroForestal] = {}

    def add_finca(self, registro: RegistroForestal) -> None:
        """Agrega una finca (RegistroForestal) al servicio (US-018)."""
        id_padron = registro.get_id_padron()
        if id_padron not in self._fincas:
            self._fincas[id_padron] = registro
            print(f"[NEGOCIO] Finca con padron {id_padron} agregada.")
        else:
            print(f"[NEGOCIO] Finca con padron {id_padron} actualizada.")

    def buscar_finca(self, id_padron: int) -> Optional[RegistroForestal]:
        """Busca una finca por ID de padron (US-018)."""
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga una plantacion especifica (US-019)."""
        finca = self.buscar_finca(id_padron)
        if finca:
            print(f"\n[NEGOCIO] Fumigando plantacion "
                  f"'{finca.get_plantacion().get_nombre()}' "
                  f"con: {plaguicida}")
            # Logica de fumigacion (aqui solo imprimimos)
        else:
            print(f"[NEGOCIO] Error: Finca {id_padron} no encontrada.")

    def cosechar_y_empaquetar(
        self,
        tipo_cultivo: Type[T_Cultivo]
    ) -> Paquete[T_Cultivo]:
        """
        Cosecha todos los cultivos de un tipo especifico de
        TODAS las fincas gestionadas (US-020).

        Args:
            tipo_cultivo: La clase del cultivo a cosechar (ej. Lechuga).

        Returns:
            Un Paquete[T_Cultivo] tipo-seguro con los items cosechados.
        """
        print(f"\n[NEGOCIO] Iniciando cosecha de: {tipo_cultivo.__name__}...")
        paquete = Paquete(tipo_cultivo)
        cultivos_a_remover = []

        # 1. Buscar en todas las fincas
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            # Iteramos sobre una copia para poder modificar la lista original
            for cultivo in plantacion.get_cultivos():
                # 2. Cosechar por tipo (US-020)
                if isinstance(cultivo, tipo_cultivo):
                    # Aseguramos el tipo para el Paquete generico
                    cultivo_especifico = cultivo  # type: T_Cultivo
                    paquete.agregar_item(cultivo_especifico)
                    # Marcar para remover (no modificar lista mientras se itera)
                    cultivos_a_remover.append((plantacion, cultivo))

        # 3. Remover de las plantaciones
        for plantacion, cultivo in cultivos_a_remover:
            plantacion.remover_cultivo(cultivo)

        print(f"[NEGOCIO] COSECHANDO {paquete.get_cantidad()} unidades "
              f"de {tipo_cultivo.__name__}")

        return paquete