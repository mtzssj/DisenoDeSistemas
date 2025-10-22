"""
Modulo de Excepcion Base.

Define la excepcion base personalizada para el sistema (Rubrica 2.3).
"""

class ForestacionException(Exception):
    """Excepcion base para todos los errores de dominio del sistema."""

    def __init__(self, user_message: str, technical_message: str):
        """
        Inicializa la excepcion base.

        Args:
            user_message: Mensaje claro para el usuario final.
            technical_message: Mensaje tecnico para desarrolladores/logs.
        """
        super().__init__(technical_message)
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        """
        Obtiene el mensaje orientado al usuario.

        Returns:
            Mensaje de error para el usuario.
        """
        return self._user_message

    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje orientado al tecnico.

        Returns:
            Mensaje de error tecnico.
        """
        return self._technical_message

    def get_full_message(self) -> str:
        """
        Obtiene un mensaje combinado para logs.

        Returns:
            Mensaje combinado (Usuario + Tecnico).
        """
        return f"[USUARIO] {self._user_message} [TECNICO] {self._technical_message}"