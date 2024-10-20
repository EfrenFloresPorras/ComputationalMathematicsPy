import math

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Función para calcular el símbolo de Legendre (a/p)
def legendre(a, p):
    if p <= 1 or not es_primo(p):
        raise ValueError("p debe ser un número primo mayor que 1")
    if a % p == 0:
        return 0
    if pow(a, (p - 1) // 2, p) == p - 1:
        return -1
    else:
        return 1

# Ejemplo de uso de las funciones
numero = 29
print(f"¿El número {numero} es primo? {'Sí' if es_primo(numero) else 'No'}")

a = 5
p = 11
print(f"El símbolo de Legendre ({a}/{p}) es {legendre(a, p)}")
