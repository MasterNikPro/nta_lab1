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

a = pascal(10, 6)
print(a)

