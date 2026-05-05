# calculadora.py

import math
import datetime
from pathlib import Path

def mostrar_menu():
    """Muestra el menú principal de la calculadora"""
    print("\n=== CALCULADORA CON HISTORIAL === ")
    print("1. Sumar (+) ")
    print("2. Restar (-) ")
    print("3. Multiplicar (*) ")
    print("4. Dividir (/) ")
    print("5. Potencia (^) ")
    print("6. Raíz Cuadrada (√) ")
    print("7. Porcentaje (%) ")
    print("8. Ver historial")
    print("9. Borrar historial")
    print("10. Salir")
    print("=" * 35)

def obtener_numero(mensaje):
    """Soicita un numero al usuario manejando errores"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("X Error: Debe ingresar un número válido")

def obtener_timestamp():
    """Obtiene la fecha y hora actual en formato legible"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def inicializar_archivo_historial():
    """Crea el archivo historial.txt con encabezados si no existe"""
    archivo = Path("historial.txt")
    if not archivo.exists():
        with open("historial.txt", "w", encoding="utf-8") as f:
            f.write("="*80 + "\n")
            f.write("REGISTRO DE OPERACIONES - CALCULADORA\n")
            f.write(f"Inizializado: {obtener_timestamp()}\n")
            f.write("="*80 + "\n\n")
            f.write(f"{'FECHA Y HORA':<25} {'OPERACIÓN':<35} {'RESULTADO':<20}\n")
            f.write("-"*80 + "\n")

def guardar_en_historial(operacion, resultado):
    """Guarda la operacion en el archivo historial.txt con timestamp"""
    # Asefura que el archivo existe con el formato correcto
    inicializar_archivo_historial()

    timestamp = obtener_timestamp()
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{timestamp:<25} {operacion:<35} {resultado:<20}\n")

def sumar(a,b):
    """Realiza una suma"""
    resultado = a + b
    operacion = f"{a} + {b}"
    return resultado, operacion

def restar(a, b):
    """Realiza una resta"""
    resultado = a - b
    operacion = f"{a} - {b}"
    return resultado, operacion

def multiplicar(a, b):
    """Realiza una multiplicación"""
    resultado = a * b
    operacion = f"{a} * {b}"
    return resultado, operacion

def dividir(a, b):
    """Realiza una división con validación"""
    if b == 0:
        raise ValueError("X Error: No se puede dividir entre cero")
    resultado = a / b
    operacion = f"{a} / {b}"
    return resultado, operacion

