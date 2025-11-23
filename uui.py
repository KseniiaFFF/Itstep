# print(f'Sum: {6+2}')

# x = 2
# y = 3
# print(x+y)

# name = 'Kseniia'
# city = 'Cherkassy'
# age = 28
# y = 4
# print(name, city, age+y)

# user_name = input('Enter your name: ')
# user_age = input('Enter your age: ')

# print('Your name is: ', user_name, 'Your age is: ', user_age)

# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# print('first + second = : ', first + second)
# print('first - second = : ', first - second)
# print('first * second = : ', first * second)
# print('first / second = : ', first / second)

# first = float(input('Enter first number: '))
# user_znak = input('Enter znak: ')
# second = float(input('Enter second number: '))

# if user_znak == '+':
#     print('first + second = : ', first + second)
# elif user_znak == '-':
#     print('first - second = : ', first - second)
# elif user_znak == '*':
#     print('first * second = : ', first * second)
# elif user_znak == '/' and second != 0:
#     print('first / second = : ', first / second)
# else :
#   print('Error')

# user_age = int(input('Enter your age: '))

# if user_age >= 0 and user_age < 3:
#   print('You are a baby')
# elif user_age >= 3 and user_age < 12:
#   print('You are a child')
# elif user_age >= 12 and user_age < 18:
#     print('You are a teenager')
# elif user_age >= 18 and user_age < 60:
#     print('You are an adult')
# else :
#     print('You are a pensioner')

# uah_usd = 42
# uah_eur = 48
# eur_usd = uah_eur / uah_usd
# usd_kzt = 540
# eur_kzt = 580
# uah_kzt = usd_kzt / uah_usd

# valuta1 = input('I give uah/usd/eur/kzt: ')
# valuta2 = input('I take uah/usd/eur/kzt: ')
# enter = int(input('Amount of currency: '))

# if enter == 0 or valuta1 == valuta2:
#    print('Incorrect data')
#    exit()

# if valuta1 == 'uah' and valuta2 == 'usd':
#     print('You will take: ', enter / uah_usd)
# elif valuta1 == 'uah' and valuta2 == 'eur':
#     print('You will take: ', enter / uah_eur)
# elif valuta1 == 'eur' and valuta2 == 'usd':
#     print('You will take: ', enter / eur_usd)
# elif valuta1 == 'eur' and valuta2 == 'uah':
#     print('You will take: ', enter * uah_eur)
# elif valuta1 == 'usd' and valuta2 == 'uah':
#     print('You will take: ', enter * uah_usd)
# elif valuta1 == 'usd' and valuta2 == 'eur':
#     print('You will take: ', enter * eur_usd)
# elif valuta1 == 'eur' and valuta2 == 'kzt':
#     print('You will take: ', enter * eur_kzt)
# elif valuta1 == 'usd' and valuta2 == 'kzt':
#     print('You will take: ', enter * usd_kzt)
# elif valuta1 == 'kzt' and valuta2 == 'eur':
#     print('You will take: ', enter / eur_kzt)
# elif valuta1 == 'kzt' and valuta2 == 'usd':
#     print('You will take: ', enter / usd_kzt)
# elif valuta1 == 'uah' and valuta2 == 'kzt':
#     print('You will take: ', enter * uah_kzt)
# elif valuta1 == 'kzt' and valuta2 == 'uah':
#     print('You will take: ', enter / uah_kzt)
# else :
#     print('Error')

# calculator = input('Do you want to use upgraded calculator? yes/no: ')

# if calculator == 'no':

#   first = float(input('Enter first number: '))
#   user_znak = input('Enter znak: ')
#   second = float(input('Enter second number: '))

#   if user_znak == '+':
#     print('first + second = : ', first + second)
#   elif user_znak == '-':
#     print('first - second = : ', first - second)
#   elif user_znak == '*':
#     print('first * second = : ', first * second)
#   elif user_znak == '/' and second != 0:
#     print('first / second = : ', first / second)
#   else: print('Error')
#   exit()

# if calculator == 'yes':

#   first = float(input('Enter first number: '))
#   user_znak1 = input('Enter first znak: ')
#   second = float(input('Enter second number: '))
#   user_znak2 = input('Enter second znak: ')
#   third = float(input('Enter third number: '))

#   v1 = first + second + third
#   v2 = first - second - third
#   v3 = first * second * third
#   v4 = first / second / third
#   v5 = first + second - third
#   v6 = first + second * third
#   v7 = first + second / third
#   v8 = first - second + third
#   v9 = first - second * third
#   v10 = first - second / third
#   v11 = first * second + third
#   v12 = first * second - third
#   v13 = first * second / third
#   v14 = first / second + third
#   v15 = first / second - third
#   v16 = first / second * third

#   if user_znak1 == '/' and second == 0:
#     print('Error')
#   if user_znak2 == '/' and third == 0:
#     print('Error')
#     exit()
#     # Принт здесь почему то не работает. Пишет ошибку деления на ноль
#   # Traceback (most recent call last):
#   #   File "/home/runner/workspace/main.py", line 127, in <module>
#   #     v4 = first / second / third
#   #          ~~~~~~^~~~~~~~
#   # ZeroDivisionError: float division by zero

#   if user_znak1 == '+' and user_znak2 == '+':
#     print('Result = : ', v1)
#   elif user_znak1 == '-' and user_znak2 == '-':
#    print('Result = : ', v2)
#   elif user_znak1 == '*' and user_znak2 == '*':
#     print('Result = : ', v3)
#   elif (user_znak1 == '/' and user_znak2 == '/') and (second != 0 or third != 0):
#     print('Result = : ', v4)
#   elif user_znak1 == '+' and user_znak2 == '-':
#     print('Result = : ', v5)
#   elif user_znak1 == '+' and user_znak2 == '*':
#     print('Result = : ', v6)
#   elif (user_znak1 == '+' and user_znak2 == '/') and third != 0:
#     print('Result = : ', v7)
#   elif user_znak1 == '-' and user_znak2 == '+':
#     print('Result = : ', v8)
#   elif user_znak1 == '-' and user_znak2 == '*':
#     print('Result = : ', v9)
#   elif (user_znak1 == '-' and user_znak2 == '/') and third != 0:
#     print('Result = : ', v10)
#   elif user_znak1 == '*' and user_znak2 == '+':
#     print('Result = : ', v11)
#   elif user_znak1 == '*' and user_znak2 == '-':
#     print('Result = : ', v12)
#   elif (user_znak1 == '*' and user_znak2 == '/') and third != 0:
#     print('Result = : ', v13)
#   elif (user_znak1 == '/' and second != 0) and user_znak2 == '+':
#     print('Result = : ', v14)
#   elif (user_znak1 == '/' and second != 0) and user_znak2 == '-':
#     print('Result = : ', v15)
#   elif (user_znak1 == '/' and second != 0) and user_znak2 == '*':
#     print('Result = : ', v16)

# else :
#   print('Enter yes or no')

# number = int(input('Сколько раз вывести слово: '))
# word = input('Введите слово: ')

# for i in range(number):
#   print ('word: ', word )

# number = int(input('Сколько раз создать пример: '))

# import random
# xzy = 0

# for i in range(number):
#   x = random.randint(0, 100)
#   y = random.randint(1, 100)
#   t = random.randint(0, 3)

#   if t == 0:

#     xzy = x + y
#     print(t)

#   elif t == 1:

#     xzy = x - y
#     print(t)

#   elif t == 2:

#     xzy = x * y
#     print(t)

#   elif t == 3:

#     xzy = x / y
#     print(t)

#   print(x, y, '=', xzy)

# while True:
#   print('Hello')

# i = int(input('Сколько раз создать пример: '))

# import random

# xzy = 0

# if i != 0:

#   while True:
#     #for i in range(number):
#     x = random.randint(0, 100)
#     y = random.randint(1, 100)
#     t = random.randint(0, 3)

#     if t == 0:

#       xzy = x + y
#       #print('+')
#       print(x, '+', y, '=')

#     elif t == 1:

#       xzy = x - y
#       #print('-')
#       print(x, '-', y, '=')

#     elif t == 2:

#       xzy = x * y
#       #print('*')
#       print(x, '*', y, '=')

#     elif t == 3:

#       xzy = x / y
#       #print('/')
#       print(x, '/', y, '=')

#       #print(x, t, y, '=')

#     user_xzy = int(input('Введите ответ: '))

#     if user_xzy == xzy:
#       print('Correct', i)
#       i = i - 1
#       if i == 0:
#         break

# import random

# user_count = int(input('Сколько раз создать пример: '))
# u = 0

# for i in range(user_count):
#   x = random.randint(1, 5)
#   y = random.randint(1, 5)
#   c = random.randint(1, 4)
#   o = 0

#   if c == 1:
#     print(f'{x} + {y} =')
#     o = x+y
#   elif c == 2:
#     print(f'{x} - {y} =')
#     o = x-y
#   elif c == 3:
#     print(f'{x} * {y} =')
#     o = x*y
#   elif c == 4:
#     print(f'{x} / {y} =')
#     o = x/y

#   while True:
#     user = int(input('user: '))
#     if user == o:
#       u = u + 1
#       print('Правильных ответов', u)
#       if u == user_count:
#         print ('Вы ответили на все вопросы правильно')
#       break

#     else:
#       print('Error')

# import random

# user_count = int(input('Какой уровень 1, 2, 3 ?: '))

# x = random.randint(1, 99)
# y = 5
# z = 3

# if user_count == 1:
#   while True:

#     user_count = int(input('Угадай число: '))

#     if user_count == x:
#       print('Вы угадали число')
#       break

#     else:
#       print('Попробуйте ещё раз.')

# if user_count == 2:
#   while True:

#     user_count = int(input('Угадай число: '))

#     if user_count == x:
#       print('Вы угадали число')
#       break

#     else:
#       y = y - 1
#       print('Попробуйте ещё раз. Осталось', y, 'попыток')

#     if y == 0:
#       print('Вы не угадали число')
#       exit()

# if user_count == 3:
#   while True:

#     user_count = int(input('Угадай число: '))

#     if user_count == x:
#       print('Вы угадали число')
#       break

#     else:
#       z = z - 1
#       print('Попробуйте ещё раз. Осталось', z, 'попыток')

#     if z == 0:
#       print('Вы не угадали число')
#       exit()

# else:
#   print('Напишите 1, 2 или 3')

# print ('Вивести на екран таблицю множення від 1 до 10.')

# x = 1
# y = 1

# while True:
#   z = x * y
#   print(x, '*', y, '=', z)
#   y = y + 1
#   if y == 11:
#     x = x + 1
#     y = 1
#     if x == 11:
#       break

# for i in range(3,100,5):
#     print(i)

# for i in range(3,100):
#     print(i)

# user_x = int(input('Какой уровень 1, 2, 3 ?: '))

# x = int(input('С какого числа начать?:'))
# y = int(input('Каким числом закончить?: '))

# if x > y:
#   for i in range(y,x):
#      print(i*2)
#   print('Вы ввели неправильные числа. Я поменял их местами', x, y)
# for i in range(x,y):
#    print(i*2)

# ========================================================================
# for i in range(3,100,5):
#     print(i)

# for i in range(3,100):
#     print(i)

# user_start = int(input(': '))
# user_stop = int(input(': '))

# for i in range(user_start,user_stop):
#     print(i)
# ========================================================================
# user_start = int(input(': '))
# user_stop = int(input(': '))

# if user_start > user_stop:
#     for i in range(user_stop, user_start):
#         print(i)
# elif user_start < user_stop:
#     for i in range(user_start, user_stop):
#         print(i)
# else:
#     print('Error')
# ========================================================================
# user_start = int(input(': '))
# user_stop = int(input(': '))

# if user_start > user_stop:
#     tmp = user_start
#     user_start = user_stop
#     user_stop = tmp

#     for i in range(user_start, user_stop):
#         print(i)
# elif user_start < user_stop:
#     for i in range(user_start, user_stop):
#         print(i)
# else:
#     print('Error')
# ========================================================================

# mss = []

# mss = [-1, 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty",'qw', 'er', 'ty', 6, 9, 4, "qwe", "rty"]

# print(mss)

# for i in range(len(mss)):
#     print(mss[i])

# print('==================')

# for item in mss:
#     print(item)

# print('==================')

# print(mss[0])
# print(mss[1])
# print(mss[2])
# print(mss[3])
# print(mss[4])
# print(mss[6])
# print(mss[7])

