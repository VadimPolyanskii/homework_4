# ДЗ 4

"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def separator(symbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return symbol * count


def long_separator(count):
    """
    Функция создает разделитель из звездочек, число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return separator("*", count)


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return long_separator(10)


print(simple_separator())

print(long_separator(20))
print(long_separator(60))


print(separator('-', 40))
print(separator('$', 45))

print()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print(separator("*", 10))
    print()
    print(f'Hello {who}!')
    print()
    print(separator("#", 10))


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    hello_who()


hello_world()
hello_who()

hello_who('Max')
hello_who('Kate')

print()


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    return sum(args) ** power


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 10


print()


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в виде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for k, v in kwargs.items():
        print(f'{k} --> {v}')


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


print()


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаная последовательность
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    new_lst = []
    for el in iterable:
        if function(el):
            new_lst.append(el)

    return new_lst
    # return list(filter(iterable, function))      # Другое решение


def f(x):
    if x > 3:
        return True
    else:
        return False


print(my_filter([1,2,3,4,5,6,7,8,9], f))



#
# print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
# print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True