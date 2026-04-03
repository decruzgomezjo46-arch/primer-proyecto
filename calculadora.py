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


print("Calculadora básica")

while True:
    print("\n--- A joder la calculadora ---")

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar números válidos chaval")
        continue

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    op = input("Opción: ")

    if op == "1":
        print("Resultado:", suma(a, b))
    elif op == "2":
        print("Resultado:", resta(a, b))
    elif op == "3":
        print("Resultado:", multiplicacion(a, b))
    elif op == "4":
        print("Resultado:", division(a, b))
    elif op == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")