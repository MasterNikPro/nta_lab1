import time
from division_method import division
from solovai_strassen import s_s
from ro_pollard import p_pollard
from brilhart_morrison import canonical_decomposition, is_prime
import sys
import os
def log_divisor(divisor, method):
    timestamp = time.time()-start_time
    print(f"Дільник: {divisor}, Знайдено методом: {method}, Час: {timestamp}")


def canonical_decomposition_algorithm(n):


    start_whole_time = time.time()
    # print(f"Початок роботи алгоритму: {start_time}")

    def decompose(n):
        global start_time
        result = []

        # Step 3a: Check if the number is prime
        start_time = time.time()
        if is_prime(n):
            log_divisor(n, "Перевірка простоти")
            result.append(n)
            return result

        # Step 3b: Trial division method up to 47
        start_time = time.time()
        divisor = division(n)
        if divisor:
            log_divisor(divisor, "діллень")
            # print(f'Перевірка простоти: {divisor}')
            if is_prime(divisor):
                result.append(divisor)
            else:
                result.extend(decompose(divisor))
            result.extend(decompose(n // divisor))
            return result

        # Step 3в: Pollard's rho method
        start_time = time.time()
        divisor = p_pollard(n)
        if divisor:
            log_divisor(divisor, "ρ-метод Полларда")
            if is_prime(divisor):
                result.append(divisor)
            else:
                result.extend(decompose(divisor))
            result.extend(decompose(n // divisor))
            return result

        # Step 3г: Check if the number is prime
        start_time = time.time()
        if is_prime(n):
            print(f'Перевірка простоти: {divisor}')
            # log_divisor(n, "Перевірка простоти")
            result.append(n)
            return result

        # Step 3д: Brilhart-Morrison method or other advanced method
        start_time = time.time()
        factor1, factor2 = canonical_decomposition(n, k=20)
        if factor1 and factor2:
            log_divisor(factor1, "Метод Брiлхарта-Моррiсона")
            log_divisor(factor2, "Метод Брiлхарта-Моррiсона")
            if is_prime(factor1):
                result.append(factor1)
            else:
                result.extend(decompose(factor1))
            if is_prime(factor2):
                result.append(factor2)
            else:
                result.extend(decompose(factor2))
            return result

        print("Я не можу знайти канонiчний розклад числа :(")
        return []

    result = decompose(n)


    print(f"Кінець роботи алгоритму: {time.time() - start_whole_time}")

    return result


if __name__ == "__main__":
    number = os.getenv('NUMBER', '0')
    n = int(number)
    result = canonical_decomposition_algorithm(n)
    print(f"Канонiчний розклад числа {n}: {result}")

