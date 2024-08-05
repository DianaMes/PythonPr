# import random as rnd
# # from random import randint


# def create_rnd_list(size):
#     lst = []
#     for _ in range(size):
#         lst.append(rnd.randint(1,100))
#     return lst

# def plus_two_values(v1: int, v2: int) -> int:
#     '''
#     this function add two integer values
#     '''
# # if isinstance(v1, int) and isinstance(v2, int):
# # return v1 + v2
# # else:
# # print("Error!")
#     if not (isinstance(v1, int) and isinstance(v2, int)):
#         raise TypeError("Must be int values")
#     return v1 + v2


# # print(create_rnd_list(8))
# # print(plus_two_values.__doc__)
# # print(plus_two_values(5,8))
# # help(print)
# print(plus_two_values("hello "," world"))

# # lst = []
# # for _ in range(10):
# # lst.append(rnd.randint(1,100))
# # print(lst)

# ---------------------------------------------------------------------------------

# Задача №1. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью
# постфикса формата _n. Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# s = 'a a a b c a a d c d d'
# # data = input().split()

# data = s.split()

# data_dict = {}
# result_str = ''

# for elem in data:
#     if elem in data_dict.keys():
#         data_dict[elem] += 1
#         result_str += f'{elem}_{data_dict[elem]} '
#     else:
#         data_dict[elem] = 0
#     result_str += f'{elem} '

# print(result_str)

# -------------------------------------------------------------------------------------------------

# Задача №2. Решение в группах Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним
# или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she
#  sells sea shells on the sea shore I'm sure that the shells are sea shore shells Output: 13

# data = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''

# data = data.lower().replace('.',' ').split()

# result = len(set(data))


# print(result)

# -----------------------------------------------------------------------------------------------

# Задача №3
# задача Генерация необязательная
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты
# случайные от -10 до 10.
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

# from random import *

# k = int(input())


# def mnogochlenov(k):
#     s = []
#     for i in range(k):
#         s.append(f"*x^{i}")


# r = [randint(-10, 10) for i in range(k + 1)]
# s = s[::-1]
# res = ""
# for i in range(k):
#     if r[i] < 0:
#         res += str(r[i]) + s[i]
#     elif r[i] > 0:
#         res += "+" + str(r[i]) + s[i]
# else:
#     res += ""

# res = res.replace("*x^0", "")
# res = res.replace("x^1", "x")
# res = res.replace("-1x", "-x")
# res = res.replace("+1x", "+x")

# if res[0] == "+":
# return res[1:]
# else:
# return res

# print(mnogochlenov(k))
