# calculadora.py

import math

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

def guardar_en_historial(operacion, resultado):
    """Guardar la operacion el el archivo historial.txt"""
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{operacion} = {resultado}\n")

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
                print("\n=== HISTORIAL DE CALCULOS ===")
                print(contenido)
                print("=" * 35)
            else:
                print("\n El historial está vacío")
    except FileNotFoundError:
        print("\n El historial está vacío (archivo no existe)")

def borrar_historial():
    """Borra todo el historial"""
    confirmacion = input("\n ¿Seguro que desea borrar todo el historial? (s/n): ")
    if confirmacion.lower() == 's':
        with open("historial.txt", "w", encoding="utf-8") as archivo:
            archivo.write("")
        print("Hisorial borrado correctamente")
    else:
        print("X Operación cancelada")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("\n Elige una opción (1-10): ")

        if opcion == "1":   #Sumar
            print("\n--- SUMA ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = sumar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "2":     #Restar
            print("\n--- RESTA ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = restar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "3":     #Multiplicar
            print("\n--- MULTIPLICACIÓN ---")
            a = obtener_numero("Ingrese el primer valor: ")
            b = obtener_numero("Ingrese el segundo valor: ")
            resultado, operacion = multiplicar(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "4":     #Dividr
            print("\n--- DIVISION ---")
            a = obtener_numero("Dividendo: ")
            b = obtener_numero("Divisor: ")
            try:
                resultado, operacion = dividir(a, b)
                print(f"\n Resultado: {operacion} =  {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "5":     #Potencia
            print("\n--- POTENCIA ---")
            a = obtener_numero("Base: ")
            b = obtener_numero("Exponente: ")
            resultado, operacion = potencia(a, b)
            print(f"\n Resultado: {operacion} = {resultado}")
            guardar_en_historial(operacion, resultado)

        elif opcion == "6":     #Raíz Cuadrada
            print("\n--- RAÍZ CUADRADA ---")
            a = obtener_numero("Número: ")
            try:
                resultado, operacion = raiz_cuadrada(a)
                print(f"\n Resultado: {operacion} = {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "7":     #Porcentaje
            print("\n--- PORCENTAJE ---")
            a = obtener_numero("Parte: ")
            b = obtener_numero("Total: ")
            try:
                resultado, operacion = porcentaje(a, b)
                print(f"\n Resultado: El {operacion} = {resultado}")
                guardar_en_historial(operacion, resultado)
            except ValueError as e:
                print(f"\n{e}")

        elif opcion == "8":     #Ver historial
            ver_historial()

        elif opcion == "9":     #Borrar historial
            borrar_historial()

        elif opcion == "10":    #Salir
            print("\n ¡Gracias por usar la calculadora!")
            break

        else:
            print("\n X Opción Inválida. Elige un número del 1 a 7")

        #Pausa antes de continuar
        input("\n Presiona Enter para continuar...")

#Punto de entrada del programa
if __name__ == "__main__":
    main()