# my_mss = ['6',9,'4',0]
# print(my_mss)

# my_mss.append('qwerty')
# my_mss.append(2)
# print(my_mss)

# my_mss = ['6',9,'4',0]
# print(my_mss)

# my_mss[3] = 'qwerty'
# print(my_mss)

# user_date = int(input('Enter date: '))

# mss = [user_date]

# while True:
#      print(mss)
#      user_date = input('Enter date or stop: ')
#      mss.append(user_date)
#      if user_date == 'stop':
#          print('End')
#          break
#==========================================================================
# mss = []

# while True:
#     user = int(input(': '))
#     if user == 99:
#         break
#     mss.append(user)

#     for i in range(len(mss)):
#       print(mss[i])
#       print(sum(mss))
#==========================================================================
# mss = []

# s = 0
# p = 1

# while True:
#   user = int(input(': '))
#   if user == 0:
#     break
#   mss.append(user)

# for i in mss:
#   s += i
#   p *= i

# print(mss)
# print('sum:',s)
# print('pro:',p)

# import random

# user_start =int(input('Количество рандомных чисел: '))
# user_stop =int(input('Диапазон чисел (0,100): '))

# mss = []

# for i in range(user_start):
#     x = random.randint(0, user_stop)
#     mss.append(x)
#     print(x)

# x = min(mss)
# z = max(mss)
# print(x, z)
#==========================================================================
# import random

# mss = []

# while True:

#     user_enter = int(
#         input(
#             'Сделайте ход где 1-камень, 2-ножницы, 3-бумага, 0-выход из игры: '
#         ))

#     bot_enter = random.randint(1, 3)
#     print(bot_enter)

#     if user_enter == 1 and bot_enter == 2:
#         print('Ход бота: ножницы')
#         mss.append(1)
#         print('-Вы выиграли-')
#     elif user_enter == 1 and bot_enter == 3:
#         print('Ход бота: бумага')
#         mss.append(-1)
#         print('-Вы проиграли-')
#     elif user_enter == 2 and bot_enter == 1:
#         print('Ход бота: камень')
#         mss.append(-1)
#         print('-Вы проиграли-')
#     elif user_enter == 2 and bot_enter == 3:
#         print('Ход бота: бумага')
#         mss.append(1)
#         print('-Вы выиграли-')
#     elif user_enter == 3 and bot_enter == 1:
#         print('Ход бота: камень')
#         mss.append(1)
#         print('-Вы выиграли-')
#     elif user_enter == 3 and bot_enter == 2:
#         print('Ход бота: ножницы')
#         mss.append(-1)
#         print('-Вы проиграли-')
#     elif user_enter == bot_enter:
#         print('-Ничья-')
#     elif user_enter == 0:
#         print('Вы вышли из игры')
#         print('-Кол-во очков:', sum(mss))
#         break
#     else:
#         print('Error. Enter 1, 2, 3 or 0')
#==========================================================================
# products = ['apple', 'orange', 'banana', 'cherry']
# price = [10, 8, 12, 15]
# name = []
# cart = []

# for i in range (len(products)):
#     print (products[i], '=', price [i])

# while True:
#     user_enter = input('Enter product(0-exit): ')

#     if user_enter in products:
#         index = products.index(user_enter)
#         cart.append(price[index])
#         name.append(user_enter)
#         print('Your cart: ', name, 'Total: ', sum(cart))

#     if user_enter == '0':
#         print('Exit')
#         break
#     else:
#         print('Error')
#==========================================================================
# hour = []

# while True:
#     user_hour = int(input('Enter hour(111-exit): '))
#     hour.append(user_hour)

#     if user_hour >= 0 and user_hour < 6:
#         print('Good night', hour)
#     elif user_hour >= 6 and user_hour < 12:
#         print('Good morning', hour)
#     elif user_hour >= 12 and user_hour < 18:
#         print('Good day', hour)
#     elif user_hour >= 18 and user_hour < 24:
#         print('Good evening', hour)
#     elif user_hour == 111:
#         print('Exit')
#         break
#     else:
#         print('Error. Enter 0-24')
#==========================================================================
# hour = []
# minute = []
# time = '00:00'

# while True:
#     user_time = input('Enter time. hh:mm (or exit): ')
#     #print(user_time)

#     if user_time == 'exit':
#         print('Exit')
#         break

#     user_hour = int(user_time[0:2])
#     user_minute = int(user_time[3:5])

#     if len(user_time) != 5 or user_time[2] != ':':
#          print('Error. Enter hh:mm')
#          break

#     if user_hour < 0 or user_hour > 23:
#         print('Error. Enter hour 0-23')
#     elif user_minute < 0 or user_minute > 59:
#         print('Error. Enter minute 0-59')

#     if user_hour >= 0 and user_hour < 6:
#         print('Good night', user_hour, ':', user_minute)
#     elif user_hour >= 6 and user_hour < 12:
#         print('Good morning', user_hour, ':', user_minute)
#     elif user_hour >= 12 and user_hour < 18:
#         print('Good day', user_hour, ':', user_minute)
#     elif user_hour >= 18 and user_hour < 24:
#         print('Good evening', user_hour, ':', user_minute)

#==========================================================================
#x = 'qwerty'

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])

# mss = []

# x = 'qwerty'
# print('1',x)

# for i in range(len(x)):
#   mss.append(x[i])

# print('2',mss)

# mss[1] = 'GG'
# print(mss)

# x = ''
# for item in mss:
#   x += item

# print(x)

#=====================================23.09====================================

# import random

# qwerty = []
# numbers = '0123456789'
# symbols2 ='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
# symbols3 = '!@#$%^&*()_+=-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
# user_num = int(input('Сколько символов?(минимальное кол-во 8 символов): '))
# if user_num < 8:
#     print('Error. Enter more than 8 symbols')
#     exit()

# user_symbol = int(
#     input(
#         'Какие символы? 1-только цифры, 2-цифры и буквы, 3-цифры, буквы и спецсимволы: '
#     ))

# z = len(numbers)
# x = len(symbols2)
# c = len(symbols3)

# while True:

#     if user_symbol == 1:
#         for i in range(user_num):
#             q = random.randint(0, z - 1)
#             qwerty.append(numbers[q])

#     elif user_symbol == 2:
#         for i in range(user_num):
#             w = random.randint(0, x - 1)
#             qwerty.append(symbols2[w])

#     elif user_symbol == 3:
#         for i in range(user_num):
#             e = random.randint(0, c - 1)
#             qwerty.append(symbols3[e])

#     else:
#         print('Error. Enter 1, 2 or 3')
#         break
#     x = ''
#     for item in qwerty:
#         x += item
#     print('Ваш пароль: ', x)
#     break

#=====================================23.09====================================

# import random

# words = [
#     'hello', 'world', 'python', 'programming', 'language', 'computer',
#     'science', 'data', 'machine', 'learning', 'artificial', 'intelligence',
#     'neural', 'network', 'deep', 'learning', 'convolutional', 'neural',
#     'network', 'recurrent', 'neural', 'network', 'long', 'short', 'term',
#     'memory', 'gated', 'recurrent', 'unit', 'transformer', 'model', 'natural',
#     'language', 'processing', 'text', 'classification', 'sentiment',
#     'analysis', 'named', 'entity', 'recognition', 'object', 'detection',
#     'image', 'recognition', 'computer', 'vision', 'robotics', 'autonomous',
#     'vehicles', 'drones', 'internet', 'often', 'things', 'blockchain',
#     'cryptocurrency', 'smart', 'contracts', 'decentralized', 'applications',
#     'virtual', 'reality', 'augmented', 'reality', 'gaming', 'mobile',
#     'applications', 'web', 'development', 'frontend', 'backend', 'full',
#     'stack', 'developer', 'software', 'engineering', 'quality', 'assurance',
#     'devops', 'agile', 'scrum', 'kanban', 'project', 'management', 'team',
#     'leadership', 'communication', 'problem', 'solving', 'critical',
#     'thinking', 'creative', 'problem', 'solving', 'adaptability', 'resilience',
#     'time', 'management'
# ]
# s = ['a', 'e', 'i', 'o', 'u','g','y','j','k','l','m','n','p','q','r','s','t','v','w','x','z','b','d','f','h','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M', 'c']
# user_word = []

# for i in range(1):
#     w = random.randint(0, len(words) - 1)
#     user_word.append(words[w])

# print('Случайное слово: ', user_word)

# q = int(input('Какой номер буквы заменить?: '))

# q = q-1

# w = input('На какую букву заменить?: ')

# if len(w) > 1 or len(w) == 0:
#     print('Error1')
#     exit()

# mss = []

# if w in s:

#     x = str(user_word)

#     if q < 0 or q > len(x) - 2:
#         print('Error')
#         exit()

#     for i in range(2,len(x) - 2):
#         mss.append(x[i])

#     print(mss)

#     mss[q] = str(w)
#     print(mss)

#     x = ''
#     for item in mss:
#        x += item

#     print(x)

# else:
#     print('Enter a letter')
#     exit()

#=====================================23.09====================================
# it is a good day
# text = input('Enter text: ')

# word = ['time', 'car', 'qwerty', 'mobile', 'safety', 'comfort', 'quality', 'speed', 'design', 'technology', 'performance', 'reliability', 'efficiency', 'durability', 'sustainability', 'innovation', 'day', 'night', 'morning', 'evening', 'afternoon', 'sunrise', 'sunset', 'dawn', 'dusk', 'midnight', 'noon', 'midday', 'midnight', 'midnight']

# pass_symbol = [' ', '.', ',', '!', '?', '—']

# new_text = ''
# tmp_word = ''

# for i in range(len(text)):
#     ch = text[i]
#     if ch in pass_symbol:
#         if tmp_word in word:
#             new_text += '*' * len(tmp_word)
#         else:
#             new_text += tmp_word
#         new_text += ch
#         tmp_word = ''
#     else:
#         tmp_word += ch

# if tmp_word != '':
#     if tmp_word in word:
#         new_text += '*' * len(tmp_word)
#     else:
#         new_text += tmp_word

# print(new_text)
# ====================================
# mss = [4,7,9,1,0,5,3]
# print(mss)
# mss.sort()
# print(mss)
# mss.reverse()
# print(mss)

# ====================================
# mss = ['qw','er','ty','as','df','gh']
# print(mss)
# mss.pop(2)
# print(mss)
# mss.remove('er')
# print(mss)

# ====================================
# user = input(': ').lower() # yes
# user = input(': ').upper() # YES
# print(user)
# if user == 'YES':
#     print('GG WP')
# else:
#     print('else')

# ====================================
# x = '32'
# y = 'qw 54er'

# print(x.isdigit())
# print(y.isdigit())

# ====================================
# while True:
#     user = input(': ')

#     if user.isdigit():
#         print('Qwerty')
#         print(int(user))
#         break
#     else:
#         print('ELSE')
# ====================================
# user = input(': ')
# if user == '1':
#     print('lvl 1')
# if user == '2':
#     print('lvl 2')
# if user == '3':
#     print('lvl 3')
# ====================================
# text = "ываыв 32 ваы 234 ываывв 32 выапыв1"
# digits = []
# q = ''

# for w in text:
#     if w.isdigit():
#         q += w
#     else:
#         if q != '':
#             digits.append(int(q))
#             q = ''

# if q != '':
#     digits.append(int(q))
#     q = ''
# print('Numbers:', digits)

# sum = 0
# for i in digits:
#     sum += i
# print('Sum:', sum)

# mult = 1
# for i in digits:
#     mult *= i
# print('Mult:', mult)

# ====================================

# import random

# pole1 = ['[_]', '[_]', '[_]']
# pole2 = ['[_]', '[_]', '[_]']
# pole3 = ['[_]', '[_]', '[_]']

# print(pole1)
# print(pole2)
# print(pole3)

# user_win = False
# bot_win = False

# z = [0, 1, 2]
# y = [0, 1, 2]

# bot1 = random.randint(0, len(z) - 1)
# bot2 = random.randint(0, len(y) - 1)
# i = int(bot2)

# if pole1[i] != '[_]' or pole2[i] != '[_]' or pole3[i] != '[_]':
#     if not user_win and bot_win:
#         print('Game over')
#         exit()

# while True:
#     user1 = input('user1: ')
#     user2 = input('user2: ')

#     if user2.isdigit():
#         user2 = int(user2) - 1
#     else:
#         print('Error')
#         exit()

