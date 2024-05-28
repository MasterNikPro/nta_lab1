import random
import math


def jacobi(a, n):  # допоміжна функція для обчислення символу Якобі
    if n <= 0 or n % 2 == 0:
        return 0  # символ Якобі визначений тільки для непарних n > 0

    result = 1

    if a < 0:
        a = -a
        if n % 4 == 3:
            result = -result  # якщо a від'ємне - змінюємо знак результату

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result  # змінюємо знак в залежності від n % 8
        a, n = n, a  # міняємо місцями a і n
        if a % 4 == 3 and n % 4 == 3:
            result = -result  # змінюємо знак в залежності від a % 4 і n % 4
        a %= n  # присвоюємо a залишок від ділення на n

    if n == 1:
        return result  # якщо n дорівнює 1, повертаємо результат
    else:
        return 0  # інакше повертаємо 0