# Предусловие.
# Задачи 3 и 4 выполнить в 2-х вариантах
# 1) В процедурном виде (весь код в одной процедуре).
# 2) В виде функций - код разбит на функции.
# Отдельные функции можно вынести в другие .py файлы и вызывать их в main.py предвварительно импортируя в main.py.
#
#
# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде
#                 Ты ввёл int (Валюта)
#                 конвертированная сумма в USD = int
#     3. Валюту пользователя определите сами.

# while True:
#
#     your_money = int(input('Enter RUB '))
#     USD = your_money / 73.0841
#     EUR = your_money / 86.1150
#     CHF = your_money / 79.3616
#     GBR = your_money / 100.9730
#     CNY = your_money / 11.3230
#
#     print(your_money, 'RUB =', USD, 'USD')
#
#     break

# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде
#                 Ты ввёл int (Валюта)
#                 Конвертированная сумма в USD = int
#                 Конвертированная сумма в EUR = int
#                 Конвертированная сумма в CHF = int
#                 Конвертированная сумма в GBP = int
#                 Конвертированная сумма в CNY = int
#     3. Валюту пользователя определите сами.

# while True:
#
#     your_money = int(input('Enter RUB '))
#     USD = your_money / 73.0841
#     EUR = your_money / 86.1150
#     CHF = your_money / 79.3616
#     GBR = your_money / 100.9730
#     CNY = your_money / 11.3230
#
#     print(your_money, 'RUB =', USD, 'USD')
#     print(your_money, 'RUB =', EUR, 'EUR')
#     print(your_money, 'RUB =', CHF, 'CHF')
#     print(your_money, 'RUB =', GBR, 'GBR')
#     print(your_money, 'RUB =', CNY, 'CNY')
#
#     break

# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде
#                 Ты ввёл int (Валюта)
#                 Конвертированная сумма в USD = int
#                 Конвертированная сумма в EUR = int
#                 Конвертированная сумма в CHF = int
#                 Конвертированная сумма в GBP = int
#                 Конвертированная сумма в CNY = int
#     3. Скипт должен выдать сообщение
#                 Введите положительное число. Если число меньше 0.
#                 Вы ввели не число. Введите число. Если введены буквы.
#                 Вы ввели пустое поле. Введите число. Если введено пустое значение.
#     4. Валюту пользователя определите сами.

# Variant 1

# while True:
#
#     your_money = input('Enter RUB ')
#     try:
#         your_money = int(your_money)
#     except ValueError:
#         print(your_money, 'is not a number. Try again!')
#         continue
#
#     if your_money < 0:
#         print('Enter positive number')
#         continue
#
#     USD = your_money / 73.0841
#     EUR = your_money / 86.1150
#     CHF = your_money / 79.3616
#     GBR = your_money / 100.9730
#     CNY = your_money / 11.3230
#
#     print(your_money, 'RUB =', USD, 'USD')
#     print(your_money, 'RUB =', EUR, 'EUR')
#     print(your_money, 'RUB =', CHF, 'CHF')
#     print(your_money, 'RUB =', GBR, 'GBR')
#     print(your_money, 'RUB =', CNY, 'CNY')
#
#     break

# Variant 2

# currency_to_rate = {'USD': 73.0841, 'EUR': 86.1150, 'CHF': 79.3616, 'GBR': 100.9730, 'CNY': 11.3230}
#
# def main():
#     money = input_money()
#     print(money, 'RUB =', exchange_ym(money, 'USD'), 'USD')
#     print(money, 'RUB =', exchange_ym(money, 'EUR'), 'EUR')
#     print(money, 'RUB =', exchange_ym(money, 'CHF'), 'CHF')
#     print(money, 'RUB =', exchange_ym(money, 'GBR'), 'GBR')
#     print(money, 'RUB =', exchange_ym(money, 'CNY'), 'CNY')
#
#
# def input_money():
#     while True:
#         your_money = input('Enter RUB ')
#
#         try:
#             your_money = int(your_money)
#         except ValueError:
#             print(your_money, 'is not a number. Try again!')
#             continue
#
#         if your_money < 0:
#             print('Enter positive number')
#             continue
#
#         return your_money
#
#
# def exchange_ym(um, currency):
#     return um / currency_to_rate[currency]
#
#
# main()

# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит Выберите валюту из ['USD','EUR','CHF','GBP','CNY']
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит Введите сумму
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит
#             Вы ввели сумму int и валюту Валюта
#             конвертированная сумма в Валюта = int
#     6. Скипт должен выдать сообщение
#                 Введите положительное число. Если число меньше 0.
#                 Вы ввели не число. Введите число. Если введены буквы.
#                 Вы ввели пустое поле. Введите число. Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.

# Variant 1

# cur = ['USD', 'EUR', 'CHF', 'GBR', 'CNY']
# currency_to_rate = {'USD': 73.0841, 'EUR': 86.1150, 'CHF': 79.3616, 'GBR': 100.9730, 'CNY': 11.3230}
#
# while True:
#
#     your_money = input('Enter RUB ')
#     try:
#         your_money = int(your_money)
#         if your_money < 0:
#             raise ValueError
#     except ValueError:
#         print(your_money, '- wrong input. Enter positive number!')
#         continue
#
#     print('Choose currency from 0 to 4 :', '\n', 'USD - 0', '\n', 'EUR - 1', '\n', 'CHF - 2', '\n',
#           'GBR - 3', '\n', 'CNY - 4')
#     break
#
# while True:
#
#     input_currency = input()
#     try:
#         input_currency = int(input_currency)
#         if input_currency > 5:
#             raise ValueError
#         elif input_currency < 0:
#             raise ValueError
#     except ValueError:
#         print('- wrong input. Choose your currency from 0 to 4', '\n',
#         'USD - 0', '\n', 'EUR - 1', '\n', 'CHF - 2', '\n', 'GBR - 3', '\n', 'CNY - 4 :')

#         continue
#
#     your_currency = cur[input_currency]
#     your_exchange_result = your_money / currency_to_rate[your_currency]
#     print(your_money, 'RUB =', your_exchange_result, your_currency)
#     break
#
#
# Variant 2

cur = ['USD', 'EUR', 'CHF', 'GBR', 'CNY']
currency_to_rate = {'USD': 73.0841, 'EUR': 86.1150, 'CHF': 79.3616, 'GBR': 100.9730, 'CNY': 11.3230}


def main():
    money = input_money()
    your_currency = input_currency()
    print(money, 'RUB =', exchange_ym(money, your_currency), your_currency)


def input_currency():
    while True:
        print('Choose currency', '\n', 'USD - 0', '\n', 'EUR - 1', '\n', 'CHF - 2', '\n', 'GBR - 3', '\n', 'CNY - 4')
        index = input()
        try:
            index = int(index)
            if index > 5:
                raise ValueError
            elif index < 0:
                raise ValueError
        except ValueError:
            print('Wrong input. Choose your currency from 0 to 4')
            continue

        return cur[index]


def input_money():
    while True:
        your_money = input('Enter RUB ')
        try:
            your_money = int(your_money)
        except ValueError:
            print(your_money, 'is not a number. Try again!')
            continue
        if your_money < 0:
            print('Enter positive number')
            continue

        return your_money


def exchange_ym(um, currency):
    return um / currency_to_rate[currency]


while True:
    main()