#     if user1 == '1' and pole1[int(user2)] == '[_]':
#         pole1[int(user2)] = '[X]'

#     elif user1 == '2' and pole2[int(user2)] == '[_]':
#         pole2[int(user2)] = '[X]'

#     elif user1 == '3' and pole3[int(user2)] == '[_]':
#         pole3[int(user2)] = '[X]'

#     if pole1[0] == pole1[1] == pole1[2] == '[X]' or pole2[0] == pole2[
#             1] == pole2[2] == '[X]' or pole3[0] == pole3[1] == pole3[
#                 2] == '[X]' or pole1[0] == pole2[0] == pole3[
#                     0] == '[X]' or pole1[1] == pole2[1] == pole3[
#                         1] == '[X]' or pole1[2] == pole2[2] == pole3[
#                             2] == '[X]' or pole1[0] == pole2[1] == pole3[
#                                 2] == '[X]' or pole1[2] == pole2[1] == pole3[
#                                     0] == '[X]':
#         print(pole1)
#         print(pole2)
#         print(pole3)
#         print('User win')
#         user_win = True
#         break

#     z = [0, 1, 2]
#     y = [0, 1, 2]

#     bot1 = random.randint(0, len(z) - 1)
#     bot2 = random.randint(0, len(y) - 1)
#     i = int(bot2)

#     if bot1 == 0 and pole1[i] == '[_]':
#         pole1[i] = '[O]'
#     else:
#         bot1 = 1

#     if bot1 == 1 and pole2[i] == '[_]':
#         pole2[i] = '[O]'
#     else:
#         bot1 = 2

#     if bot1 == 2 and pole3[i] == '[_]':
#             pole3[i] = '[O]'
#     else:
#         bot1 = 0

#     if pole1[0] == pole1[1] == pole1[2] == '[O]' or pole2[0] == pole2[
#                 1] == pole2[2] == '[O]' or pole3[0] == pole3[1] == pole3[
#                     2] == '[O]' or pole1[0] == pole2[0] == pole3[
#                         0] == '[O]' or pole1[1] == pole2[1] == pole3[
#                             1] == '[O]' or pole1[2] == pole2[2] == pole3[
#                                 2] == '[O]' or pole1[0] == pole2[1] == pole3[
#                                     2] == '[O]' or pole1[2] == pole2[
#                                         1] == pole3[0] == '[O]':
#         print(pole1)
#         print(pole2)
#         print(pole3)
#         print('Bot win')
#         bot_win = True
#         break

#     print(pole1)
#     print(pole2)
#     print(pole3)

# ====================================

# pole1 = ['[_]','[_]','[_]']
# pole2 = ['[_]','[_]','[_]']
# pole3 = ['[_]','[_]','[_]']

# def show_pole():
#     print(pole1)
#     print(pole2)
#     print(pole3)

# show_pole()
# ===============================
# def print_user_data(user_data):
#     print(user_data)

# print_user_data('QWERTY')
# print_user_data('asdfgh')
# ===============================
# def print_user_data(user_data):
#     print(user_data)

# print_user_data(input('User: '))
# ===============================
# def calc(a,b):
#     summa = a + b
#     print(summa)
#     summa = summa ** summa
#     print(summa)

# # calc(int(input('num1: ')),int(input('num2: ')))
# xfdsdf = int(input('num1: '))
# y = int(input('num2: '))
# calc(xfdsdf,y)

# x = int(input('num1: '))
# xfdsdf= int(input('num2: '))
# calc(x,xfdsdf)
# ===============================
# def test_fun(a,b):
#     return a+b

# res1 = test_fun(2,2)
# res2 = test_fun(3,3)
# res3 = res1 + res2
# print(res3)
# ===============================
# import random

# def test_fun():
#     return random.randint(1,4)

# if test_fun() == 1:
#     print('Qwerty1')
# if test_fun() == 2:
#     print('Qwerty2')
# if test_fun() == 3:
#     print('Qwerty3')
# if test_fun() == 4:
#     print('Qwerty4')

# ===============================
# import random

# def test_fun():
#     return random.randint(1, 4)

# res = test_fun()

# if res == 1:
#     print('Qwerty1')
# if res == 2:
#     print('Qwerty2')
# if res == 3:
#     print('Qwerty3')
# if res == 4:
#     print('Qwerty4')

# ====================================

# first = float(input('Enter first number: '))
# user_znak = input('Enter znak: ')
# second = float(input('Enter second number: '))

# def summa(first,second):
#     print(first + second)
# def minus(first,second):
#     print(first - second)
# def umn(first,second):
#     print(first * second)
# def delit(first,second):
#     print(first / second)

# if user_znak == '+':
#     summa(first,second)
# elif user_znak == '-':
#     minus(first,second)
# elif user_znak == '*':
#     umn(first,second)
# elif user_znak == '/' and second != 0:
#     delit(first,second)
# else :
#   print('Error')
# ====================================
# import random
# user = int(input('Password(1) or text(2)? Enter 1 or 2: '))

# def password():

#   user_num = int(input('Сколько символов?(минимальное кол-во 8 символов): '))

#   qwerty = []
#   symbols = '!@#$%^&*()_+=-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
#   c = len(symbols)

#   if user_num < 8:
#                print('Error. Enter more than 8 symbols')
#                exit()

#   for i in range(user_num):
#         e = random.randint(0, c - 1)
#         qwerty.append(symbols[e])

#   x = ''
#   for item in qwerty:
#         x += item
#   print('Ваш пароль: ', x)

# qwerty = []

# def phrase():

#     words = [
#               ' The tawny-bellied hermit (Phaethornis syrmatophorus) is a species in the hummingbird family ', ' Trochilidae. It is found in Colombia ', ' Ecuador, and Peru, where it inhabits the understory of humid montane forest and is also sometimes at forest edges and in dense secondary forest. ',  ' In elevation it mostly ranges between 1,000 and 2,300 m. ', ' The tawny-bellied hermit is about 14 cm long and weighs 5 to 7 g. ', ' It has olive green upperparts, males also having reddish-orange uppertail coverts, while the central tail feathers of both sexes are long and white and the rest are dark with bright orange ends. ',  ' It has either an orange or dark brown chest, depending on subspecies. ', ' Similar to other hermit hummingbirds, it is a "trap-line" feeder, visiting a circuit of a wide variety of flowering plants for nectar, and it has a song which consists of high-pitched "tsi" calls. ', ' This tawny-bellied hermit was photographed at San Isidro Lodge near Cosanga, Napo Province, Ecuador. ']

#     user_word = []

#     for i in range(1):
#         w = random.randint(0, len(words) - 1)
#         user_word.append(words[w])

#     print('Text: ', user_word)

# if user == 1:
#     password()

# elif user == 2:
#     phrase()
# else:
#     print('Error. Enter 1 or 2')

# ===============================

# ===============================

# def show_pole(pole):
#     for i in range(3):
#         for j in range(5):
#             print(pole[i][j], ' ' ,end='')
#         print()

# pole = [
#     ['[00]', '[01]', '[02]', '[03]', '[04]'],
#     ['[10]', '[11]', '[12]', '[13]', '[14]'],
#     ['[20]', '[21]', '[22]', '[23]', '[24]'],
# ]

# show_pole(pole)

# userI = int(input('userI: '))
# userJ = int(input('userJ: '))
# user = input('user: ')
# pole[userI][userJ] = user
# # pole[int(input('userI: '))][int(input('userJ: '))] = input('user: ')

# show_pole(pole)

# ===============================

# import random

# user_size_i = int(input('user_size_i: '))
# user_size_j = int(input('user_size_j: '))

# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# pole = []

# fill_pole(pole, user_size_i, user_size_j)
# show_pole(pole, user_size_i, user_size_j)

# def user_step():
#          user1 = input('user1: ')
#          user2 = input('user2: ')

#          if user1.isdigit and user2.isdigit():
#             user1 = int(user1) - 1
#             user2 = int(user2) - 1
#          else:
#             print('Error')
#             exit()

#          if pole[int(user1)][int(user2)] == '[_]':
#              pole[int(user1)][int(user2)] = '[X]'
#          else:
#              print('Error')

#          fill_pole(pole, user_size_i, user_size_j)
#          show_pole(pole, user_size_i, user_size_j)

# def bot_step():
#   while True:
#       bot1 = random.randint(0, user_size_i - 1)
#       bot2 = random.randint(0, user_size_j - 1)

#       if pole[bot1][bot2] == '[_]':
#           pole[bot1][bot2] = '[O]'
#           break

# def user_win():
#     for i in range (user_size_i):
#         if pole[i][0] == pole[i][1] == pole[i][2] == '[X]':
#             print('User win horizontal')
#             exit()

#     for i in range (user_size_j):
#         if pole[0][i] == pole[1][i] == pole[2][i] == '[X]':
#             print('User win vertical')
#             exit()

#         if pole[0][i] == pole[1][i+1] == pole[2][i+2] == '[X]':
#             print('User win diagonal')
#             exit()
#         elif pole[0][i+2] == pole[1][i+1] == pole[2][i] == '[X]':
#             print('User win diagonal')
#             exit()

# def bot_win():
#     for i in range (user_size_i):
#         if pole[i][0] == pole[i][1] == pole[i][2] == '[O]':
#             print('Bot win horizontal')
#             show_pole(pole, user_size_i, user_size_j)
#             exit()

#     for i in range (user_size_j):
#         if pole[0][i] == pole[1][i] == pole[2][i] == '[O]':
#             print('Bot win vertical')
#             show_pole(pole, user_size_i, user_size_j)
#             exit()

#         if pole[0][i] == pole[1][i+1] == pole[2][i+2] == '[O]':
#             print('Bot win diagonal')
#             show_pole(pole, user_size_i, user_size_j)
#             exit()
#         elif pole[0][i+2] == pole[1][i+1] == pole[2][i] == '[O]':
#             print('Bot win diagonal')
#             show_pole(pole, user_size_i, user_size_j)
#             exit()

# def nothing():
#     for j in range (user_size_j):
#         for i in range (user_size_i):
#             if pole[i][j] == '[_]':
#                 return
#     print('Nothing')
#     exit()

# while True:
#     user_step()
#     bot_step()
#     user_win()
#     bot_win()
#     nothing()

#===========================================================================

# import random

# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()


# def fill_mines(mss, size_i, size_j, prosent_mines):
#     for i in range(int((size_i * size_j) * prosent_mines / 100)):
#         while True:
#             rand_i = random.randint(0, size_i - 1)
#             rand_j = random.randint(0, size_j - 1)
#             if mss[rand_i][rand_j] == '[_]':
#                 mss[rand_i][rand_j] = '[*]'
#                 break

# def user(pole, pole_size_i, pole_size_j, count_hod):
#     user1 = input('user1: ')
#     user2 = input('user2: ')

#     if user1.isdigit and user2.isdigit():
#         user1 = int(user1) - 1
#         user2 = int(user2) - 1
#     else:
#         print('Error')
#         exit()

#     if pole[int(user1)][int(user2)] == '[_]':
#                  pole[int(user1)][int(user2)] = '[X]'
#     else:
#         print('You lose')
#         exit()
#     play()

# #show_pole(pole, pole_size_i, pole_size_j)





# pole = []

# print('Выбирай размер поля и процентность мин.')
# pole_size_i = int(input('pole_size_i: '))
# pole_size_j = int(input('pole_size_j: '))
# prosent_mines = int(input('prosent_mines: '))
# count_mines = int((pole_size_i * pole_size_j) * prosent_mines / 100)
# count_hod = 0



# if prosent_mines == '100' or prosent_mines == '0':
#     print('Error')
#     exit()

# def play():    
#     fill_pole(pole, pole_size_i, pole_size_j)
#     show_pole(pole, pole_size_i, pole_size_j)
#     user(pole, pole_size_i, pole_size_j)

# # if pole_size_i.isdigit() and pole_size_j.isdigit() and prosent_mines.isdigit():
# #     pole_size_i = int(pole_size_i)
# #     pole_size_j = int(pole_size_j)
# #     prosent_mines = int(prosent_mines)

# fill_pole(pole, pole_size_i, pole_size_j)
# fill_mines(pole, pole_size_i, pole_size_j, prosent_mines)
# count_hod = user(pole, pole_size_i, pole_size_j, count_hod)

# def win(pole, size_i, size_j):
#     intmines = int((size_i * size_j) * prosent_mines / 100)
#     if int((size_i * size_j) - intmines) == count_hod:
#         print('You win')
#         exit()

