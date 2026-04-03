def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


historial = []

print("Calculadora básica")

while True:
    print("\n--- Nueva operación ---")

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar números válidos")
        continue

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("6. Ver historial")

    op = input("Opción: ")

    if op == "1":
        resultado = suma(a, b)
        print("Resultado:", resultado)

        operacion = f"{a} + {b} = {resultado}"
        historial.append(operacion)

        with open("historial.txt", "a") as f:
            f.write(operacion + "\n")



    elif op == "2":
        resultado = resta(a, b)
        print("Resultado:", resultado)
        
        operacion = f"{a} - {b} = {resultado}"
        historial.append(operacion)

        with open("historial.txt", "a") as f:
            f.write(operacion + "\n")

    elif op == "3":
        resultado = multiplicacion(a, b)
        print("Resultado:", resultado)

        operacion = f"{a} * {b} = {resultado}"
        historial.append(operacion)

        with open("historial.txt", "a") as f:
            f.write(operacion + "\n")

    elif op == "4":
        resultado = division(a, b)
        print("Resultado:", resultado)

        operacion = f"{a} / {b} = {resultado}"
        historial.append(operacion)

        with open("historial.txt", "a") as f:
            f.write(operacion + "\n")

    elif op == "5":
        print("Saliendo...")
        break

    elif op == "6":
        print("\n--- Historial ---")
        try:
            with open("historial.txt", "r") as f:
                contenido = f.read()
                if contenido == "":
                    print("No hay operaciones en el historial.")
                else:
                    print(contenido)
        except FileNotFoundError:
            print("No hay historial disponible.")

    else:
        print("Opción no válida")