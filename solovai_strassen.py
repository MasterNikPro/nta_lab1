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


def is_pseudo_prime(x, p):  # перевірка псевдопростоти по модулю
    jacobi_symbol = jacobi(x, p) % p  # обчислюємо символ Якобі і беремо залишок від ділення на p
    power_res = pow(x, (p - 1) // 2, p)  # обчислюємо x^(p-1)/2 mod p
    return jacobi_symbol == power_res or jacobi_symbol == power_res - p  # порівнюємо результати


def s_s(p, k):  # основна функція для перевірки числа на простоту (Соловея-Штрассена)

    counter = 0  # встановлюємо лічильник в 0

    while counter < k:  # поки лічильник менший за k
        x = random.randint(2, p - 1)  # вибираємо випадкове число x в інтервалі [2, p-1]
        gcd = math.gcd(x, p)  # обчислюємо НСД (x, p)

        if gcd > 1:
            return False  # якщо НСД більший за 1, p - складене число

        if not is_pseudo_prime(x, p):
            return False  # якщо p не псевдопросте за основою x, p - складене число

        counter += 1  # збільшуємо лічильник на 1

    return True  # якщо пройшли всі k ітерацій, p є ймовірно простим


# приклад
# p = 102  # число для перевірки
# k = 5  # кількість випадкових основ
#
# if s_s(p, k):
#     print(f"Число {p} є ймовірно простим.")
# else:
#     print(f"Число {p} є складеним.")

if __name__ == '__main__':
    n = 2500744714570633849
    start_time = time.time()
    res = s_s(n, 5)
    print(time.time() - start_time)
    print(f"Нетривіальний дільник числа {n} це {res}")