# play()



#    0    1    2
# 0 [_]  [*]  [*]  
# 1 [_]  [*]  [_]  
# 2 [*]  [_]  [_]  

#===========================================================================

# import random


# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')


# def show_pole(mss, size_i, size_j):
#     for j in range(size_j):
#         print('   ', j+1, end='')
#     print()
#     for i in range(size_i):
#         print(i+1, ' ', end='')
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()


# def fill_mines(mss, size_i, size_j, count_mines):
#     for i in range(count_mines):
#         while True:
#             rand_i = random.randint(0, size_i - 1)
#             rand_j = random.randint(0, size_j - 1)
#             if mss[rand_i][rand_j] == '[_]':
#                 mss[rand_i][rand_j] = '[*]'
#                 break

# def heart(mss, size_i, size_j, count_mines):
#     for i in range(count_mines):
#         while True:
#             rand_i = random.randint(0, size_i - 1)
#             rand_j = random.randint(0, size_j - 1)
#             if mss[rand_i][rand_j] == '[_]':
#                 mss[rand_i][rand_j] = '[♥]'
#                 break


# mss1 = []

# def user(mss_game, size_i, size_j, count_hod, mss_user, mss1):

#     while True:
#         userI = input('userI: ')
#         userJ = input('userJ: ')

#         if userI.isdigit() and userJ.isdigit():
#             userI = int(userI) - 1
#             userJ = int(userJ) - 1
#         else:
#                 print('Error')
#                 exit()

#         if (userI >= 0 and userI <= size_i - 1) and (userJ >= 0
#                                                      and userJ <= size_j - 1):
#             if mss_game[userI][userJ] == '[*]':
#                 mss_user[userI][userJ] = '[*]'
#                 count_hod = -1
#                 mss1.append(-1)
#                 print('You lose')
#                 print('Number of lives', sum(mss1))
#             elif mss_game[userI][userJ] == '[♥]':
#                 mss_user[userI][userJ] = '[♥]'
#                 count_hod = +1
#                 mss1.append(1)
#                 print('You find a heart')
#                 print('Number of lives', sum(mss1))
#             else:
#                 mss_user[userI][userJ] = '[X]'
#                 count_hod += 1

#             break
#         else: 
#           print('Error')  
#     return count_hod


# def win(size_i, size_j, count_mines, count_hod, mss1):
#     if size_i * size_j - count_mines == count_hod:
#         print('WIN!')
#         return 1
#     elif sum(mss1) == -1:
#         print('You lost:(')
#         return 2



# pole_user = []
# pole_game = []

# print('Выбирай размер поля и процентность мин.')
# pole_size_i = int(input('pole_size_i: '))
# pole_size_j = int(input('pole_size_j: '))
# prosent_mines = int(input('prosent_mines: '))

# count_mines = int((pole_size_i * pole_size_j) * prosent_mines / 100)
# count_hod = 0

# fill_pole(pole_game, pole_size_i, pole_size_j)
# fill_mines(pole_game, pole_size_i, pole_size_j, count_mines)
# heart(pole_game, pole_size_i, pole_size_j, count_mines)
# fill_pole(pole_user, pole_size_i, pole_size_j)

# while True:
#     show_pole(pole_user, pole_size_i, pole_size_j)
#     count_hod = user(pole_game, pole_size_i, pole_size_j, count_hod, pole_user, mss1)
#     if win(pole_size_i, pole_size_j, count_mines, count_hod, mss1) == 1:
#         break
#     if win(pole_size_i, pole_size_j, count_mines, count_hod, mss1) == 2:
#         break

#===========================================================================
# import random

# mss = []
# size_i = 10
# size_j = 10
# mss_c = []
# mss_a = []
# #mss_e = []
# mss_d = []
# mss_h = []

# def fill_pole():
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole():
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# def fill_items():
#     for i in range(5):
#         while True:
#             rand_i = random.randint(0, size_i - 1)
#             rand_j = random.randint(0, size_j - 1)
#             if mss[rand_i][rand_j] == '[_]':
#               mss[rand_i][rand_j] = '[C]'
              
#             rand_z = random.randint(0, size_i - 1)
#             rand_x = random.randint(0, size_j - 1)
#             if mss[rand_z][rand_x] == '[_]':
#               mss[rand_z][rand_x] = '[A]' 
              
#             rand_q = random.randint(0, size_i - 1)
#             rand_w = random.randint(0, size_j - 1)
#             if mss[rand_q][rand_w] == '[_]':
#               mss[rand_q][rand_w] = '[D]'
              
#             rand_o = random.randint(0, size_i - 1)
#             rand_p = random.randint(0, size_j - 1)
#             if mss[rand_o][rand_p] == '[_]':
#               mss[rand_o][rand_p] = '[D]'
              
#             rand_t = random.randint(0, size_i - 1)
#             rand_y = random.randint(0, size_j - 1)
#             if mss[rand_t][rand_y] == '[_]':
#               mss[rand_t][rand_y] = '[H]'

#             rand_t = random.randint(0, size_i - 1)
#             rand_y = random.randint(0, size_j - 1)
#             if mss[rand_t][rand_y] == '[_]':
#               mss[rand_t][rand_y] = '[E]'
#             break

# def print_user_case():
#   print('Number of C',sum(mss_c))
#   print('Number of A',sum(mss_a))
#   print('Number of D',sum(mss_d))
#   print('Number of H',sum(mss_h))

# a_sum = []
# c_sum = []
# d_sum = []
# h_sum = []
# enemy_average = 0
# user_average = 0
# user_plus = 0
# en_plus = 0

# def enemy(user_plus, en_plus, user_average, enemy_average):
#   for i in range(1):
#     while True:
#       a_enemy = random.randint(0, 5)
#       c_enemy = random.randint(0, 5)
#       d_enemy = random.randint(0, 5)
#       h_enemy = random.randint(0, 5)
#       a_sum.append(a_enemy)
#       c_sum.append(c_enemy)
#       d_sum.append(d_enemy)
#       h_sum.append(h_enemy)
#       enemy_average = (a_enemy + c_enemy + d_enemy + h_enemy) / 4
#       print('Enemy A',a_sum)
#       print('Enemy C',c_sum)
#       print('Enemy D',d_sum)
#       print('Enemy H',h_sum)
#       print('Enemy average',enemy_average)
#   krit()
#   if krit == 1:
#     chance_krittt(user_plus, en_plus, user_average, enemy_average)
#   battle(user_plus, en_plus, user_average, enemy_average)
#   #break

# def user(user_plus, en_plus, user_average, enemy_average):
#   start_user = [0, 0]
#   mss[start_user[0]][start_user[1]] = '[U]'
  
#   while True:
#     show_pole()
#     userI = input('Enter w,s,a,d or q for exit: ')

#     if userI == 'q':
#       print('Exit')
#       break

#     mss[start_user[0]][start_user[1]] = '[_]'

#     if userI == 'w' and start_user[0] > 0:
#       start_user[0] -= 1
      
#     elif userI == 's' and start_user[0] < size_i - 1:
#       start_user[0] += 1
      
#     elif userI == 'a' and start_user[1] > 0:
#       start_user[1] -= 1
      
#     elif userI == 'd' and start_user[1] < size_j - 1:
#       start_user[1] += 1
#     else:
#       print('Error. Enter w, a, s, d')

#     if mss[start_user[0]][start_user[1]] == '[C]':
#       mss_c.append(1)
#       print_user_case()

#     elif mss[start_user[0]][start_user[1]] == '[A]':
#       mss_a.append(1)
#       print_user_case()

#     elif mss[start_user[0]][start_user[1]] == '[D]':
#       mss_d.append(1)
#       print_user_case()

#     elif mss[start_user[0]][start_user[1]] == '[H]':
#       mss_h.append(1)
#       print_user_case()

#     elif mss[start_user[0]][start_user[1]] == '[E]':
#       user_average = (sum(mss_a) + sum(mss_c) + sum(mss_d) + sum(mss_h)) / 4
#       print('User average',user_average)
#       krit()
#     if krit == 1:
#       chance_krittt(user_plus, en_plus, user_average, enemy_average)
              
#       enemy(user_plus, en_plus, user_average, enemy_average)

#     mss[start_user[0]][start_user[1]] = '[U]'

# def battle(user_plus, en_plus, user_average, enemy_average):
#   #user_average = user_average + user_plus
#   #enemy_average = enemy_average + en_plus
#   print('User average',user_average)
#   print('Enemy average',enemy_average)
#   if user_average > enemy_average:
#     print('You win')
#   elif user_average < enemy_average:
#     print('- You lose, start a new game -')
#     fill_pole()
#     fill_items()
#     user(user_plus, en_plus, user_average, enemy_average)
#   else:
#     print('Draw, the game continues')

# def chance_krittt(user_plus, en_plus, user_average, enemy_average):
#   user_average = user_average + user_plus
#   krit_perc_us = random.randint(1, 30)
#   krit_perc_en = random.randint(1, 30)
#   user_plus = krit_perc_us / 100
#   en_plus = krit_perc_en / 100
#   print('User plus',user_plus)
#   print('Enemy plus',en_plus)
  
# def krit():
#   chance_krit = random.randint(1, 2)
#   print(chance_krit)
#   if chance_krit == 1:
#     print('Krit')
#     #chance_krittt(user_plus, en_plus)
#     return 1
#   elif chance_krit == 2:
#     print('No krit')
#     return 2
  
    
# fill_pole()
# fill_items()
# user(user_plus, en_plus, user_average, enemy_average)

#===========================================================================

# import random

# size_i = 10
# size_j = 10
# mss = []

# mss_c = []
# mss_a = []
# mss_d = []
# mss_h = []

# def fill_pole():
#     mss.clear()
#     for i in range(size_i):
#         row = ['[_]' for _ in range(size_j)]
#         mss.append(row)

# def show_pole():
#     for i in range(size_i):
#         for j in range(size_j):
#             if start_user[0] == i and start_user[1] == j:
#                 print('[U]', end=' ')
#             else:    
#                 print(mss[i][j], end=' ')
#         print()
#     print()

# enemy_pos = []

# def fill_items():
#     for i in range(5):
#       while True:
#         rand_i = random.randint(0, size_i - 1)
#         rand_j = random.randint(0, size_j - 1)
#         if mss[rand_i][rand_j] == '[_]':
#           mss[rand_i][rand_j] = '[C]'
#           break    
            
#     for i in range(5):
#       while True:
#         rand_z = random.randint(0, size_i - 1)
#         rand_x = random.randint(0, size_j - 1)
#         if mss[rand_z][rand_x] == '[_]':
#           mss[rand_z][rand_x] = '[A]' 
#           break  

#     for i in range(5):
#           while True:
#             rand_z = random.randint(0, size_i - 1)
#             rand_x = random.randint(0, size_j - 1)
#             if mss[rand_z][rand_x] == '[_]':
#               mss[rand_z][rand_x] = '[D]' 
#               break  

#     for i in range(5):
#           while True:
#             rand_z = random.randint(0, size_i - 1)
#             rand_x = random.randint(0, size_j - 1)
#             if mss[rand_z][rand_x] == '[_]':
#               mss[rand_z][rand_x] = '[H]' 
#               break  

#     for i in range(5):
#           while True:
#             rand_t = random.randint(0, size_i - 1)
#             rand_y = random.randint(0, size_j - 1)
#             if mss[rand_t][rand_y] == '[_]':
#               mss[rand_t][rand_y] = '[E]' 
                
#               enemy_pos.append([rand_t, rand_y])
#               break

# def fill_items2():
#     for i in range(5):
#           while True:
#             rand_i = random.randint(0, size_i - 1)
#             rand_j = random.randint(0, size_j - 1)
#             if mss[rand_i][rand_j] == '[_]':
#               mss[rand_i][rand_j] = '[C]'
#               break    

#     for i in range(5):
#       while True:
#         rand_z = random.randint(0, size_i - 1)
#         rand_x = random.randint(0, size_j - 1)
#         if mss[rand_z][rand_x] == '[_]':
#           mss[rand_z][rand_x] = '[A]' 
#           break  

#     for i in range(5):
#           while True:
#             rand_z = random.randint(0, size_i - 1)
#             rand_x = random.randint(0, size_j - 1)
#             if mss[rand_z][rand_x] == '[_]':
#               mss[rand_z][rand_x] = '[D]' 
#               break  

