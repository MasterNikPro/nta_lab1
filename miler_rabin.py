import random
import math

def solovay_strassen(p, k):
    def jacobi(a, n):
        if n <= 0 or n % 2 == 0:
            return 0
        result = 1
        if a < 0:
            a = -a
            if n % 4 == 3:
                result = -result
        while a != 0:
            while a % 2 == 0:
                a //= 2
                if n % 8 == 3 or n % 8 == 5:
                    result = -result
            a, n = n, a
            if a % 4 == 3 and n % 4 == 3:
                result = -result
            a %= n
        if n == 1:
            return result
        else:
            return 0


    def is_pseudo_prime(x, p):
        jacobi_symbol = jacobi(x, p)
        power_result = pow(x, (p - 1) // 2, p)
        return jacobi_symbol == power_result or jacobi_symbol == power_result - p


    counter = 0

    while counter < k:
        x = random.randint(2, p - 1)
        gcd = math.gcd(x, p)

        if gcd > 1:
            return False

        if not is_pseudo_prime(x, p):
            return False

        counter += 1

    return True

# Приклад використання
p = 101  # Тестове число
k = 5  # Кількість випадкових основ

if solovay_strassen(p, k):
    print(f"Число {p} є ймовірно простим.")
else:
    print(f"Число {p} є складеним.")