def potencia(a, b):
    """Calcula a elevado a b"""
    resultado = a ** b
    operacion = f"{a} ^ {b}"
    return resultado, operacion

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada de a"""
    if a < 0:
        raise ValueError("X Error: No se puede calcular la raíz cuadrada de un número negativo")
    resultado = math.sqrt(a)
    operacion = f"√{a}"
    return resultado, operacion

def porcentaje(a, b):
    """Calcula el porcentaje de a respecto a b"""
    if b == 0:
        raise ValueError("X Error: No se puede calcular el porcentaje respecto a cero")
    resultado = (a / 100) * b
    operacion = f"{a} % de {b}"
    return resultado, operacion

def ver_historial():
    """Muestra todo el historial guardado"""
    try:
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print("\n=== HISTORIAL DE CÁLCULOS ===")
                print(contenido)
            else:
                print("\n El historial está vacío")
    except FileNotFoundError:
        print("\n El historial está vacío (archivo no existe)")

def ver_historial_resumido():
    """Muestra solo las operaciones (sin encabezados) para compatibilidad """
    try:
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            # Filtrar líneas que no son operaciones (no comienzan con fecha)
            operaciones = [l for l in lineas if l[0].isdigit() if len(l) > 0]
            if operaciones:
                print("\n=== HISTORIAL DE CÁLCULOS ===")
                for op in operaciones:
                    print(op.strip())
            else:
                print("\n El historial no tiene operaciones registradas")
    except FileNotFoundError:
            print("\n El historial está vacío (archivo no existe)")

def borrar_historial():
    """Borra todo el historial y reiniciar formato"""
    confirmacion = input("\n ¿Seguro que desea borrar todo el historial? (s/n): ")
    if confirmacion.lower() == 's':
        # Reniciar el archivo con el formato correcto
        with open("historial.txt", "w", encoding="utf-8") as archivo:
            archivo.write("="*80 + "\n")
            archivo.write("REGISTRO DE OPERACIONES - CALCULADORA\n")
            archivo.write(f"Inizializado: {obtener_timestamp()}\n")
            archivo.write("="*80 + "\n\n")
            archivo.write(f"{'FECHA Y HORA':<25} {'OPERACIÓN':<35} {'RESULTADO':<20}\n")
            archivo.write("-"*80 + "\n")
        print("Hisorial borrado correctamente")
    else:
        print("Operación cancelada")

def buscar_por_fecha():
    """Busca operaciones por fecha específica"""
    fecha = input("\n Ingrese la fecha a buscar (YYYY-MM-DD): ")
    try:
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            resultados = []
            for linea in lineas:
                if linea.startswith(fecha):
                    resultados.append(linea.strip())

                
            if resultados:
                print(f"\n=== OPERACIONES DEL {fecha} ===")
                for r in resultados:
                    print(r)
                print(f"\n Total de operaciones encontradas: {len(resultados)}")
            else:
                print(f"\n No se encontraron operaciones para la fecha {fecha}")
    except FileNotFoundError:
        print("\n El historial está vacío (archivo no existe)")

def mostrar_estadisticas():
    """Muestra estadísticas básicas del historial"""
    try:
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            # Filtrar solo las líneas que representan operaciones (comienzan con fecha)
            operaciones = [l for l in lineas if l and l[0].isdigit()]

            if not operaciones:
                print("\n El historial no tiene operaciones registradas")
                return
            
            fechas_uncicas = set()
            operaciones_por_dia = {}

            for op in operaciones:
                fecha = op[:10]  # Extraer solo la parte de la fecha (YYYY-MM-DD)
                fechas_uncicas.add(fecha)
                operaciones_por_dia[fecha] = operaciones_por_dia.get(fecha, 0) + 1

            total_operaciones = len(operaciones)
            dia_uso = len(fechas_uncicas)
            promedio = total_operaciones / dia_uso if dia_uso > 0 else 0

            print("\n"+"="*50)
            print("ESTADÍSTICAS DE USO DE LA CALCULADORA")
            print("="*50)
            print(f"Total de operaciones registradas: {total_operaciones}")
            print(f"Días con operaciones registradas: {dia_uso}")
            print(f"Promedio de operaciones por día: {promedio:.1f}")
            print(f"Día más activo: {max(operaciones_por_dia, key=operaciones_por_dia.get)} con {max(operaciones_por_dia.values())} operaciones")
            print(f"Primera operación registrada: {min(fechas_uncicas) if fechas_uncicas else 'N/A'}")
            print(f"Última operación registrada: {max(fechas_uncicas) if fechas_uncicas else 'N/A'}")
            print("="*50)

    except FileNotFoundError:
        print("\n El historial está vacío (archivo no existe)")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("\n Elige una opción (1-10): ")

        if opcion == "1":   # Sumar
            print("\n--- SUMA ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = sumar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "2":     # Restar
            print("\n--- RESTA ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = restar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "3":     # Multiplicar
            print("\n--- MULTIPLICACIÓN ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = multiplicar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "4":     # Dividr
            print("\n--- DIVISION ---")
            a = obtener_numero("Dividendo: ")
            b = obtener_numero("Divisor: ")
            try:
                resultado, operacion = dividir(a, b)
                print(f"\n Resultado: {operacion} =  {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "5":     # Potencia
            print("\n--- POTENCIA ---")
            a = obtener_numero("Base: ")
            b = obtener_numero("Exponente: ")
            resultado, operacion = potencia(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "6":     # Raíz Cuadrada
            print("\n--- RAÍZ CUADRADA ---")
            a = obtener_numero("Número: ")
            try:
                resultado, operacion = raiz_cuadrada(a)
                print(f"\n Resultado: {operacion} = {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "7":     # Porcentaje
            print("\n--- PORCENTAJE ---")
            a = obtener_numero("Parte: ")
            b = obtener_numero("Total: ")
            try:
                resultado, operacion = porcentaje(a, b)
                print(f"\n Resultado: El {operacion} = {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "8":     # Ver historial
            print("\n ¿Cómo deseas ver el historial?")
            print("1. Ver historial completo (con formato)")
            print("2. Ver solo operaciones (resumido)")
            sub_opcion = input("\n Elige una opción (1-2): ")
            if sub_opcion == "2":
                ver_historial_resumido()
            else:
                ver_historial()

        elif opcion == "9":     # Borrar historial
            borrar_historial()

        elif opcion == "10":    # Salir
            print("\n ¡Gracias por usar la calculadora!")
            break

        else:
            print("\n X Opción Inválida. Elige un número del 1 a 7")

        # Pausa antes de continuar
        input("\n Presiona Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()