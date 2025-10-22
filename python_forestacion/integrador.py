"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion
Fecha: 2025-10-22 01:20:00
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\__init__.py
# ================================================================================

# Archivo __init__.py para el paquete principal python_forestacion
# Permite que Python trate este directorio como un paquete.

# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: C:\Users\Marcos\Desktop\Proyecto Parcial\python_forestacion\constantes.py
# ================================================================================

"""
Modulo de Constantes.

Centraliza todos los valores magicos y configuraciones del sistema
para cumplir con los principios de Codigo Limpio (Rubrica 3.4).
"""

# --- AGUA Y RIEGO (US-002, US-008, US-012) ---
AGUA_INICIAL_PLANTACION = 500  # Litros
AGUA_MINIMA_RIEGO = 10         # Litros consumidos por riego

# --- CULTIVOS (US-004 a US-007) ---
# Pino
SUPERFICIE_PINO = 2.0        # m²
AGUA_INICIAL_PINO = 2        # Litros
ALTURA_INICIAL_ARBOL = 1.0   # Metros (usado por Pino)
CRECIMIENTO_PINO = 0.10      # Metros por riego

# Olivo
SUPERFICIE_OLIVO = 3.0       # m²
AGUA_INICIAL_OLIVO = 5       # Litros
ALTURA_INICIAL_OLIVO = 0.5   # Metros (mas bajo que pino)
CRECIMIENTO_OLIVO = 0.01     # Metros por riego

# Lechuga
SUPERFICIE_LECHUGA = 0.10    # m²
AGUA_INICIAL_LECHUGA = 1     # Litros

# Zanahoria
SUPERFICIE_ZANAHORIA = 0.15  # m²
AGUA_INICIAL_ZANAHORIA = 0   # Litros

# --- ESTRATEGIAS DE ABSORCION (US-008, US-TECH-004) ---
# Seasonal (Arboles)
ABSORCION_SEASONAL_VERANO = 5    # Litros
ABSORCION_SEASONAL_INVIERNO = 2  # Litros
MES_INICIO_VERANO = 3            # Marzo
MES_FIN_VERANO = 8               # Agosto

# Constante (Hortalizas)
ABSORCION_CONSTANTE_LECHUGA = 1  # Litros
ABSORCION_CONSTANTE_ZANAHORIA = 2 # Litros

# --- SISTEMA DE RIEGO (US-010, US-011, US-012, US-013) ---
# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25               # °C
SENSOR_TEMP_MAX = 50                # °C

INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
SENSOR_HUMEDAD_MIN = 0              # %
SENSOR_HUMEDAD_MAX = 100            # %

# Control
INTERVALO_CONTROL_RIEGO = 2.5       # segundos
TEMP_MIN_RIEGO = 8                  # °C
TEMP_MAX_RIEGO = 15                 # °C
HUMEDAD_MAX_RIEGO = 50              # %

# Threading
THREAD_JOIN_TIMEOUT = 2.0           # segundos

# --- PERSISTENCIA (US-021) ---
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

