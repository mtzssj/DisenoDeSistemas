"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: apto_medico.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\apto_medico.py
# ================================================================================

"""Entidad AptoMedico (US-015)."""

# Standard library
from datetime import date
from typing import Optional


class AptoMedico:
    """Entidad que certifica la aptitud medica de un trabajador."""

    def __init__(
        self,
        esta_apto: bool,
        fecha_emision: date,
        observaciones: Optional[str] = None
    ):
        """
        Inicializa el Apto Medico.

        Args:
            esta_apto: True si esta apto, False si no.
            fecha_emision: Fecha de emision del certificado.
            observaciones: Observaciones medicas (opcional).
        """
        self._esta_apto = esta_apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._esta_apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> Optional[str]:
        return self._observaciones

# ================================================================================
# ARCHIVO 3/6: estado_tarea.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\estado_tarea.py
# ================================================================================

"""Define el Enum para el estado de una Tarea (US-014)."""

# Standard library
from enum import Enum, auto


class EstadoTarea(Enum):
    """Estado de ejecucion de una tarea."""
    PENDIENTE = auto()
    COMPLETADA = auto()

# ================================================================================
# ARCHIVO 4/6: herramienta.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\herramienta.py
# ================================================================================

"""Entidad Herramienta (US-016)."""

class Herramienta:
    """Entidad Herramienta utilizada por un trabajador."""

    def __init__(
        self,
        id_herramienta: int,
        nombre: str,
        certificado_hys: bool
    ):
        """
        Inicializa la Herramienta.

        Args:
            id_herramienta: ID unico de la herramienta.
            nombre: Nombre (ej. Pala).
            certificado_hys: Si posee certificacion de Higiene y Seguridad.
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_nombre(self) -> str:
        return self._nombre

# ================================================================================
# ARCHIVO 5/6: tarea.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\tarea.py
# ================================================================================

"""Entidad Tarea (US-014)."""

# Standard library
from datetime import date

# Local application
from python_forestacion.entidades.personal.estado_tarea import EstadoTarea


class Tarea:
    """Entidad Tarea asignada a un trabajador."""

    def __init__(
        self,
        id_tarea: int,
        fecha_programada: date,
        descripcion: str
    ):
        """
        Inicializa la Tarea.

        Args:
            id_tarea: ID unico de la tarea.
            fecha_programada: Fecha de ejecucion.
            descripcion: Descripcion.
        """
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._estado: EstadoTarea = EstadoTarea.PENDIENTE

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> EstadoTarea:
        return self._estado

    def completar_tarea(self) -> None:
        """Marca la tarea como completada."""
        self._estado = EstadoTarea.COMPLETADA

# ================================================================================
# ARCHIVO 6/6: trabajador.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\entidades\personal\trabajador.py
# ================================================================================

"""Entidad Trabajador (US-014)."""

# Standard library
from typing import List, Optional

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea


class Trabajador:
    """Entidad Trabajador agricola."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        """
        Inicializa el Trabajador.

        Args:
            dni: DNI unico.
            nombre: Nombre completo.
            tareas: Lista de tareas asignadas.
        """
        self._dni = dni
        self._nombre = nombre
        # Defensive copy (Rubrica 5.2)
        self._tareas: List[Tarea] = tareas.copy()
        self._apto_medico: Optional[AptoMedico] = None  # Sin apto inicial

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        """Retorna copia de la lista de tareas (US-014)."""
        return self._tareas.copy()

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico) -> None:
        """Asigna o actualiza el apto medico."""
        self._apto_medico = apto

