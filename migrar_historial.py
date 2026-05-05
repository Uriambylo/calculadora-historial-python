# migrar_historial.py

import datetime
from pathlib import Path

def migrar_historial():
    """Convierte el historial antiguo al nuevo formato con timestamps"""
    
    archivo_antiguo = Path("historial.txt")
    archivo_backup = Path("historial_backup.txt")
    
    if not archivo_antiguo.exists():
        print("No hay historial antiguo para migrar")
        return
    
    # Crear backup
    import shutil
    shutil.copy(archivo_antiguo, archivo_backup)
    print(f"✅ Backup creado: {archivo_backup}")
    
    # Leer operaciones antiguas
    with open(archivo_antiguo, "r", encoding="utf-8") as f:
        lineas_antiguas = f.readlines()
    
    # Extraer solo las operaciones (líneas que contienen "=")
    operaciones = []
    for linea in lineas_antiguas:
        linea = linea.strip()
        if linea and "=" in linea and not linea.startswith("=") and not linea.startswith("REGISTRO"):
            operaciones.append(linea)
    
    if not operaciones:
        print("No se encontraron operaciones para migrar")
        return
    
    # Crear nuevo archivo con formato
    timestamp_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(archivo_antiguo, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("REGISTRO DE OPERACIONES - CALCULADORA\n")
        f.write(f"Inicializado: {timestamp_actual}\n")
        f.write("="*80 + "\n\n")
        f.write(f"{'FECHA Y HORA':<25} {'OPERACIÓN':<35} {'RESULTADO':<20}\n")
        f.write("-"*80 + "\n")
        
        # Asignar timestamp a operaciones antiguas
        for op in operaciones:
            # Intentar extraer resultado
            if "=" in op:
                partes = op.split("=")
                operacion = partes[0].strip()
                resultado = partes[1].strip()
            else:
                operacion = op
                resultado = "?"
            
            f.write(f"{timestamp_actual:<25} {operacion:<35} {resultado:<20}\n")
    
    print(f"✅ Migración completada")
    print(f"📊 {len(operaciones)} operaciones migradas con timestamp actual")
    print(f"💡 Puedes editar manualmente las fechas en {archivo_antiguo} si es necesario")

if __name__ == "__main__":
    print("=== MIGRADOR DE HISTORIAL ===\n")
    respuesta = input("¿Migrar historial al nuevo formato con timestamp? (s/n): ")
    if respuesta.lower() == 's':
        migrar_historial()
    else:
        print("Migración cancelada")