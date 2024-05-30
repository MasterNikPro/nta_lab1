import math
import random


def p_pollard(n):  # основний алгоритм для р-метода Полларда

    # якщо число n парне, повертаємо 2
    if n % 2 == 0:
        return 2

    # вибираємо початкові значення x і y та константу c
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    def f(x):  # функція f(x) = (x^2 + c) mod n
        return (x * x + c) % n

    while d == 1:  # повторюємо поки не знайдемо дільник або не досягнемо умови зупинки
        # створюємо нові значення x і y
        x = f(x)
        y = f(f(y))

        # обчислюємо нсд (x-y) і n
        d = math.gcd(abs(x - y), n)

        # якщо x і y однакові, повторюємо з новими початковими значеннями
        if d == n:
            return p_pollard(n)

    return d  # повертаємо знайдений дільник


# приклад
n = 2500744714570633849
res = p_pollard(n)
print(f"Нетривіальний дільник числа {n} це {res}")
