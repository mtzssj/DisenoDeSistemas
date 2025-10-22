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