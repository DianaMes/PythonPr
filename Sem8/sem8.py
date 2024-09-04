# import sqlite3 as sl


# conn = sl.connect("study.db")

# cur = conn.cursor()

# cur.execute(
#     """
# CREATE TABLE IF NOT EXISTS students
# (id INTEGER PRIMARY KEY,
# name TEXT,
# surname TEXT
# );"""
# )

# # cur.execute("INSERT INTO students VALUES (1,'Ваня','Петров');")
# # cur.execute("INSERT INTO students VALUES (2,'Сергей','Сергеев');")

# cur.execute("SELECT * FROM students;")
# res = cur.fetchall()
# print(res)


# conn.commit()
# conn.close()

# -------------------------------------------------

# import sqlite3 as sl
# from easygui import *


# def select_all():
#     cur.execute("SELECT * FROM students;")
#     return cur.fetchall()


# def add_values():
#     cur.execute("INSERT INTO students VALUES (1,'Ваня','Петров');")
#     cur.execute("INSERT INTO students VALUES (2,'Сергей','Сергеев');")


# def select_ivan():
#     cur.execute("SELECT * FROM students WHERE name = 'Ваня';")
#     return cur.fetchall()


# conn = sl.connect("study.db")
# cur = conn.cursor()
# cur.execute(
#     """
# CREATE TABLE IF NOT EXISTS students
# (id INTEGER PRIMARY KEY,
# name TEXT,
# surname TEXT
# );"""
# )

# choice = choicebox("Выберите запрос", "Главная форма", ["Все записи", "Только Ваня"])

# if choice == "Все записи":
#     msg = select_all()
#     msgbox(msg, "Результат запроса")
# elif choice == "Только Ваня":
#     msg = select_ivan()
#     msgbox(msg, "Результат запроса")


# conn.commit()
# conn.close()

# ------------------------------------------------------------------

# Задача. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# spisok = [["Иван", "8909090999"]]

# while True:
#     command = input("введите команду: ")
#     if command == "find":
#         x = input("введите имя абонента: ")
#     for i in range(len(spisok)):
#         if spisok[i][0] == x:
#             print(spisok[i][0], spisok[i][1])
#     if command == "add":
#         x = input("Введите Имя абонента и его номер через пробел: ")
#     spisok.append(x.split())
#     if command == "show":
#         for i in spisok:
#             print(*i)

# --------------

# phonebook = {
#     "дядя Ваня": {
#         "phones": [1212121, 5555555],
#         "email": "777@mail.com",
#         "birthday": "10.10.1990",
#     },
#     "дядя Вася": {"phones": [888888]},
# }

# # print(phonebook['дядя Ваня'])
# # print(phonebook['дядя Ваня'] ['phones'])
# print(phonebook["дядя Ваня"]["phones"][0])

# ------------------------

# import json
# contact = {"дядя Ваня": {'phones': [1212121,5555555],
# 'email': '777@mail.com', 'birthday': '10.10.1990'},
# "дядя Вася": {'phones': [888888]}
# }

# contact["Igor"] = {'phones':[440440, 2202220]}

# def save():
#     with open("films.json","w",encoding="utf-8") as fh:
#         fh.write(json.dumps(contact,ensure_ascii=False))
# print("Nasha biblioteca sohranena")

# def load():
#     with open("films.json","r",encoding="utf-8") as fh:
#         contact=json.load(fh)
#     print("Filmoteca zagrujena")
#     return contact


# while True:
#     command=input("Vvedite comand ")
#     if command=="/start":
#         print("spravochnic nachal rabotu")
#     elif command=="/stop":
#         save()
#     print("spravochnic ostanovil raboty")
#     break
#     elif command=="/all":
#     print("Tekushii spisok filmov")
#     print(contact)
#     elif command =="/add":
# f=input("Vvedite nazvanie ")
# contact.append(f)
# print("Film dobavlen v spisok")
# elif command=="/find":
# name = input("Vvedite imia: ")
# print(contact[name]['phones'])

# # ---------------------------------

# phonebook = open("phonebook.txt","r",encoding="utf-8")
# z = phonebook.readline()
# spisok = [str(i).split() for i in phonebook]
# phonebook = open("phonebook.txt","w",encoding="utf-8")

# phonebook.close()
# print(spisok)
# q = True
# while q:
# command = input("Введите команду: ")
# if command == "Поиск":
# x = input("Введите имя абонента: ")
# for i in range(len(spisok)):
# if spisok[i][0] == x:
# print(spisok[i][0],spisok[i][1])

# elif command == "добавить":
# phonebook = open("phonebook.txt","w", encoding="utf-8")
# phonebook.writelines(z)
# # x = input("Введите Имя абонента и его номер через пробел: ")
# x = input("введите имя обонента и его номера через пробел")
# spisok.append(x.split())
# # while True:
# # m = input("Добавить еще номер абонента? (да/нет)")
# # if m == "да":
# # x += input("Введите номер: ")
# # else: break
# for i in spisok:
# phonebook.writelines(str(i))
# phonebook.close()
# elif command == "вывод":
# for i in spisok:
# print(*i)
# elif command == "Выход":
# q = False

# else:
# print("неверная команда")