#     for i in range(5):
#           while True:
#             rand_z = random.randint(0, size_i - 1)
#             rand_x = random.randint(0, size_j - 1)
#             if mss[rand_z][rand_x] == '[_]':
#               mss[rand_z][rand_x] = '[H]' 
#               break  

# def print_user_case():
#   print('Number of C',sum(mss_c))
#   print('Number of A',sum(mss_a))
#   print('Number of D',sum(mss_d))
#   print('Number of H',sum(mss_h))

# def krit():
#     chance = random.randint(1, 2)
#     if chance == 1:
#         print('Krit!')
#         return True
#     else:
#         print('No krit')
#         return False

# def chance_krittt():
#     bonus = random.randint(5, 30) / 100
#     print('Crit bonus: +' + str(int(bonus*100)) + '%')
#     return bonus

# def battle(user_avg, enemy_avg):
#     print('--- BATTLE ---')

#     if krit():
#         user_avg += user_avg * chance_krittt()

#     if krit():
#         enemy_avg += enemy_avg * chance_krittt()

#     print('User final power:', user_avg)
#     print('Enemy final power:', enemy_avg)

#     if user_avg >= enemy_avg:
#         #print('You WIN!')
#         return True
#     elif user_avg < enemy_avg:
#         #print('You LOSE...')
#         return False
#     fill_pole()
#     fill_items2()
    
#     for pos in enemy_pos:
#       i, j = pos
#       mss[i][j] = '[E]'
#     user()

# def enemy_battle(user_avg):
#     a = random.randint(0, 5)
#     c = random.randint(0, 5)
#     d = random.randint(0, 5)
#     h = random.randint(0, 5)
#     enemy_avg = (a + c + d + h) / 4
#     print('Enemy A',a)
#     print('Enemy C',c)
#     print('Enemy D',d)
#     print('Enemy H',h)
#     print('Enemy avg',enemy_avg)
#     result = battle(user_avg, enemy_avg)
#     return result


# start_user = [0, 0]

# def user():

#     while True:
#         show_pole()
#         move = input('Enter w,s,a,d or q for exit: ')

#         if move == 'q':
#             print('Exit game')
#             break
            

#         mss[start_user[0]][start_user[1]] = '[_]'

#         if move == 'w' and start_user[0] > 0:
#             start_user[0] -= 1
            
#         elif move == 's' and start_user[0] < size_i - 1:
#             start_user[0] += 1
#         elif move == 'a' and start_user[1] > 0:
#             start_user[1] -= 1
#         elif move == 'd' and start_user[1] < size_j - 1:
#             start_user[1] += 1
#         else:
#             print('Invalid move')
#             continue

#         cell = mss[start_user[0]][start_user[1]]

#         if cell == '[C]':
#             mss_c.append(1)
#             print_user_case()
#             mss[start_user[0]][start_user[1]] = '[_]'
#         elif cell == '[A]':
#             mss_a.append(1)
#             print_user_case()
#             mss[start_user[0]][start_user[1]] = '[_]'
#         elif cell == '[D]':
#             mss_d.append(1)
#             print_user_case()
#             mss[start_user[0]][start_user[1]] = '[_]'
#         elif cell == '[H]':
#             print_user_case()
#             mss_h.append(1)
#             mss[start_user[0]][start_user[1]] = '[_]'
#         elif cell == '[E]':
#             user_avg = (sum(mss_a) + sum(mss_c) + sum(mss_d) + sum(mss_h)) / 4
#             print_user_case()
#             print('User average:',user_avg)
#             result = enemy_battle(user_avg)
#             print(result)

#             if result:
#                 print('You win')
#                 mss[start_user[0]][start_user[1]] = '[_]'
#             else:
#                 print('You lose')
#                 mss[start_user[0]][start_user[1]] = '[E]'
                
#         if cell == '[P]':
#             next_level()

#         elif cell == '[_]':
#             mss[start_user[0]][start_user[1]] = '[_]'
        

#         mss[start_user[0]][start_user[1]] = '[U]'
#         symbol_P = False
#         for i in range(size_i):
#             for j in range(size_j):
#                 if mss[i][j] in '[P]':    
#                     symbol_P = True
#                     print('Symbol P found')
#                     break
#             if symbol_P:
#                 break
#         if not symbol_P:        
#             port()


# def port():
#     symbols = False
#     for i in range(size_i):
#         for j in range(size_j):
#             if mss[i][j] in ('[C]', '[A]', '[D]', '[H]','[E]'):    
#                 symbols = True
#                 print('Symbols found')
#                 break
#         if symbols:
#             break

#     if not symbols:
#         print('Symbols not found')
#         use_port()

# def use_port():        
#     while True:
#         rand_p = random.randint(0, size_i - 1)
#         rand_l = random.randint(0, size_j - 1)
#         if mss[rand_p][rand_l] == '[_]':
#           mss[rand_p][rand_l] = '[P]'
#           break


# def next_level():
#     print('Next level')
#     level2()
# size_q = 30
# size_w = 30

# def level2():
#     def fill_pole2():
#         mss.clear()
#         for q in range(size_q):
#             row = []
#             for w in range(size_w):
#                 if random.random() < 0.3:
#                     row.append('██')
#                 else:
#                     row.append('░░')
#             mss.append(row)

#     def show_pole2():
#         for q in range(size_q):
#             for w in range(size_w):
#                 if start_user[0] == q and start_user[1] == w:
#                     print('웃', end=' ')
#                 else:    
#                     print(mss[q][w], end=' ')
#             print()
#         print()

#     def user2():
#         mss[start_user[0]][start_user[1]] = '웃'
        
#         while True:
            
#             move = input('Enter w,s,a,d or q for exit: ')

#             if move == 'q':
#                 print('Exit game')
#                 break

#             if move == 'w' and start_user[0] > 0:
#                 if mss[start_user[0] - 1][start_user[1]] != '██':
#                     start_user[0] -= 1
#                 else:
#                     print('Invalid move')
#             elif move == 's' and start_user[0] < size_q - 1:
#                 if mss[start_user[0] + 1][start_user[1]] != '██':
#                     start_user[0] += 1
#                 else:
#                     print('Invalid move')
#             elif move == 'a' and start_user[1] > 0:
#                 if mss[start_user[0]][start_user[1] - 1] != '██':
#                     start_user[1] -= 1
#                 else:
#                     print('Invalid move')
#             elif move == 'd' and start_user[1] < size_w - 1:
#                 if mss[start_user[0]][start_user[1] + 1] != '██':
#                     start_user[1] += 1
#                 else:
#                     print('Invalid move')
#             else:
#                 print('Invalid move')
#                 continue

#             show_pole2()

#             cell = mss[start_user[0]][start_user[1]]

#             if cell == '░░':
#                 mss[start_user[0]][start_user[1]] = '░░'

#             elif cell == '██':
#                 mss[start_user[0]][start_user[1]] = '██'
            
#             elif cell == '-𖦹':
#                 level2()

#     def use_port2():        
#         while True:
#             rand_p = random.randint(0, size_q - 1)
#             rand_l = random.randint(0, size_w - 1)
#             if mss[rand_p][rand_l] == '░░':
#               mss[rand_p][rand_l] = '-𖦹'
#               break

#     fill_pole2()
#     use_port2()
#     show_pole2()
#     user2()
# #level2()    
# fill_pole()
# fill_items()
# user()

# #===========================================================================
# import random

# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)

# def fill_cards_players(player, deck, count_cards):
#   for i in range(count_cards):
#     tmp_cards = random.choice(deck)
#     player.append(tmp_cards)
#     deck.remove(tmp_cards)

# def user_hod(player, table):
#   print('user_hod')
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         break
#   else:
#     print('no cards user')

# def bot_hod(player, table):
#   print('bot hod')
#   if len(player) > 0:
#     tmp = random.choice(player)
#     table.append(tmp)
#     player.remove(tmp)

# user = []
# bot1 = []
# bot2 = []
# bot3 = []

# def dop_cards(player, players, deck):
#     if len(player) < 6 and len(deck) > 0:
        
#         for player in players:
#             dop_card = random.choice(deck)
#             player.append(dop_card)
#             deck.remove(dop_card)
#             print('dop card:', dop_card)

#     else:
#         print('no cards or enough cards')

#     if len(player) == 0:
#         print('no users cards ')
#         exit()

# meaning = ['6','7','8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']

# deck = []
# table = []
# players = [user, bot1, bot2, bot3]

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# kozir = random.choice(suit)
# kozirs = []
# print('trump:', kozir)

# def kozir_power( kozir, player, players, kozirs):
#     for player in players:
#         count = 0
#         for card in player:
#             if kozir in card:
#                 count += 1
#                 kozirs.append(card)
#         print('Player', players.index(player)+1, '=',count) 
#     print('All kozirs', kozirs)

#     if len(kozirs) == 0:
#         print('no kozirs')
    
# def find_min_trump(symbol_trump, meaning, kozirs):
#   tmp_mss = []
#   tmp_mss_index = []
#   tmp_res = ''
#   for item in kozirs:
#     if symbol_trump == item[0]:
#       tmp_mss.append(item)

#   if len(tmp_mss) > 0:
#     for i in tmp_mss:
#       for j in range(len(meaning)):
#         if i[1] == meaning[j]:
#           tmp_mss_index.append(j)

#   if len(tmp_mss_index) > 0:
#     tmp_mss_index.sort()
#     tmp_res = symbol_trump + meaning[tmp_mss_index[0]]

#   if tmp_res != None:
#     return tmp_res
  
# fill_cards_players(user, deck, 6)
# fill_cards_players(bot1, deck, 6)
# fill_cards_players(bot2, deck, 6)
# fill_cards_players(bot3, deck, 6)
# kozir_power(kozir, user, players, kozirs)

# a = find_min_trump(kozir, meaning, kozirs)
# print('Min kozir ', a)

# def first_hod(player):
  
#   for player in players:
#     for card in player:
#         if card == a: 
#             print('First hod', players.index(player)+1, 'a', a)
#             break

#   who_hod(player)

# def who_hod(player):
#   print('who_hod')
#   if players.index(player) == 0:
#     user_hod(user, table)
#   elif players.index(player) == 1:
#     bot_hod(bot1, table)
#   elif players.index(player) == 2:
#     bot_hod(bot2, table)
#   elif players.index(player) == 3:
#     bot_hod(bot3, table) 
      
# # while True:
# print('user:', user)
# print('bot1:', bot1)
# print('bot2:', bot2)
# print('bot3:', bot3)

# print('table:', table)

# first_hod(user)

# # user_hod(user, table)
# # bot_hod(bot1, table)
# # bot_hod(bot2, table)
# # bot_hod(bot3, table)
# # who_hod(bot1)
# # dop_cards(user, players, deck)  




#===========================================================================

# import random


# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)


# def fill_cards_players(player, deck, count_cards):
#   for i in range(count_cards):
#     tmp_cards = random.choice(deck)
#     player.append(tmp_cards)
#     deck.remove(tmp_cards)


# def user_hod(player, table):
#   print('user_hod')
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         break
#   else:
#     print('no cards user')


# def bot_hod(player, table):
#   print('bot hod')
#   if len(player) > 0:
#     tmp = random.choice(player)
#     table.append(tmp)
#     player.remove(tmp)
#     print('bot card:', tmp)


# user = []
# bot1 = []
# bot2 = []
# bot3 = []


# def dop_cards(player, players, deck):
#   if len(player) < 6 and len(deck) > 0:
#     for player in players:
#       dop_card = random.choice(deck)
#       player.append(dop_card)
#       deck.remove(dop_card)
#       print('dop card:', dop_card)

#   else:
#     print('no cards or enough cards')

#   if len(player) == 0:
#     print('no users cards ')
#     exit()


# meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']

# deck = []
# table = []
# players = [user, bot1, bot2, bot3]
# max_card = []

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# kozir = random.choice(suit)
# kozirs = []
# print('trump:', kozir)


# def kozir_power(kozir, player, players, kozirs):
#   for player in players:
#     count = 0
#     for card in player:
#       if kozir in card:
#         count += 1
#         kozirs.append(card)
#     print('Player', players.index(player) + 1, '=', count)
#   print('All kozirs', kozirs)

#   if len(kozirs) == 0:
#     print('no kozirs')


# def find_min_trump(symbol_trump, meaning, kozirs):
#   tmp_mss = []
#   tmp_mss_index = []
#   tmp_res = ''
#   for item in kozirs:
#     if symbol_trump == item[0]:
#       tmp_mss.append(item)

