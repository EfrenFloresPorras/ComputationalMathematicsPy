def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def main():
    try:
        a = int(input("Introduce el valor de a: "))
        b = int(input("Introduce el valor de b: "))
        
        if a < 0 or b < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        gcd, x, y = extended_gcd(a, b)
        print(f"El máximo común divisor de {a} y {b} es {gcd}")
        print(f"Coeficientes de Bézout: x = {x}, y = {y}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()
