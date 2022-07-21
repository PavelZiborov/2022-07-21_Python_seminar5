# 34. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('f1.txt', 'r') as f1:
    m1 = f1.readline()

with open('f2.txt', 'r') as f2:
    m2 = f2.readline()

sp1 = [i for i in m1]
new_sp1 = []
for i in sp1:
    try:
        int(i)
        new_sp1.append(int(i))
    except:
        continue

sum1 = sum(new_sp1)

print(sp1)
print(new_sp1)
print(sum1)
# print(sp2)