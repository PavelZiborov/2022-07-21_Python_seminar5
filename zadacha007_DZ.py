# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.

# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66




from itertools import zip_longest

def OpenFile(fileName):
    with open(fileName, 'r') as file:  # открываем файл на чтение
        return file.read()

def WriteFile(fileName, data):
    with open(fileName, 'a') as file:  
        file.write(str(data)+'\n')

def SelectionOfPolynomials(inputText):
    # Убираем лишние пробелы и делаем список разделенный знаком +
    inputList = inputText.replace(' ', '').split('+')
    # создание списка длиной с inputList и заполненный нулями
    lst = [0 for i in range(0, len(inputList))]

    for i in range(0, len(inputList)):
        if inputList[i].isdigit():               # проверяет на наличие числа
            lst[-1] = inputList[i]
        elif inputList[i][-1] == 'x':            # проверяет на наличие 'x'
            lst[-2] = inputList[i].split('*')[0]

    for coefficent in range(0, len(inputList)):
        for item in inputList:
            if not item.isdigit() and item.split('*')[1] == f'x^{coefficent}':
                lst[-coefficent-1] = item.split('*')[0]
    
    return [int(i) for i in lst]

def SummOfPolynomials(lst_1, lst_2):
    result_list = []
    lst_1.reverse()
    lst_2.reverse()
    for i,j in zip_longest(lst_1,lst_2, fillvalue=0):
        result_list.append(i+j)
    result_list.reverse()
    return result_list

def PrintPolinomials (data):
    text = ''
    for i in range(0,len(data)):
        if i == len(data) -1:
            text = text + f'{data[i]}'
        elif i == len(data) -2:
            text = text + f'{data[i]}' + '*x + '
        else:
            text = text + f'{data[i]}' + f'*x^{len(data) - 1 - i}' +' + '
    return text


m1 = OpenFile('f1.txt')
m2 = OpenFile('f2.txt')

print(m1)
l1 = SelectionOfPolynomials(m1)

print(m2)
l2 = SelectionOfPolynomials(m2)

result = SummOfPolynomials(l1,l2)
print(result)                                                # [3, 12, 10, 66]

result_text = PrintPolinomials(result)

print(f'В файл записано:\n{result_text}')                    # 3*x^3 + 12*x^2 + 10*x + 66
WriteFile('result.txt', result_text)