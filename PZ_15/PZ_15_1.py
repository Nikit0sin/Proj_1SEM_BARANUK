# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Вариант 1
# Разработать БД «Турист» с тремя таблицами, установить связь между
# таблицами. Заполнить таблицы произвольными данными (не менее 10
# записей). Реализовать SQL-запросы на выборку, обновление, удаление
# данных из БД.
import sqlite3 as sq
import PZ_15_2
from PZ_15_2 import tourists, tours, booking


with sq.connect('tourist.db') as con:
    cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tourists(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    sex VARCHAR,
    birth_date DATE,
    telephone_number VARCHAR, 
    email VARCHAR
)""")


with sq.connect('tourist.db') as con:
    cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tours(
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    country VARCHAR,
    town VARCHAR,
    start_date DATE,
    end_date DATE, 
    price DECIMAL
)""")


with sq.connect('tourist.db') as con:
    con.execute('PRAGMA forign_keys = ON')
    cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS booking(
    id INTEGER PRIMARY KEY,
    id_tourists INTEGER,
    id_tours INTEGER,
    date_of_booking DATE,
    quantity_of_tourists INTEGER,
    FOREIGN KEY (id_tourists) REFERENCES tourists(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_tours) REFERENCES tours(id) ON DELETE CASCADE ON UPDATE CASCADE
)""")


# with sq.connect('tourist.db') as con:
#      cur = con.cursor()
#      cur.executemany("INSERT INTO tourists VALUES (?, ?, ?, ?, ?, ?, ?)", tourists)


# with sq.connect('tourist.db') as con:
#         cur = con.cursor()
#         cur.executemany("INSERT INTO tours VALUES (?, ?, ?, ?, ?, ?, ?)", tours)


# with sq.connect('tourist.db') as con:
#         cur = con.cursor()
#         cur.executemany("INSERT INTO booking VALUES (?, ?, ?, ?, ?)", booking)

#Выборка
#1
# Вывести список всех туристов
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, first_name, last_name FROM tourists")
#     result = cur.fetchmany(11)
# print(result)

#2
#Вывести список всех туров, отсортированных по цене в порядке убывания
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name FROM tours ORDER BY price DESC")
#     sel = cur.fetchall()
# print(sel)

#3
# Вывести список всех бронирований, сделанных в заданном городе
# -

#4
# Вывести список всех туристов, сделавших бронирование в определенный период времени
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id_tourists, date_of_booking FROM booking WHERE date_of_booking BETWEEN '01.03.2023' AND '30.10.2023'")
#     dat = cur.fetchall()
# print(dat)

#5
# Вывести список всех туров с указанием названия страны и города
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, country, town FROM tours")
#     twn = cur.fetchall()
# print(twn)

#6
# Вывести список всех туристов, женщин, у которых дата рождения позже 01.01.1990
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, birth_date FROM tourists WHERE birth_date > '01.01.2000'")
#     wmn = cur.fetchall()
# print(wmn)

#7
# Вывести список всех туров, цена которых больше 5000
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, name FROM tours WHERE price > 2000")
#     nma = cur.fetchall()
# print(nma)

#8
# Вывести список всех туристов, которые сделали бронирование на конкретный тур
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id_tourists, date_of_booking FROM booking WHERE date_of_booking = '20.06.2023'")
#     trdt = cur.fetchall()
# print(trdt)

# 9
# Вывести список всех туристов, которые сделали бронирование на тур в указанную дату
# -

#10
# Вывести список всех туристов, у которых номер телефона начинается на '897'
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, telephone_number FROM tourists WHERE telephone_number LIKE '897%'")
#     trdt = cur.fetchall()
# print(th)


#Обновление
#1
# Изменить дату начала тура с id=1 на '01.05.2023':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET start_date = '01.05.2023' WHERE id = 1")

#2
# Обновить цену тура с id=7 на 1500:
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET price = 1500 WHERE id = 7")

#3
# Изменить номер телефона туриста с id = 5 на '85551234567':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tourists SET telephone_number = '85551234567' WHERE id = 5")

#4
# Изменить дату бронирования с id=3 на '25.02.2023':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE booking SET date_of_booking = '25.02.2023' WHERE id = 3")


#5
# Обновить количество туристов в бронировании с id=8 на 3
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE booking SET quantity_of_tourists = 3 WHERE id = 8")

#6
# Изменить дату окончания тура с id=2 на '31.08.2023':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET end_date = '31.08.2023' WHERE id = 2")

#7
# Обновить электронную почту туриста с id=1 на 'new_email@example.com':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tourists SET email = 'new_email@example.com' WHERE id = 1")

#8
# Изменить дату начала тура с id=4 на '15.06.2023':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET start_date = '15.06.2023' WHERE id = 4")

#9
# Обновить дату начала тура на 2023-05-01 для всех туров, где страна = 'Ирландия':
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET start_date = '01.05.2023' WHERE country = 'Ирландия'")

#10
# Обновление цены на тур 'Еврейская мечта' на 10000 у.е.
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET price = 10000 WHERE name = 'Еврейская мечта'")

#11
# Обновление даты начала тура 'ИСПАНЦЫ' на '01.06.2023'
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET start_date = '01.06.2023' WHERE name = 'ИСПАНЦЫ'")

#12
# Обновление количества туристов в бронировании с id 2 на 3 человека
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE booking SET quantity_of_tourists = quantity_of_tourists+3 WHERE id = 2")

#13
# Обновление номера телефона у туриста с id 2 на '81234567890'
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tourists SET telephone_number = '81234567890' WHERE id = 2")

#14
#Обновление даты начала тура на 01.07.2024'-01 для всех туров, цена которых меньше 2000 у.е.
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tours SET start_date = '01.07.2024' WHERE price < 2000")

#15
#Обновление электронной почты у всех туристов из России на new_email@example.com.
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tourists SET email = 'new_email1@example.com' WHERE sex = 'ж'")

#16
# Обновление даты начала тура на 2023-08-15 для всех бронирований с количеством туристов больше 2.
# -

#17
# Обновление названия тура на "Египет-отдых на курорте" для всех бронирований с id_тура равным 1003
#-

#  Удаление
#1
# Удалить все бронирования, связанные с туристом с id=1
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM booking WHERE id_tourists = 1")

#2
# Удалить все бронирования, связанные с туром с id=2
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM booking WHERE id_tours = 2")

#3
# Удалить все бронирования, сделанные в определенную дату
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM booking WHERE date_of_booking = '25.04.2023'")

# Задания с 4 по 10 я не понял как правильно выполнить