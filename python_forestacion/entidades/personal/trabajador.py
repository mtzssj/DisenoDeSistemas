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