# Задание №1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

# list_1 = [1, 2, 3, 4, 5, 3, 3]
# k = 3

# counts = list_1.count(k)
# print (counts)

# --------------------------------------------------------------------------------------

# Задание №2
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6 

# bliz_el = None
# min_diff = float ('inf')
# for num in list_1:
#     diff = abs(num - k)
#     if diff < min_diff:
#         min_diff = diff
#         bliz_el = num
# print(bliz_el)

# --------------------------------------------------------------------------------------

# Задание №3
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Пример:
# k = 'ноутбук'
# # 12

# # Стоимости букв для английского алфавита
# english_scores = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# # Стоимости букв для русского алфавита
# russian_scores = {
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#     'Й': 4, 'Ы': 4,
#     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#     'Ш': 8, 'Э': 8, 'Ю': 8,
#     'Ф': 10, 'Щ': 10, 'Ъ': 10
# }

# k = 'ноутбук'
# def calculate_k_score(k):
#     # Приведение слова к верхнему регистру
#     k = k.upper()

#     # Определение алфавита, на котором написано слово
#     if k[0] in english_scores:
#         scores = english_scores
#     elif k[0] in russian_scores:
#         scores = russian_scores
#     else:
#         raise ValueError("Слово должно содержать только английские или только русские буквы")

#     # Подсчет стоимости слова
#     score = sum(scores.get(letter, 0) for letter in k)
#     return score

# # Вычисление и вывод стоимости слова
# print(calculate_k_score(k))

# -------------------------------------------------------------------------------

# Задание №4
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]​

# a = [1,0,1]
# k = 9
# for i in range(k-2):
#     a.append(a[-1]+a[-2])
#     a.insert(0,a[-1]*((-1)**(i+1)))
# print(a)

# -------------------------------------------------------------------------------

# Задание №5
# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие 
# максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта послед-сть длиннее чем от 7 до 8
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта послед-сть длиннее чем от 7 до 8

# def find_max_increasing_subsequence(arr):
#     if not arr:
#         return []

#     max_start_index = 0
#     max_end_index = 0
#     current_start_index = 0

#     for i in range(1, len(arr)):
#         if arr[i] <= arr[i - 1]:
#             # Завершаем текущую возрастающую последовательность
#             if i - current_start_index > max_end_index - max_start_index:
#                 max_start_index = current_start_index
#                 max_end_index = i - 1
#             # Начинаем новую возрастающую последовательность
#             current_start_index = i

#     # Проверка последней последовательности
#     if len(arr) - current_start_index > max_end_index - max_start_index + 1:
#         max_start_index = current_start_index
#         max_end_index = len(arr) - 1

#     return [arr[max_start_index], arr[max_end_index]]

# # Пример
# print(find_max_increasing_subsequence([1, 5, 2, 3, 4, 6, 1, 7]))  # [1, 7]

# ----------------------------------------------------------------------------------

# Задание №6
# Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали, выходящей из левого 
# верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# def generate_spiral(n):
#     # Создаем пустую таблицу размером n x n
#     spiral = [[0] * n for _ in range(n)]
    
#     # Определяем границы спирали
#     top, bottom, left, right = 0, n - 1, 0, n - 1
#     num = 1
    
#     while top <= bottom and left <= right:
#         # Заполняем верхнюю горизонтальную линию
#         for col in range(left, right + 1):
#             spiral[top][col] = num
#             num += 1
#         top += 1
        
#         # Заполняем правую вертикальную линию
#         for row in range(top, bottom + 1):
#             spiral[row][right] = num
#             num += 1
#         right -= 1
        
#         # Заполняем нижнюю горизонтальную линию
#         for col in range(right, left - 1, -1):
#             spiral[bottom][col] = num
#             num += 1
#         bottom -= 1
        
#         # Заполняем левую вертикальную линию
#         for row in range(bottom, top - 1, -1):
#             spiral[row][left] = num
#             num += 1
#         left += 1
    
#     return spiral

# def print_spiral(spiral):
#     for row in spiral:
#         print(' '.join(map(str, row)))

# # Пример использования
# n = 5
# spiral = generate_spiral(n)
# print_spiral(spiral)

# --------------------------------------------------------------------------------

# Задание №7
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
# | | Х |
# | | O |
# | | O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход

import random

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # First row
        [board[1][0], board[1][1], board[1][2]],  # Second row
        [board[2][0], board[2][1], board[2][2]],  # Third row
        [board[0][0], board[1][0], board[2][0]],  # First column
        [board[0][1], board[1][1], board[2][1]],  # Second column
        [board[0][2], board[1][2], board[2][2]],  # Third column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal
        [board[2][0], board[1][1], board[0][2]]   # Anti-diagonal
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_bot_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells) if empty_cells else None

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True
    
    while True:
        print_board(board)
        
        if player_turn:
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board, 'X'):
                    print_board(board)
                    print("Вы выиграли!")
                    break
            else:
                print("Эта клетка уже занята, попробуйте другую.")
                continue
        else:
            row, col = get_bot_move(board)
            if row is not None:
                board[row][col] = 'O'
                if check_winner(board, 'O'):
                    print_board(board)
                    print("Бот выиграл!")
                    break
            else:
                print("Ничья!")
                break

        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()
