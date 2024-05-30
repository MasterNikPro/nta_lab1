# pascal test for dividing from methodichka


def pascal(number, dividor):
    number_string = str(number)
    lenght_of_number = len(number_string)
    # массив для залишків після ділення перший елемент 1 бо 10^0 це 1
    remainder_array = [1]
    for i in range(1, lenght_of_number):
        # кожний наступний член послідовності це минуле значення помноженне на 10 и залишок від ділення dividor
        remainder_array.append((remainder_array[i - 1] * 10) % dividor)
    sum_string = 0

    for i in range(lenght_of_number):
        # робимо число суммою
        sum_string += int(number_string[lenght_of_number - i - 1]) * remainder_array[i]
        # дивимось на відповідь
    return sum_string % dividor == 0



def division(value):
    dividers=[]
     #перевіряємо на подільність на 2
    if value % 2 == 0:
        return 2
    #перевіряємо тепер як воно ділиться на непарні числа йдемо до корня з значення +1 щоб оптимізувати алгоритм
    for i in range(3, 47, 2):
        if pascal(value, i):
           return i

    return 0

n = 13195
factors = division(n)
print(f"Простые делители числа {n}: {factors}")