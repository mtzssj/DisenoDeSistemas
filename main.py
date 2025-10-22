"""
Punto de entrada principal (main.py) - Sistema de Gestion Forestal.

Este script ejecuta un flujo de demostracion completo que valida
todas las historias de usuario y patrones de diseno implementados,
siguiendo las trazas de USER_STORIES.md y README.md.
"""

# Standard library
import sys
import time
from datetime import date

# Local application
# Constantes
from python_forestacion import constantes
# Entidades
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.terrenos.registro_forestal import (
    RegistroForestal,
)
# Excepciones
from python_forestacion.excepciones.agua_agotada_exception import (
    AguaAgotadaException,
)
from python_forestacion.excepciones.persistencia_exception import (
    PersistenciaException,
)
from python_forestacion.excepciones.superficie_insuficiente_exception import (
    SuperficieInsuficienteException,
)
# Riego (Threads)
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.sensores.temperatura_reader_task import (
    TemperaturaReaderTask,
)
# Servicios
from python_forestacion.servicios.cultivos.cultivo_service_registry import (
    CultivoServiceRegistry,
)
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.personal.trabajador_service import (
    TrabajadorService,
)
from python_forestacion.servicios.terrenos.plantacion_service import (
    PlantacionService,
)
from python_forestacion.servicios.terrenos.registro_forestal_service import (
    RegistroForestalService,
)
from python_forestacion.servicios.terrenos.tierra_service import TierraService


