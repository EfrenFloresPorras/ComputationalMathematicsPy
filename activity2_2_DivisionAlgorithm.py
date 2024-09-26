def algoritmo_division(a, b):
    if b == 0:
        return "Error: División por cero"
    
    # Inicialización
    r = abs(a)
    q = 0
    
    # Proceso de división
    while r >= abs(b):
        r -= abs(b)
        q += 1
    
    # Ajuste de signos
    if a > 0:
        quotient = q
        remainder = r
    elif r == 0:
        quotient = -q
        remainder = 0
    else:
        quotient = -q - 1
        remainder = abs(b) - r
    
    return quotient, remainder

# Solicitar entrada del usuario
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

# Ejecutar el algoritmo con los valores ingresados
resultado = algoritmo_division(a, b)
print(f"Cociente: {resultado[0]}, Resto: {resultado[1]}")
