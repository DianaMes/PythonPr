# Задача 1
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data:
#     if i % 2 == 0:
#         out.append((i, i**2))
# print(out)


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)

# res = where(lambda x: x % 2 == 0, res)
# print(res)  # [2, 8, 38]
# res = list(select(lambda x: (x, x**2), res))

# ---------------------------------------------


# def where(f, col):
#     return [x for x in col if f(x)]


# data = "1 2 3 5 8 15 23 38".split()
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# -----------------------------------------------
# data = "1 2 3 5 8 15 23 38".split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
# ----------------------------------------

# users = ["user1", "user2", "user3", "user4", "user5"]
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
# -------------------------------------------