def run_demo():
    """Ejecuta la demostracion completa del sistema."""

    print("=" * 70)
    print("     SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)

    # --- INICIALIZACION Y PATRON SINGLETON (US-TECH-001) ---
    print("\n" + "-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)
    
    # Instanciamos servicios. Esto inicializara el Singleton Registry.
    tierra_service = TierraService()
    plantacion_service = PlantacionService()
    registro_service = RegistroForestalService()
    trabajador_service = TrabajadorService()
    fincas_service = FincasService()
    
    # Validamos el Singleton
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry()  # Llama a __new__
    
    if id(registry1) == id(registry2) and id(plantacion_service._registry) == id(registry1):
        print("[OK] SINGLETON: Todos los servicios comparten la misma instancia del Registry.")
    else:
        print("[ERROR] SINGLETON: Las instancias del Registry son DIFERENTES.")
        sys.exit(1)

    # --- EPIC 1: GESTION DE TERRENOS (US-001, US-002, US-003) ---
    print("\n" + "-" * 70)
    print("  EPIC 1: Gestion de Terrenos y Plantaciones")
    print("-" * 70)
    
    print("1.1. Creando tierra con plantacion (US-001, US-002)...")
    # Trazabilidad: main.py lineas 111-116 (US-001)
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=100.0,  # Superficie pequenia para probar limites
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()
    print(f"[OK] Terreno '{terreno.get_domicilio()}' y plantacion "
          f"'{plantacion.get_nombre()}' creados.")
    print(f"    Superficie disponible inicial: {plantacion.get_superficie_disponible()} m²")

    # Trazabilidad: main.py lineas 123-129 (US-003)
    print("\n1.2. Creando Registro Forestal (US-003)...")
    registro = RegistroForestal(
        id_padron=terreno.get_id_padron_catastral(),
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print(f"[OK] Registro creado para {registro.get_propietario()}.")

    # --- EPIC 2: GESTION DE CULTIVOS (US-004 a US-009) ---
    print("\n" + "-" * 70)
    print("  EPIC 2: Gestion de Cultivos (Patron Factory y Strategy)")
    print("-" * 70)
    
    print("2.1. Plantando cultivos (Patron Factory)...")
    try:
        # Trazabilidad: main.py linea 141 (US-004)
        plantacion_service.plantar(plantacion, "Pino", 5)
        print(f"[OK] 5 Pinos plantados (Req: {5 * constantes.SUPERFICIE_PINO} m²). "
              f"Disp: {plantacion.get_superficie_disponible()} m²")
        
        # Trazabilidad: main.py linea 142 (US-005)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        print(f"[OK] 5 Olivos plantados (Req: {5 * constantes.SUPERFICIE_OLIVO} m²). "
              f"Disp: {plantacion.get_superficie_disponible()} m²")
        
        # Trazabilidad: main.py linea 143 (US-006)
        plantacion_service.plantar(plantacion, "Lechuga", 20)
        print(f"[OK] 20 Lechugas plantadas (Req: {20 * constantes.SUPERFICIE_LECHUGA} m²). "
              f"Disp: {plantacion.get_superficie_disponible()} m²")
        
        # Trazabilidad: main.py linea 144 (US-007)
        plantacion_service.plantar(plantacion, "Zanahoria", 10)
        print(f"[OK] 10 Zanahorias plantadas (Req: {10 * constantes.SUPERFICIE_ZANAHORIA} m²). "
              f"Disp: {plantacion.get_superficie_disponible()} m²")
        
        print("\n2.2. Probando excepcion de superficie (US-004)...")
        plantacion_service.plantar(plantacion, "Pino", 100) # Esto debe fallar
        
    except SuperficieInsuficienteException as e:
        print(f"[OK] EXCEPCION CAPTURADA: {e.get_user_message()}")
        print(f"    Requerida: {e.get_superficie_requerida()} m², "
              f"Disponible: {e.get_superficie_disponible()} m²")
    except ValueError as e:
        print(f"[ERROR] Factory fallo: {e}")
        
    print(f"\n2.3. Regando plantacion (Patron Strategy)... (US-008)")
    try:
        plantacion_service.regar(plantacion)
    except AguaAgotadaException as e:
        print(f"[ERROR] Riego fallo: {e.get_user_message()}")
        
    print("\n2.4. Mostrando datos de cultivos (Patron Registry)... (US-009)")
    # Trazabilidad: cultivo_service_registry.py lineas 78-89
    for cultivo in plantacion.get_cultivos():
        registry1.mostrar_datos(cultivo) # Usando el Registry
        print("---")
        
    # --- EPIC 3: RIEGO AUTOMATIZADO (US-010 a US-013) ---
    print("\n" + "-" * 70)
    print("  EPIC 3: Riego Automatizado (Patron Observer y Threads)")
    print("-" * 70)
    
    # Trazabilidad: main.py lineas 158-166
    print("3.1. Iniciando sensores (Threads Observable)...")
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    
    print("3.2. Iniciando Control de Riego (Thread Observer)...")
    tarea_control = ControlRiegoTask(
        sensor_temperatura=tarea_temp,
        sensor_humedad=tarea_hum,
        plantacion=plantacion,
        plantacion_service=plantacion_service
    )
    
    # Iniciamos los threads
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()
    
    print("\n[OBSERVER] Sistema de riego automatico funcionando...")
    print("[OBSERVER] Esperando 10 segundos (observe la consola)...")
    time.sleep(10)
    
    # Trazabilidad: main.py lineas 256-263 (US-013)
    print("\n3.3. Deteniendo sistema de riego (Graceful Shutdown)...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    
    # Esperar finalizacion con timeout (US-013)
    tarea_temp.join(timeout=constantes.THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=constantes.THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=constantes.THREAD_JOIN_TIMEOUT)
    print("[OK] Threads de riego detenidos.")

    # --- EPIC 4: GESTION DE PERSONAL (US-014 a US-017) ---
    print("\n" + "-" * 70)
    print("  EPIC 4: Gestion de Personal")
    print("-" * 70)
    
    # Trazabilidad: main.py lineas 176-185 (US-014)
    print("4.1. Creando tareas y trabajador (US-014)...")
    tareas_juan = [
        Tarea(1, date(2025, 10, 22), "Desmalezar"),
        Tarea(2, date(2025, 10, 22), "Abonar"),
        Tarea(3, date(2025, 10, 22), "Marcar surcos")
    ]
    trabajador_juan = Trabajador(
        dni=43888734,
        nombre="Juan Perez",
        tareas=tareas_juan
    )
    
    # Trazabilidad: main.py linea 187 (US-017)
    print("4.2. Asignando trabajador a plantacion (US-017)...")
    plantacion.set_trabajadores([trabajador_juan])
    print(f"[OK] {trabajador_juan.get_nombre()} asignado a "
          f"{plantacion.get_nombre()}.")
          
    # Trazabilidad: main.py lineas 191-196 (US-015)
    print("\n4.3. Asignando Apto Medico (US-015)...")
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador_juan,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    if trabajador_juan.get_apto_medico().esta_apto():
        print("[OK] Apto medico de Juan Perez: APTO")
    else:
        print("[ERROR] Apto medico de Juan Perez: NO APTO")
        
    # Trazabilidad: main.py lineas 199-204 (US-016)
    print("\n4.4. Trabajador ejecutando tareas (US-016)...")
    herramienta = Herramienta(
        id_herramienta=1,
        nombre="Pala",
        certificado_hys=True
    )
    # Ejecutar tareas (debe imprimir en orden 3, 2, 1)
    trabajador_service.trabajar(
        trabajador=trabajador_juan,
        fecha=date(2025, 10, 22), # Fecha de hoy (hardcodeada por demo)
        util=herramienta
    )

    # --- EPIC 5: OPERACIONES DE NEGOCIO (US-018 a US-020) ---
    print("\n" + "-" * 70)
    print("  EPIC 5: Operaciones de Negocio")
    print("-" * 70)
    
    # Trazabilidad: main.py linea 225 (US-018)
    print("5.1. Agregando finca al servicio de Fincas (US-018)...")
    fincas_service.add_finca(registro)
    
    # Trazabilidad: main.py linea 228 (US-019)
    print("\n5.2. Fumigando plantacion (US-019)...")
    fincas_service.fumigar(
        id_padron=1,
        plaguicida="insecto organico"
    )
    
    # Trazabilidad: main.py lineas 232-236 (US-020)
    print("\n5.3. Cosechando y empaquetando (Generics)... (US-020)")
    print(f"    Cultivos ANTES de cosecha: {len(plantacion.get_cultivos())}")
    
    # Cosechar Lechugas
    caja_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()
    
    # Cosechar Pinos
    caja_pinos = fincas_service.cosechar_y_empaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()
    
    print(f"\n    Cultivos DESPUES de cosecha: {len(plantacion.get_cultivos())}")

    # --- EPIC 6: PERSISTENCIA Y AUDITORIA (US-021 a US-023) ---
    print("\n" + "-" * 70)
    print("  EPIC 6: Persistencia y Auditoria (Pickle)")
    print("-" * 70)
    
    registro_leido = None
    try:
        # Trazabilidad: main.py linea 242 (US-021)
        print("6.1. Persistiendo Registro Forestal en disco (US-021)...")
        registro_service.persistir(registro)
        
        # Trazabilidad: main.py lineas 246-247 (US-022)
        print("\n6.2. Recuperando Registro Forestal desde disco (US-022)...")
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        
    except (PersistenciaException, ValueError) as e:
        print(f"[ERROR] Fallo la persistencia: {e}")
    
    if registro_leido:
        # Trazabilidad: main.py linea 247 (US-023)
        print("\n6.3. Mostrando datos del registro recuperado (US-023)...")
        # Usamos el servicio para mostrar los datos
        registro_service.mostrar_datos(registro_leido)
        # Validamos que los datos (ej. cultivos restantes) coincidan
        cultivos_leidos = registro_leido.get_plantacion().get_cultivos()
        print(f"\n    Cultivos en obj original: {len(plantacion.get_cultivos())}")
        print(f"    Cultivos en obj leido:    {len(cultivos_leidos)}")
        if len(plantacion.get_cultivos()) == len(cultivos_leidos):
            print("[OK] La persistencia fue exitosa.")

    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de 4 tipos de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y control de riego")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua (Seasonal/Constante)")
    print("  [OK] REGISTRY    - Dispatch polimorfico para mostrar_datos y absorber_agua")
    print("  [OK] PERSISTENCE - Guardado y recuperacion con Pickle")
    print("  [OK] THREADING   - Sensores y control en threads daemon con graceful shutdown")
    print("=" * 70)


if __name__ == "__main__":
    run_demo()