#   if len(tmp_mss) > 0:
#     for i in tmp_mss:
#       for j in range(len(meaning)):
#         if i[1] == meaning[j]:
#           tmp_mss_index.append(j)

#   if len(tmp_mss_index) > 0:
#     tmp_mss_index.sort()
#     tmp_res = symbol_trump + meaning[tmp_mss_index[0]]

#   if tmp_res != None:
#     return tmp_res

# def fight(table, players, max_card):
#   #print('fight')
#   print('table:', table)
#   if len(table) == 4:
#     for player in players:
#       for card in player:
#         if table[0][0] in card:
#           find_max_card(table, meaning)
#           break
#   else:
#     print('no fight')

# def find_max_card(table, meaning):
#   best_card = None
#   best_index = -1

#   for card in table:
#     if isinstance(card, str):
#       value = card[1:]
#     elif isinstance(card,(list,tuple)):
#       value = card[1]
#     else:
#       continue

#     if value in meaning:
#       idx = meaning.index(value)
#       if idx > best_index:
#         best_index = idx
#         best_card = card
#   return best_card

# deck_otboi = []

# def otboi(table, deck_otboi):
#   for card in table:
#     deck_otboi.append(card)

#   table.clear()
#   print('otboi', deck_otboi)
#   return deck_otboi



# fill_cards_players(user, deck, 6)
# fill_cards_players(bot1, deck, 6)
# fill_cards_players(bot2, deck, 6)
# fill_cards_players(bot3, deck, 6)
# kozir_power(kozir, user, players, kozirs)

# a = find_min_trump(kozir, meaning, kozirs)
# print('Min kozir ', a)

# for player in players:
#   for card in player:
#     if a in card:
#       first_player = player
#       break
#   else:
#     continue
#   break


# def who_hod(player):
#   #print('who_hod')
#   if players.index(player) == 0:
#     user_hod(user, table)
#   elif players.index(player) == 1:
#     bot_hod(bot1, table)
#   elif players.index(player) == 2:
#     bot_hod(bot2, table)
#   elif players.index(player) == 3:
#     bot_hod(bot3, table)


# def first_hod(player):
#   for player in players:
#     for card in player:
#       if a in card:
#         print('First hod', players.index(player) + 1)
#         who_hod(player)
#         return



# while True:
#   print('user:', user)
#   print('bot1:', bot1)
#   print('bot2:', bot2)
#   print('bot3:', bot3)
#   print('table:', table)

#   first_hod(first_player)
#   if first_player == user:
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
#   elif first_player == bot1:
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
#     user_hod(user, table)
#   elif first_player == bot2:
#     bot_hod(bot3, table)
#     user_hod(user, table)
#     bot_hod(bot1, table)
#   elif first_player == bot3:
#     user_hod(user, table)
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)

#   # user_hod(user, table)
#   # bot_hod(bot1, table)
#   # bot_hod(bot2, table)
#   # bot_hod(bot3, table)
#   fight(table, players, max_card)
#   b = find_max_card(table, meaning)
#   print('Max card', b)
#   otboi(table, deck_otboi)
#   dop_cards(user, players, deck)

#===========================================================================

# person = {
#   'name': 'qwerty',
#   'age' : 25,
#   'name1': 'qwerty2',
# }

# print(person)
# # print(person['name'])
# # print(person['age'])
# print('=====')
# # print(person['qwerty'])
# # print(person['name'])
# person['name'] = 'poni'
# # print(person['name'])
# print('=====')
# person['city'] = 'Dnipro'
# print(person)
# print('=====')
# del person['name1']
# print(person)

# for jsdhvfjds, sdfklskdfs in person.items():
#     print(f'{jsdhvfjds}: {sdfklskdfs}')

# print(person.keys())
# print(person.values())


# print(person.get('asd', 'error keys'))

#===========================================================================
# user_dict = {}

# while True:

#   def onekey(user_key, user_dict):
#     return user_key not in user_dict
  
#   user_key = input('Enter key or exit: ')
#   if user_key == 'exit':
#     print('Exit')
#     print(user_dict)
#     break
#   user_value = input('Enter value: ')
  
#   if onekey(user_key, user_dict):
#     user_dict[user_key] = user_value
#     print('Key added')
#   else:
#     print('Error. Key already exists')
  
  
#   print(user_dict)

# while True:

#   user_go = input('Would you like to delete or change a key? Delete - enter 1, cange - enter 2 or 3 for add a new key: ')
#   if user_go == '1' or user_go == '2' or user_go == '3':
#     print('Ok')
#   else:
#     print('Error. Enter 1, 2 or 3')
#     break
#   user_keyEnter = input('Enter key for editing or end for exit: ')
#   if user_keyEnter == 'end':
#     print('End')
#     print(user_dict)
#     break
  
#   if user_go == '1':
#     if user_keyEnter in user_dict:
#       del user_dict[user_keyEnter]
#       print('Key deleted')
#       print(user_dict)
#     else:
#       print('Error. Key not found')
    
#   elif user_go == '2':
#     if user_keyEnter in user_dict:
#       user_valueEnter = input('Enter new element: ')
#       user_dict[user_keyEnter] = user_valueEnter
#       print('Key changed')
#       print(user_dict)
#     else:
#       print('Error. Key not found')

#   elif user_go == '3':
#     if onekey(user_keyEnter, user_dict):
#       user_valueEnter = input('Enter new element: ')
#       user_dict[user_keyEnter] = user_valueEnter
#       print('Key added')
#       print(user_dict)
#     else:
#       print('Error. Key not found')
#===========================================================================

# import random

# user_size_i = int(input('user_size_i: '))
# user_size_j = int(input('user_size_j: '))

# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# pole = []

# fill_pole(pole, user_size_i, user_size_j)
# show_pole(pole, user_size_i, user_size_j)

# def user_step():
#          user1 = input('user1: ')
#          user2 = input('user2: ')

#          if user1.isdigit and user2.isdigit():
#             user1 = int(user1) - 1
#             user2 = int(user2) - 1
#          else:
#             print('Error')
#             exit()

#          if pole[int(user1)][int(user2)] == '[_]':
#              pole[int(user1)][int(user2)] = '[X]'
#          else:
#              print('Error')

#          fill_pole(pole, user_size_i, user_size_j)
#          show_pole(pole, user_size_i, user_size_j)

# def bot_step():
#   while True:
#       bot1 = random.randint(0, user_size_i - 1)
#       bot2 = random.randint(0, user_size_j - 1)

#       if pole[bot1][bot2] == '[_]':
#           pole[bot1][bot2] = '[O]'
#           break

# symbol = ['[X]', '[O]']

# def player_win():
#     for i in range (user_size_i):
#         if pole[i][0] == pole[i][1] == pole[i][2] and pole[i][0] in symbol:
#             print('Player win horizontal')
#             exit()

#     for i in range (user_size_j):
#         if pole[0][i] == pole[1][i] == pole[2][i] and pole[0][i] in symbol:
#             print('Player win vertical')
#             exit()

#     if pole[0][0] == pole[1][1] == pole[2][2] and pole[0][0]  in symbol:
#         print('Player win diagonal')
#         exit()
#     elif pole[0][2] == pole[1][1] == pole[2][0] and pole[0][2] in symbol:
#         print('Player win diagonal')
#         exit()

# def nothing():
#     for j in range (user_size_j):
#         for i in range (user_size_i):
#             if pole[i][j] == '[_]':
#                 return
#     print('Nothing')
#     exit()

# while True:
#     user_step()
#     bot_step()
#     player_win()
#     nothing()

# def fill_pole(pole, size_i, size_j):
# for i in range(size_i):
#     pole.append([])
#     for j in range(size_j):
#         pole[i].append('[_]')


# def show_pole(pole, size_i, size_j):
#   for i in range(size_i):
#       for j in range(size_j):
#           print(pole[i][j], ' ' ,end=" ")
#       print()

# def check_win(pole, symbol):
#   win = {
#       "l1": [pole[0][0], pole[0][1], pole[0][2]],
#       "l2": [pole[1][0], pole[1][1], pole[1][2]],
#       "l3": [pole[2][0], pole[2][1], pole[2][2]],

#       "l4": [pole[0][0], pole[1][0], pole[2][0]],
#       "l5": [pole[0][1], pole[1][1], pole[2][1]],
#       "l6": [pole[0][2], pole[1][2], pole[2][2]],

#       "l7": [pole[0][0], pole[1][1], pole[2][2]],
#       "l8": [pole[0][2], pole[1][1], pole[2][0]],
#   }

#   for line in win.values():
#       if line[0] == line[1] == line[2] == symbol:
#           return True
#   return False

# pole = []
# size_i, size_j = 3, 3
# symbol = '[X]'

# fill_pole(pole, size_i, size_j)

# pole[0][0] = symbol
# pole[1][1] = symbol
# pole[2][2] = symbol

# show_pole(pole, size_i, size_j)

# if check_win(pole, symbol):
#   print("WIN X!")

# di = {
#     'l1':[mss[0][0],mss[0][1],mss[0][2]],
#     'l2':[mss[1][0],mss[1][1],mss[1][2]],
#     'l3':[mss[2][0],mss[2][1],mss[2][2]],
# }

# print(di)

# mss[0][0] = '[X]'
# mss[1][0] = '[X]'
# mss[2][0] = '[X]'


# import random

# mss = []

# user_size_i = int(input('user_size_i: '))
# user_size_j = int(input('user_size_j: '))

# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# def user_step():
#          user1 = input('user1: ')
#          user2 = input('user2: ')

#          if user1.isdigit and user2.isdigit():
#             user1 = int(user1) - 1
#             user2 = int(user2) - 1
#          else:
#             print('Error')
#             exit()

#          if pole[int(user1)][int(user2)] == '[_]':
#              pole[int(user1)][int(user2)] = '[X]'
#          else:
#              print('Error')

#          fill_pole(pole, user_size_i, user_size_j)
#          show_pole(pole, user_size_i, user_size_j)

# def bot_step():
#   while True:
#       bot1 = random.randint(0, user_size_i - 1)
#       bot2 = random.randint(0, user_size_j - 1)

#       if pole[bot1][bot2] == '[_]':
#           pole[bot1][bot2] = '[O]'
#           break

# def diagram(mss, i, j):

#     horiz = {'h1':[mss[i][j],mss[i][j+1],mss[i][j+2]],
#             'h2':[mss[i+1][j],mss[i+1][j+1],mss[i+1][j+2]],
#             'h3':[mss[i+2][j],mss[i+2][j+1],mss[i+2][j+2]]
#     }
#     vert = {'v1':[mss[i][j],mss[i+1][j],mss[i+2][j]],
#             'v2':[mss[i][j+1],mss[i+1][j+1],mss[i+2][j+1]],
#             'v3':[mss[i][j+2],mss[i+1][j+2],mss[i+2][j+2]]
#     }
#     di = {
#         'd1':[mss[i][j],mss[i+1][j+1],mss[i+2][j+2]],
#         'd2':[mss[i+2][j],mss[i+1][j+1],mss[i][j+2]],
#     }
#     return horiz, vert, di

# def win_player(horiz, vert, di):

#     for line in horiz.values():
#         if line.count('[X]') == 3:
#             print('Player win horizontal')
#             exit()
#         elif line.count('[O]') == 3:
#             print('Bot win horizontal')
#             exit()    
    
#     for line in vert.values():
#         if line.count('[X]') == 3:
#             print('Player win vertical')
#             exit()
#         elif line.count('[O]') == 3:
#             print('Bot win vertical')
#             exit()  

#     for line in di.values():
#         if line.count('[X]') == 3:
#             print('Player win diagonal')
#             exit()
#         elif line.count('[O]') == 3:
#             print('Bot win diagonal')
#             exit()          


# pole = []

# fill_pole(pole, user_size_i, user_size_j)
# show_pole(pole, user_size_i, user_size_j)

# while True:
#     user_step()
#     bot_step()
    
#     horiz, vert, di = diagram(pole, 0 , 0)
#     win_player(horiz, vert, di)
    
# print(di)

# mss[0][0] = '[X]'
# mss[1][0] = '[X]'
# mss[2][0] = '[X]'
#=========================================
#===========================(tuple)
# point = (10,20)
# print(point)
#
# # print(type(point))
# print(point[0])
#
# x, y = point
# print(x,y)
#===========================(set)

