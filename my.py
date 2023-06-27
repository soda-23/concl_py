'''========Строки=========='''
# неизменямый тип данных, каторый   предназанчина для хранение последователност символов заключение в одирнарные или двойные кавычки

# string1 = "Строка"
# string2 = 'Строка'
# string3 = "Неправелно'

# string4 = "don't"
# string5 = 'he: hello"'


# #string6 = '''
# # hello
# # soda
# # main
# # class

# '''

# string7 = """

# hello
# soda
# main
# class
# """

# #print(string6)



''' Экранированные последовательности'''

# последовательности символов , начинающаяся  с-> \
# '\n' # -> перенос на следущую строку
# '\t' # -> Тобуляция
# '\\' # -> Для отображение
# '\"' # -> Для отображение
# '\r' # -> возвращает каретку ы начало сторки
# '\v' # -> вертикалная табулясия




# string = 'lello\vmakers\nsoda'

# print(string)

'''Конкантенция -> скдлевание строки'''

# str_1 = 'Hello '
# str_2 = 'World'

# # print(str_1 + ' ' + str_2)
# print(str_1 *100)
# '''============= Формотирование строк============'''

# 1. с использование %
# 2. с использование метода 
# 3. интерполяция строки (f- сторки)

# name = input('Как вас зовут')
# a = input()
# result = 'Hello,   %s' 

print(result)
. format
name = input("Как вас зовут:")
age = input("Сколька вам лет:")
test = input("Что вы умете:")   
result = 'Hello, {} {} {}'.format(name, age, test)

#f-строка

name = input("your name")
age = input("your age")
test = input("yor age")
result = f'Hello {name} your ara{age} your old {test}'
print(result)

'''=======Индексы=============='''
# ПОРЯДКОВЫЙ НОМЕР СИМВОЛОВ В СТРОКЕ
"H E L L O   W O R L D"
#0 1 2 3 4 5 6 7 8 9 10
# str_ = 'Hello world '

# print(str_[0])
# '''==========Срезы==========='''
# # получение подстраки (какой-то число части строки)
# print(str_[:5])
# print(str_[0:-1])



# str_ = 'Hello'
# str_[::-1]
# print(str_[:: -1])
# #  Срезы по индексу -> [3:] -> начиная с 3
# # до самого конца, [;6]  -> c 0 индекса 
# # до 6(не вклбчително) [::]

# str.isdigit() # состоит  ил в строке толька числа
# str.islower() # находится ли строка  
# print (dir( hello' ))


# методы на is -> проверяют # возвращают True/False
# str.isalnum() -> состоит ли строка только из букв и/или чисел
# str.isalpha() -> состоит ли строка только из букв
# str.isdigit() #-> состоит ли строка толлько из чисел
# str.islower ( ) #-> находится ли строка в нижнем регистре
# str.isupper() # -> состоит ли строка из

# str.title()
# str = 'Hello'

# print(str.title)



# str1= 'ha ha ha ha'
# new_str = str.replace('ha', 'yas' )
# print(new_str)







print(dir('hello'))

# методы на is -> проверяют
# возвращают True/False
str.isalnum() -> состоит ли строка только из букв и/или чисел
str.isalpha() -> состоит ли строка только из букв
str.isdigit() #->  состоит ли строка толлько из чисел
str.islower() #-> находится ли строка в нижнем регистре
str.isupper() # -> состоит ли строка из символов верхнего регистра
str.isspace() # -> состоит ли строка из неотображаемых символов (пробелы и экранированные последовательности)
str.isnumeric() # ->  состоит ли строка толлько из чисел

print('hello9'.isalpha())
print('1234 '.isdigit())


str.upper() -> переводит в верхний регистр
str.lower() -> переводит в гижний регистр

str_ = 'Makers'
a = str_.lower() #makers
print(a)

str_ = 'Makers'
a = str_.upper() #MAKERS
print(a)

str.title() -> каждое слово в строке запишет с заглавной буквы

str.capitalize() -> только самое первое слово в строке запишет с заглавной 

str_ = 'hello Makers'
print(str_.title()) # Hello Makers
print(str_.capitalize()) #Hello makers

strip() -> убирает пробелы в начале и в конце строки (rstrip, lstrip)
len() -> возвращает длину строки

a = input('here: ')
b = a.strip()
print(len(a), a, len(b), b)


str.replace(old, new, count) -> заменяет old значение в строке на new, count - отвечает за кол-во замен

str_ = 'ha ha ha a'
new_str = str_.replace('ha', 'new', 1)
print(new_str)

str.split('разделитель') -> делит строку по разделителю и возвращает список. разделитель по умолчанию -> пробел

a = 'hello makers boot incubator test'
b = a.split('t')
print(b)
import html
age = 