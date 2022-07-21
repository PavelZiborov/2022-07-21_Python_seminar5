# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


text = 'тыабвы выабв ты абв она ЫЫЫабвЫЫЫ он 1 2 тавабв 3'

def ListSort(text):
    lst = text.split()
    new_lst = []
    for i in range(0, len(lst)):
        if 'абв' in lst[i]:
            continue
        else:
            new_lst.append(lst[i])
    new_text = ''
    for i in new_lst:
        new_text = new_text + i + ' '
    return new_text

print(f'Изначальный текст: {text}')
print(f'Исправленный текст: {ListSort(text)}')