# nums = {1,2,3,4,3,2, 5}
# print(nums)
#
# nums.add(6)
# print(nums)
# nums.add(1)
# print(nums)
#
# nums.remove(1)
# print(nums)

# nums1 = {1,2,3}
# nums2 = {3,4,5}

# print(nums1, nums2)
# print(nums1 | nums2)
# print(nums1 & nums2)
# print(nums1 ^ nums2)
# print(nums1 - nums2)

# nums1 = (1,2,3)
# z,x,c, = nums1
# nums2 = (4,5,6)
# q,w,e = nums2
# p = 10
# nums3 = (z,x,q,w,e,p)


# print(nums3)
#nums3.remove(3)
#print(nums1 & nums2)
#nums3.add(10)
#print(nums1 ^ nums2)
#print(nums3)
#print(nums1 - nums2)

# user_number = int(input('trsjt?: '))
# # if user_number.isdigit:
# #     user_number = int(user_number)

# if user_number in nums3:
#     print('OK')
# else:
#     print('not ok')    
# nums4 = (0,1,1,2,3,5,8,13,21,34,55,89)
# alp = ['a','s','d','r','t','y','u','i']
# qwe = []
# x = 2

# while len(alp) != len(nums4):
#     if len(alp) > len(nums4):
#         alp.pop()
#     else:
#         alp.append(alp[-1] + str(x))
#         x += 1
# print('ok')
          

# for i in range(len(alp)):
#     print(alp[i], '=', nums4[i])  
  
 
# user = input('Enter word: ')
# word = set(user)  

# print(word)    
#===================================================
# import random

# mss = []

# user_size_i = int(input('user_size_i: '))
# user_size_j = int(input('user_size_j: '))

# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')

# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# def user_step():
#          user1 = input('user1: ')
#          user2 = input('user2: ')

#          if user1.isdigit and user2.isdigit():
#             user1 = int(user1) - 1
#             user2 = int(user2) - 1
#          else:
#             print('Error')
#             exit()

#          if pole[int(user1)][int(user2)] == '[_]':
#              pole[int(user1)][int(user2)] = '[X]'
#          else:
#              print('Error')


# def bot_step():
#   while True:
#       bot1 = random.randint(0, user_size_i - 1)
#       bot2 = random.randint(0, user_size_j - 1)

#       if pole[bot1][bot2] == '[_]':
#           pole[bot1][bot2] = '[O]'
#           show_pole(pole, user_size_i, user_size_j)
#           break
            

# def diagram(mss, i, j):
#     horiz = (
#         (mss[i][j],mss[i][j+1],mss[i][j+2]),
#         (mss[i+1][j],mss[i+1][j+1],mss[i+1][j+2]),
#         (mss[i+2][j],mss[i+2][j+1],mss[i+2][j+2])
#     )
    
#     vert = (
#         (mss[i][j],mss[i+1][j],mss[i+2][j]),
#         (mss[i][j+1],mss[i+1][j+1],mss[i+2][j+1]),
#         (mss[i][j+2],mss[i+1][j+2],mss[i+2][j+2])
#     )
    
#     di = (
#         (mss[i][j],mss[i+1][j+1],mss[i+2][j+2]),
#         (mss[i+2][j],mss[i+1][j+1],mss[i][j+2])
#         )
    
#     return horiz, vert, di

# def win_player(horiz, vert, di):

#     win_user = ('[X]','[X]','[X]')   
#     win_bot = ('[O]','[O]','[O]') 

#     for line in horiz + vert + di:
#         if line == win_user:
#             print('Player win')
#             exit()
#         elif line == win_bot:
#             print('Bot win')
#             exit()


# pole = []

# fill_pole(pole, user_size_i, user_size_j)
# show_pole(pole, user_size_i, user_size_j)

# while True:
#     user_step()
#     bot_step()
    
#     horiz, vert, di = diagram(pole, 0 , 0)
#     win_player(horiz, vert, di)
#===============================================
# import random

# user_chests = []
# bot1_chests = []
# bot2_chests = []
# bot3_chests = []

# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)


# def fill_cards_players(player, deck, count_cards):
#   for i in range(count_cards):
#     tmp_cards = random.choice(deck)
#     player.append(tmp_cards)
#     deck.remove(tmp_cards)

# def user_hod(player, table):
#   print('All cards: ', deck)

#   if len(player) == 0:
#     print('you dont have cards')
#     return
#   while True:
#     contr = input('У кого угадываем карту? bot1, bot2, bot3:')
#     user = input('Какая карта?:')

#     if contr == 'bot1':
#       contr = bot1
#     elif contr == 'bot2':
#       contr = bot2
#     elif contr == 'bot3':
#       contr = bot3   
#     else:
#       print('Бот не найден')   

#     if user in contr:
#       player.append(user)
#       contr.remove(user)
#       table.append(user)
#       print(table)
#     else:
#       print('dont has this card')
#       break

# def bot_hod(player, next_player, table, deck):
#   if len(player) == 0:
#     print('bot no cards')
#     return
#   tmp = random.choice(deck)
#   print('bot card:', tmp)
#   if tmp in next_player:
#     player.append(tmp)
#     bot2.remove(tmp)
#     table.append(tmp)
#     print(table)
#     bot_hod(player, table, deck)
#   else:
#     print('dont has this card')

# def dop_cards(player, players, deck):
#   if len(player) == 0:
#     return
#   if len(player) < 4 and len(deck) > 0:
#     dop_card = random.choice(deck)
#     player.append(dop_card)
#     deck.remove(dop_card)
#     print('dop card:', dop_card)
#   else:
#     print('no cards or enough cards')

# def cycle():    
#   for pl in players:
#         dop_cards(pl, players, deck)
#   print('user:', user)
#   print('bot1:', bot1)
#   print('bot2:', bot2)
#   print('bot3:', bot3)
#   print('table:', table)
#   check_chests(user, 'User', user_chests)
#   check_chests(bot1, 'Bot1', bot1_chests)
#   check_chests(bot2, 'Bot2', bot2_chests)
#   check_chests(bot3, 'Bot3', bot3_chests)

# def who_hod():

#   print('user:', user)
#   print('bot1:', bot1)
#   print('bot2:', bot2)
#   print('bot3:', bot3)

#   pl_hod = random.randint(0,3)
#   print(pl_hod)

#   if pl_hod == 0:
#     while True:
#       user_hod(user, table)
#       bot_hod(bot1, bot2, table, deck)
#       bot_hod(bot2, bot3, table, deck)
#       bot_hod(bot3, user, table, deck)
#       cycle()

#   elif pl_hod == 1:
#     while True:
#       bot_hod(bot1, bot2, table, deck)
#       bot_hod(bot2, bot3, table, deck)
#       bot_hod(bot3, user, table, deck)
#       user_hod(user, table)
#       cycle()

#   elif pl_hod == 2:
#     while True:
#       bot_hod(bot2, bot3, table, deck)
#       bot_hod(bot3, user, table, deck)
#       user_hod(user, table)
#       bot_hod(bot1, bot2, table, deck)
#       cycle()
    
#   elif pl_hod == 3:
#     while True:
#       bot_hod(bot3, user, table, deck)
#       user_hod(user, table)
#       bot_hod(bot1, bot2, table, deck)
#       bot_hod(bot2, bot3, table, deck)
#       cycle()

# def check_chests(player, player_name, table_chests):
#   meanings = {}

#   for card in player:
#     value = card[1:]
#     if value not in meanings:
#       meanings[value] = []
#     meanings[value].append(card)

#   for value, cards in meanings.items():
#     if len(cards) == 4:
#       print('{player_name} собрал набор из четырех {value}')
#       table_chests.append(cards)
#       for c in cards:
#         if c in player:
#           player.remove(c)          



        
# user = []
# bot1 = []
# bot2 = []
# bot3 = []

# meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']

# deck = []
# table = []
# players = [user, bot1, bot2, bot3]
# max_card = []

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# fill_cards_players(user, deck, 4)
# fill_cards_players(bot1, deck, 4)
# fill_cards_players(bot2, deck, 4)
# fill_cards_players(bot3, deck, 4)

# who_hod()  
#=====================================================================
#while True:

  # print('user:', user)
  # print('bot1:', bot1)
  # print('bot2:', bot2)
  # print('bot3:', bot3)
  # print('table:', table)
#who_hod()  
  # user_hod(user, table)
  # bot_hod(bot1, bot2, table, deck)
  # bot_hod(bot2, bot3, table, deck)
  # bot_hod(bot3, user, table, deck)

  # for pl in players:
  #   dop_cards(pl, players, deck)

# def user_hod(player, table):
#   print('user_hod')
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         break
#   else:
#     print('no cards user')


# def bot_hod(player, table):
#   print('bot hod')
#   if len(player) > 0:
#     tmp = random.choice(player)
#     table.append(tmp)
#     player.remove(tmp)
#     print('bot card:', tmp)




# def dop_cards(player, players, deck):
#   if len(player) < 6 and len(deck) > 0:
#     for player in players:
#       dop_card = random.choice(deck)
#       player.append(dop_card)
#       deck.remove(dop_card)
#       print('dop card:', dop_card)

#   else:
#     print('no cards or enough cards')

#   if len(player) == 0:
#     print('no users cards ')
#     exit()




# kozir = random.choice(suit)
# kozirs = []
# print('trump:', kozir)


# def kozir_power(kozir, player, players, kozirs):
#   for player in players:
#     count = 0
#     for card in player:
#       if kozir in card:
#         count += 1
#         kozirs.append(card)
#     print('Player', players.index(player) + 1, '=', count)
#   print('All kozirs', kozirs)

#   if len(kozirs) == 0:
#     print('no kozirs')


# def find_min_trump(symbol_trump, meaning, kozirs):
#   tmp_mss = []
#   tmp_mss_index = []
#   tmp_res = ''
#   for item in kozirs:
#     if symbol_trump == item[0]:
#       tmp_mss.append(item)

#   if len(tmp_mss) > 0:
#     for i in tmp_mss:
#       for j in range(len(meaning)):
#         if i[1] == meaning[j]:
#           tmp_mss_index.append(j)

#   if len(tmp_mss_index) > 0:
#     tmp_mss_index.sort()
#     tmp_res = symbol_trump + meaning[tmp_mss_index[0]]

#   if tmp_res != None:
#     return tmp_res

# def fight(table, players, max_card):
#   #print('fight')
#   print('table:', table)
#   if len(table) == 4:
#     for player in players:
#       for card in player:
#         if table[0][0] in card:
#           find_max_card(table, meaning)
#           break
#   else:
#     print('no fight')

# def find_max_card(table, meaning):
#   best_card = None
#   best_index = -1

#   for card in table:
#     if isinstance(card, str):
#       value = card[1:]
#     elif isinstance(card,(list,tuple)):
#       value = card[1]
#     else:
#       continue

#     if value in meaning:
#       idx = meaning.index(value)
#       if idx > best_index:
#         best_index = idx
#         best_card = card
#   return best_card

# deck_otboi = []

# def otboi(table, deck_otboi):
#   for card in table:
#     deck_otboi.append(card)

#   table.clear()
#   print('otboi', deck_otboi)
#   return deck_otboi




# kozir_power(kozir, user, players, kozirs)

# a = find_min_trump(kozir, meaning, kozirs)
# print('Min kozir ', a)

# for player in players:
#   for card in player:
#     if a in card:
#       first_player = player
#       break
#   else:
#     continue
#   break




# def who_hod(player):
#   #print('who_hod')
#   if players.index(player) == 0:
#     user_hod(user, table)
#   elif players.index(player) == 1:
#     bot_hod(bot1, table)
#   elif players.index(player) == 2:
#     bot_hod(bot2, table)
#   elif players.index(player) == 3:
#     bot_hod(bot3, table)


# def first_hod(player):
#   for player in players:
#     for card in player:
#       if a in card:
#         print('First hod', players.index(player) + 1)
#         who_hod(player)
#         return



#while True:




#   first_hod(first_player)
#   if first_player == user:
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
#   elif first_player == bot1:
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
#     user_hod(user, table)
#   elif first_player == bot2:
#     bot_hod(bot3, table)
#     user_hod(user, table)
#     bot_hod(bot1, table)
#   elif first_player == bot3:
#     user_hod(user, table)
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)

#   # user_hod(user, table)
#   # bot_hod(bot1, table)
#   # bot_hod(bot2, table)
#   # bot_hod(bot3, table)
#   fight(table, players, max_card)
#   b = find_max_card(table, meaning)
#   print('Max card', b)
#   otboi(table, deck_otboi)
#   dop_cards(user, players, deck)

