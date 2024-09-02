# def hello(name):
#     return f"Hi, {name}"


# def bye(name):
#     return f"{name}, bye-bye"


# def make_phrase(func):
#     name = input("Введите свое имя ")
#     print(func(name))


# def make_dialog(list_funcs):
#     res = ""
#     name = input("Введите свое имя ")
#     for func in list_funcs:
#         res += func(name) + "\n"
#     print(res)


# make_phrase(hello)
# make_phrase(bye)
# name = input("Введите свое имя ")
# print(hello(name))
# print(bye(name))
# lf = [hello, bye]
# make_dialog(lf)


# создадим ФВП которая может любое число возвести в любую степень
# def calc(degree):
#     def power(base):
#         return base**degree

#     return power


# print(calc(3)(2))

# get_cube = calc(3)
# get_square = calc(2)
# print(get_cube(5))
# print(get_square(5))

# sq = lambda x: x ** 2
# print(sq(7))
# print(sq(9))
# is_even = lambda x: True if x % 2 == 0 else False
# is_even = lambda x: x % 2 == 0
# print(is_even(2))
# print(is_even(3))
# calc = {
# "+": lambda x,y: x + y,
# "-": lambda x,y: x - y,
# "/": lambda x,y: x / y,
# "*": lambda x,y: x * y,
# }

# eq = input("Введите арифметическое выражение ")
# num1, op, num2 = eq.split()
# print(calc[op](int(num1), int(num2)))
# sp = [1, 2, 3, 4, 5, 6, 8, 99, 11]
# # print(*map(lambda x: x ** 2, sp))
# # print(list(map(lambda x: x ** 2, sp)))
# # print(list(filter(lambda x: x % 2, sp)))
# for i, value in enumerate(sp):
#     print(f"{i = } , {value = }")

# sp2 = ["Vsya", "Sasha"]
# for item in zip(sp2, sp):
#     print(item)
# -----------------------------------------------------------------

# Задача №2. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2


# def find_farthest_orbit(list_of_orbits):
#     list_area = list(
#         map(
#             lambda orbit: orbit[0] * orbit[1] if orbit[0] != orbit[1] else 0,
#             list_of_orbits,
#         )
#     )
#     return list_area.index(max(list_area)) + 1


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(find_farthest_orbit(orbits))

# ------------

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# # def find_farthest_orbit(list_of_orbits):
# # sList = list(map(lambda x: 0 if x[0] == x[1] else x[0] * x[1], list_of_orbits))
# # maxS = max(sList)
# # # final = sList.index(maxS) + 1
# # return sList.index(maxS) + 1
# # print(find_farthest_orbit(orbits))

# sList = [0 if x[0] == x[1] else x[0] * x[1] for x in orbits]
# maxS = max(sList)
# final = sList.index(maxS) + 1

# print(final)

# ----------------------------------------------------------------
# Задача №3. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# def same_by(characteristic, objects):
#     result = True
#     list1 = [characteristic(x) for x in objects]
#     for i in range(len(list1) - 1):
#         if list1[i] != list1[i + 1]:
#             result = False
#     return result


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

# # --------------

# def same_by(characteristic, objects):
# # return len(set(map(characteristic, objects))) <= 1

# # # if len(objects) < 2:
# # # return True
# # # temp = characteristic(objects[0])
# # # return len(list(filter(lambda x: characteristic(x) == temp, objects))) == len(objects)

# return len(list(filter(characteristic, objects))) % len(objects) == 0
