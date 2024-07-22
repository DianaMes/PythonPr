# n = 6

# print(n)

# ___________________________

# a = 5
# b = 4.4
# c = 'hello'

# print(f"{a} - {b} - {c}")

# ___________________________

# c = 5.89
# print(c)
# n = int(c)
# print(n)
# ______________________________


# a = 4.44445
# b = 8.69552
# print(round(a * b, 2))
# ________________________

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# _____________________________

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Добро пожаловать, Маша!')
# elif username == 'Саша':
#     print('Здравствуй, Саша!')
# elif username == 'Диана':
#     print('Привет, Дианочка!')
# else:
#     print('Привет, ', username)
# ___________________________________

# print('Введите 1-е число: ')
# a = input()
# print('Введите 2-е число: ')
# b = input()
# print(a, '+', b, '=', a + b)
# _______________________________

# i = 0
# while i < 5:
#     # if i ==3:
#     #     break
#     i = i +1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)
# ____________________________________

# a = 'qwerty'

# for i in a:
#     print(i)
# _______________________________

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'

# # print(len(text))
# # print('ещё' in text)
# # print(text.lower())
# # print(text.upper())
# print(text.replace('ещё','ЕЩЁ')) 
# ________________________________________________

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # 
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