#==========================================================================29.10

# file = open('t.txt', 'r' )
# text_file = file.read()
# print(text_file)
# file.close()

# with open('t.txt', 'r') as file:
#     text_file = file.read()
#     print(text_file)

# file = open('t.txt', 'w' )
# file.write("Hello World")
# file.write("\nHello World")
# file.write("\nHello World")
# file.write("\nHello World")
# file.close()

# with open('t.txt', 'w') as file:
#     file.write('Hello World1')
#     file.write('\nHello World1')
#
# with open('t.txt', 'w') as file:
#     file.write('Hello World2')
#     file.write('\nHello World2')


# with open('t.txt', 'a') as file:
#     file.write('Hello World1')
#     file.write('\nHello World1')
#===================================
# with open('log.txt', 'w') as file:
#   file.write('User actions: ' + '\n') 

# while True:  

#   first = int(input('Enter first number: '))
#   user_znak = input('Enter znak or end for exit: ')

#   if user_znak == 'end':
#      print('Exit')  
#      with open('log.txt', 'r') as file:
#       text_file = file.read()
#       print(text_file)
#       exit()

#   second = int(input('Enter second number: '))

#   if user_znak == '+':
#       print('first + second = : ', first + second)
#   elif user_znak == '-':
#       print('first - second = : ', first - second)
#   elif user_znak == '*':
#       print('first * second = : ', first * second)
#   elif user_znak == '/' and second != 0:
#       print('first / second = : ', first / second)
#   else :
#     print('Error')
#     with open('log.txt', 'a') as file:
#        file.write('\nError'+ '\n')

#   with open('log.txt', 'a') as file:
#     first = str(first)
#     second = str(second)
#     file.write(first + '\n')
#     file.write(user_znak + '\n')
#     file.write(second + '\n')
#================================
  


# while True:
#   user = input('Enter text or end for exit: ')

#   with open('t.txt', 'a') as file:
#     file.write(user + '\n')

#   if user == 'end':
#     with open('t.txt', 'r') as file:
#       text_file = file.read()
#       print(text_file)
#       exit()  

#===============================================
  
# import random
 
# save_mss = []
  
# def fill_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         mss.append([])
#         for j in range(size_j):
#             mss[i].append('[_]')
#     save_mss.append(mss)
 
# def show_pole(mss, size_i, size_j):
#     for i in range(size_i):
#         for j in range(size_j):
#             print(mss[i][j], ' ', end='')
#         print()

# def save_f(mss):
#   with open('save.txt', 'w') as file:
#     for row in pole:
#       file.write(''.join(row) + '\n')     

# def dload_game():         
#   with open('save.txt', 'r') as file:
#     lines = file.readlines()

#   pole = []
#   for line in lines:
#      cells = [cell + ']' for cell in line.split(']') if cell.strip() != '']
#      pole.append(cells)
#   return pole     
  
# def user_step():
#   user1 = input('user1. Enter 0 for exit: ')
 
#   if user1 == '0':
#     save_f(save_mss)
#     exit()
 
#   user2 = input('user2: ')
 
#   if user1.isdigit() and user2.isdigit():
#     user1 = int(user1) - 1
#     user2 = int(user2) - 1
#   else:
#     print('Error')
#     exit()
 
#   if pole[int(user1)][int(user2)] == '[_]':
#       pole[int(user1)][int(user2)] = '[X]'
#   else:
#       print('Error')
 
 
# def bot_step():
#   while True:
#       bot1 = random.randint(0, user_size_i - 1)
#       bot2 = random.randint(0, user_size_j - 1)
 
#       if pole[bot1][bot2] == '[_]':
#           pole[bot1][bot2] = '[O]'
#           show_pole(pole, user_size_i, user_size_j)
#           break
           
 
# def diagram(mss, i, j):
#     horiz = (
#         (mss[i][j],mss[i][j+1],mss[i][j+2]),
#         (mss[i+1][j],mss[i+1][j+1],mss[i+1][j+2]),
#         (mss[i+2][j],mss[i+2][j+1],mss[i+2][j+2])
#     )
   
#     vert = (
#         (mss[i][j],mss[i+1][j],mss[i+2][j]),
#         (mss[i][j+1],mss[i+1][j+1],mss[i+2][j+1]),
#         (mss[i][j+2],mss[i+1][j+2],mss[i+2][j+2])
#     )
   
#     di = (
#         (mss[i][j],mss[i+1][j+1],mss[i+2][j+2]),
#         (mss[i+2][j],mss[i+1][j+1],mss[i][j+2])
#         )
   
#     return horiz, vert, di
 
# def win_player(horiz, vert, di):
 
#     win_user = ('[X]','[X]','[X]')  
#     win_bot = ('[O]','[O]','[O]')
 
#     for line in horiz + vert + di:
#         if line == win_user:
#             print('Player win')
#             exit()
#         elif line == win_bot:
#             print('Bot win')
#             exit()
 
# def game_cycle():
#   while True:
#       user_step()
#       bot_step()
      
#       horiz, vert, di = diagram(pole, 0 , 0)
#       win_player(horiz, vert, di)  

# user_size_i = int(input('user_size_i or 777 for download game: '))
 
# if user_size_i == 777:
#   pole = dload_game()
#   user_size_i = len(pole)
#   user_size_j = len(pole[0])
#   show_pole(pole, user_size_i, user_size_j)
#   game_cycle() 
# else:
#   user_size_j = int(input('user_size_j: '))
#   pole = []
 
#   fill_pole(pole, user_size_i, user_size_j)
#   show_pole(pole, user_size_i, user_size_j)
#   game_cycle() 
#===============================================3.11
# def read_file(filename, complete):
#     with open(filename, 'r') as file:
#         complete.append(file.read())

# def primer(obg, mss_primer):
#     tmp = ''
#     for i in range(len(obg[0])):
#         if obg[0][i] != '\n':
#            tmp += obg[0][i]
#         else:
#             mss_primer.append(tmp)
#             tmp = ''
#     mss_primer.append(tmp)


# def search_ch(obj, mss_ch):
#     for i in range(len(obj)):
#         if obj[i] == '+' or obj[i] == '-' or obj[i] == '*' or obj[i] == '/':
#             mss_ch.append(i)

# def add_number(start, stop, obj, mss_num):
#     tmp = ''
#     for i in range(start, stop):
#         tmp += obj[i]
#     mss_num.append(tmp)


# c_file = []
# mss_primer = []
# mss_index_ch = []
# mss_num = []

# read_file('calculator.txt', c_file)
# primer(c_file, mss_primer)

# for i in range(len(mss_primer)):
#     search_ch(mss_primer[i],mss_index_ch)

# for i in range(len(mss_primer)):
#     add_number(0, mss_index_ch[i], mss_primer[i], mss_num)
#     add_number(mss_index_ch[i]+1, len(mss_primer[i]), mss_primer[i], mss_num)


# print(c_file)
# print(mss_primer)
# print(mss_index_ch)
# print(mss_num)

# with open ('calculator.txt', 'r') as file:
#   text_file1 = file.readline()
#   text_file2 = file.readline()
#   text_file3 = file.readline()
#   text_file4 = file.readline()
#   text_file5 = file.readline()
#   print(text_file1)

# while True:
    
#   user = float(input('Enter the response : '))

#   if mss_primer[0][mss_index_ch[0]] == '+' and user == (int(mss_num[0]) + int(mss_num[1])):
#       print('OK')
#       print(text_file2)

#   elif mss_primer[1][mss_index_ch[1]] == '+' and user == (int(mss_num[2]) + int(mss_num[3])):
#       print('OK')
#       print(text_file3)

#   elif mss_primer[2][mss_index_ch[2]] == '*' and user == (int(mss_num[4]) * int(mss_num[5])):
#       print('OK')
#       print(text_file4)

#   elif mss_primer[3][mss_index_ch[3]] == '/' and user == int(mss_num[6]) / int(mss_num[7]):  
#       user == round(user, 2)  
#       print('OK')
#       print(text_file5)

#   elif mss_primer[4][mss_index_ch[4]] == '*' and user == (int(mss_num[8]) * int(mss_num[9])):
#       print('-ALL OK-')        
#       break  

#=================================================================================5.11==-fight of sea-=====

#======================================================================primer.dz.29.11

# import random

# numbers = list(range(-10, 100))
# znaks = ['+', '-', '*', '/']
# primer = []

# user_num = int(input('Сколько примеров выдать?: '))

# if user_num <= 0:
#    print('Error')
#    exit()

# with open('primer.txt', 'w') as file:

#     for i in range(user_num):

#         first, second  = random.choice(numbers), random.choice(numbers)
#         if second == 0:
#            second = random.choice(list(range(1, 100)))
#         znak = random.choice(znaks)

#         example = f"{first}{znak}{second}"
#         file.write(example + '\n')

# #=================        

# with open ('primer.txt', 'r') as file:
#   examples = [line.strip() for line in file.readlines()]

# print('Enter the response :')
# for ex in examples:
#    print(ex)
# print()

# #===============================

# for example in examples:
   
#    while True:
#       user_answer = float(input(f"{example} = " ))
#       correct = round(eval(example), 2)

#       abc = user_answer - correct
#       if abc < 0.01:
#          print('OK')
#          break
#       else:
#          print('>:(((')
#          break

#============================================================================12.11

# x = []
# with open('t.txt', 'r') as file:
#     lines = [line.strip('\n') for line in file]

#     # for line in file:
#     #     x.append(line)

#     #3. x.append(file.readline())

#     # x.append(file.read())
# print(lines)

# with open('q.txt', 'w') as file:
#     for i in lines:
#         # file.write(''.join(i)+'\n')
#         file.write(f'{i}\n')
#============
# from settings_game import fill_pole, show_pole
# from fight_game import user_step, bot_step
# from win_game import win_player, diagram
# from save_and_load_game import save_f, dload_game


# pole = []
# user_size_i = int(input('user_size_i or 777 for download game: '))
# if user_size_i == 777:
#   pole = dload_game()
#   user_size_i = len(pole)
#   user_size_j = len(pole[0])
# elif user_size_i == '0':
#   save_f(pole)
#   exit()  
# else:  
#   user_size_j = int(input('user_size_j: '))

# fill_pole(pole, user_size_i, user_size_j)
# show_pole(pole, user_size_i, user_size_j)



# while True: 
#   user_step(pole)
#   bot_step(pole, user_size_i, user_size_j, show_pole)  
 
#   horiz, vert, di = diagram(pole, 0 , 0) 
#   win_player(horiz, vert, di)
#========================================
# from alpha import random_file
# from clam import clam_word
# from check import check_word

# alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z',
#             'x','c','v','b','n','m']

# random_file(alphabet)

# x = [] 

# while True:
#   user = input('? or 0 for stop: ') 

#   if not user.isdigit():
#       print('error')
#       continue
#   if user == '0':
#     break

#   x.append(int(user)) 

# result = clam_word(x)
# check_word(result)
# if check_word(result) == False:
#    print(result)
      
#==========================
def calc(num):
  try:
      #num = int(input(': '))
      return 10 / num
  except TypeError:
      return 'no number'
  except ZeroDivisionError:
      return 'del 0'
  finally:
      print('ok')

# while True:
#   try:
#     x = int(input('Enter first number or 00 for exit: '))
#     if x == 00:
#        print('Exit')
#        exit()
#     znak = input('Enter znak: ')
#     y = int(input('Enter second number: '))

#     if znak == '-':
#       print(x - y)
#     elif znak == '+':
#       print(x + y)  
#     elif znak == '*':
#       print(x * y)  
#     elif znak == '/':
#       print(x / y)  
#     else:
#       print('Error')  
#   except ValueError:
#       print('no number')
#   except ZeroDivisionError:
#       print('del 0')
#   finally:
#       print('ok')

# def add(a,b):
#   return a+b
# letters = {'o', 'e', 'y', 'u', 'i', 'a' }
# #user = input('Enter a word: ')

# def words(user):

#   if user == '':
#     return 'Error pusto'
     
#   elif user.isdigit():
#     return 'Only letters'
    
#   i = 0

#   while True:
#     for x in user:
#       if x in letters:
#           i += 1
      
#     if i > 0:
#       print('ok', str(i))
#       break
#     else:
#       return 'not ok'  

#   return user

# words(user)