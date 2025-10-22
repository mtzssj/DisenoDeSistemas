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