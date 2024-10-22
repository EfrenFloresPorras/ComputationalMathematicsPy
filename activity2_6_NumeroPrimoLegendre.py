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
    if a % p == 0:
        return 0
    if pow(a, (p - 1) // 2, p) == p - 1:
        return -1
    else:
        return 1

# Function that calculates the quantity of prime numbers that are less than a given number
# without the use of negative Legendre's symbol
# Using Legendre's theorem
def cantidad_primos_menores_que(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    cantidad = 2
    for i in range(5, n + 1, 2):
        if es_primo(i):
            cantidad += 1
    return cantidad

# Example of use of the function
# Ejemplo de uso de las funciones
n = 214
numero = 214
print(f"¿El número {numero} es primo? {'Sí' if es_primo(numero) else 'No'}")
print(f"La cantidad de números primos menores que {n} es {cantidad_primos_menores_que(n)}")

a = 5
p = 11
print(f"El símbolo de Legendre ({a}/{p}) es {legendre(a, p)}")