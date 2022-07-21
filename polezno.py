def NeedIntNumber(text):  # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            needTrue = True
            return number
        except:
            print('Ошибка ввода. Введите целое число: ')


# A = needIntNumber('Введите целое число: ')
# print(A)


def NeedFloatNumber(text):  # Функция, которая принимает на вход вещественное число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = float(number)
            needTrue = True
            return number
        except:
            print('Ошибка ввода. Введите вещественное число: ')


# B = needFloatNumber('Введите вещественное число: ')
# print(B)


# # записывание списка в файл:
# with open('listOfNumbers.json', 'w', encoding='utf-8') as data: # загрузка списка в файл listOfNumbers.json
#     data.write(json.dumps(list))
#     data.write('\n')
# print('Лист успешно сохранен в файл')


# # считывание списка из файла:
# with open('listOfNumbers.json', 'r', encoding='utf-8') as data:  # открываем файл на чтение
#     BD = json.load(data)  # загружаем из файла данные в словарь data
# print(f'Загружена информация из файла: {BD}')


# a = input('введите числа через пробел: ')
# f = [int(s) for s in a.split()]  - что это за запись? 


# перемешивание списка
# from random import *
# sp=[1,6.8,8,11,'sdfsdf0',True]

# for i in range(25):
#     buf=0
#     x=randint(0,len(sp)-1)
#     y=randint(0,len(sp)-1)
#     buf=sp[x]
#     sp[x]=sp[y]
#     sp[y]=buf
# print(sp)