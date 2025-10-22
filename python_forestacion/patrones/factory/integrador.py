"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\factory
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\patrones\factory\cultivo_factory.py
# ================================================================================

"""
Implementacion del Patron Factory Method (US-TECH-002).
Centraliza la creacion de cultivos, desacoplando al cliente.
"""

# Standard library
from typing import TYPE_CHECKING

# Evita importacion circular en type hints
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para crear instancias de Cultivo.
    Usa un diccionario de factories (Rubrica 1.2)
    en lugar de if/elif.
    """

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """Metodo de factory privado para Pino."""
        # Imports locales para evitar dependencia circular
        # y cargar solo cuando es necesario.
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")  # Variedad por defecto

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """Metodo de factory privado para Olivo."""
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)  # Default

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """Metodo de factory privado para Lechuga."""
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")  # Default

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """Metodo de factory privado para Zanahoria."""
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=False)  # Default

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Metodo Factory principal (publico).

        Args:
            especie: El nombre del tipo de cultivo a crear.

        Returns:
            Una instancia de un subtipo de Cultivo.

        Raises:
            ValueError: Si la especie es desconocida.
        """
        # Diccionario de factories (US-TECH-002)
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        # Dispatch
        factory_method = factories.get(especie)

        if not factory_method:
            raise ValueError(f"Especie desconocida: {especie}")

        # Retorna el tipo base (Cultivo) para desacoplar
        return factory_method()

