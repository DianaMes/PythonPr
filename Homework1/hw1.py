# Задание 1
# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в переменную res.

# n = 123

# res = sum(int(digit) for digit in str(n))
# print(res)

# hundred = n // 100
# ten = (n // 10) % 10
# unit = n % 10
# res = hundred + ten + unit
# print(res)

# _________________________________________________________

# Задание 2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
# Пример:
# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10 

# n = 24

# x = n // 6
# Pet = x
# Ser = x
# Kat = 4 * x
# print(Pet,  Kat,  Ser )
# __________________________________________________________________________________________________________________

# Задание 3
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# Пример:
# n = 385916 -> yes
# n = 123456 -> no

# n = 385916

# sum_first_three = sum(int(digit) for digit in str(n)[:3])

# sum_last_three = sum(int(digit) for digit in str(n)[-3:])

# if sum_first_three == sum_last_three:
#     print('yes')
# else:
#     print('no')

# n_str = str(n)
# first_three = n_str[:3]
# last_three = n_str[3:]
# sum_first_three = sum(int(digit) for digit in first_three)
# sum_last_three = sum(int(digit) for digit in last_three)
# if sum_first_three == sum_last_three:
#     print('yes')
# else:
#     print('no')

# _________________________________________________________________________
# Задание 4
# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

a = 3
b = 2
c = 4

if c <= a * b and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')