st1 = 'try'
st2 = 'me'
i1 = int(2)
i2 = int(3)
i3 = int(4)
i4 = int(5)
f1 = float(1.5)
f2 = float(2.5)
f3 = float(3.5)


# 15 вариантов сравнения int

print('15 вариантов сравнения int')
print(i1 != i2)
print(i1 < i2)
print(i1 > i2)
print(i1 <= i2)
print(i1 >= i2)
print(i3 != i2)
print(i3 < i2)
print(i3 > i2)
print(i3 <= i2)
print(i3 >= i2)
print(i4 != i2)
print(i4 < i2)
print(i4 > i2)
print(i4 <= i2)
print(i4 >= i2, '\n')


# 9 вариантов сравнения Float

print('9 вариантов сравнения Float')
print(f1 != f2)
print(f1 <= f2)
print(f1 >= f2)
print(f1 < f2)
print(f1 > f2)
print(f1 != f3)
print(f1 <= f3)
print(f1 >= f3)
print(f1 < f3, '\n')


# 10 вариантов сравнения

print('10 вариантов сравнения int (and,or,not')
print(i1 < i2 < i1)
print(i1 < i2 or i1 > i2)
print(i1 == i2 and i1 <= i2)
print(i1 == i2 or i1 <= i2)
print(not i1 < i2)
print(not i2 < i1)
print(not i2 != i1)
print(i3 <= i1 or i3 >= i2)
print(i3 >= i1 or i3 <= i2)
print(i3 != i1 and i3 <= i2, '\n')


# 7) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"

print('Введите целое число')
a = int(input())
b = int(30)
if a < b:
    print('Вы вели число', a, 'которое меньше числа', b)
elif a == b:
    print('Вы вели число', a, 'которое равно числу', b)
else:
    print('Вы вели число', a, 'которое больше числа', b, '\n')

# 8) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"

print('Введите целое число')
yourNumber = int(input())
import random
randomNumber = random.randint(1, 100)
if yourNumber < randomNumber:
    print('Вы вели число', yourNumber, 'которое меньше сгенерированного числа', randomNumber)
elif yourNumber == randomNumber:
    print('Вы вели число', yourNumber, 'которое сгенерированному числу', randomNumber)
else:
    print('Вы вели число', yourNumber, 'которое сгенерированного числа', randomNumber, '\n')


# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно)
#        сгенерированному числу"


print('Введите целое число')
yourN = int(input())
import random
randomNo = random.randint(1, 100)
randomNt = random.randint(1, 100)
answer = 'Вы вели число ' + str(yourN) + ', которое'
if yourN < randomNo:
    answer = answer + ' меньше сгенерированного числа ' + str(randomNo)
elif yourN == randomNo:
    answer = answer + ' равно сгенерированному числу ' + str(randomNo)
else:
    answer = answer + ' больше сгенерированного числа ' + str(randomNo)
if yourN < randomNt:
    answer = answer + ' и меньше сгенерированного числа ' + str(randomNt)
elif yourN == randomNt:
    answer = answer + ' и равно сгенерированному числу ' + str(randomNt)
else:
    answer = answer + ' и больше сгенерированного числа ' + str(randomNt)
print(answer)
