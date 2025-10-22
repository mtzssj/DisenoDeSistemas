"""
Modulo de Mensajes de Excepcion.

Centraliza los mensajes de error para el usuario y tecnico,
cumpliendo con la Rubrica 2.3.
"""

# --- Superficie ---
USER_SUPERFICIE_INSUFICIENTE = "Superficie insuficiente en la plantacion."
TECH_SUPERFICIE_INSUFICIENTE = "Se intento plantar mas alla de la capacidad."

# --- Agua ---
USER_AGUA_AGOTADA = "Agua agotada en la plantacion."
TECH_AGUA_AGOTADA = "Se intento regar sin suficiente agua disponible."

# --- Persistencia ---
USER_ERROR_PERSISTENCIA = "Ocurrio un error al guardar o leer el archivo."
TECH_ERROR_PERSISTENCIA = "Error de I/O (Pickle) al operar en archivo."
USER_ARCHIVO_NO_ENCONTRADO = "El archivo de registro no fue encontrado."
TECH_ARCHIVO_NO_ENCONTRADO = "FileNotFoundError durante la lectura."
USER_ARCHIVO_CORRUPTO = "El archivo de registro esta corrupto."
TECH_ARCHIVO_CORRUPTO = "EOFError o UnpicklingError durante la lectura."

# --- Validacion ---
USER_VALOR_INVALIDO = "El valor proporcionado es invalido."
TECH_SUPERFICIE_NEGATIVA = "La superficie debe ser mayor a cero."
TECH_AGUA_NEGATIVA = "El agua disponible no puede ser negativa."
TECH_PROPIETARIO_NULO = "El nombre del propietario no puede ser nulo o vacio."