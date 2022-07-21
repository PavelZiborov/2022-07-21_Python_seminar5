# 32. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


sp = list(map(int, input().split()))
new_sp = []
for i in sp:
    if sp.count(i) == 1:
        new_sp.append(i)

# numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
# def UniqueNumbers(numbers):
#     result=[i for i in numbers if numbers.count(i)==1]
#     return result
# print(UniqueNumbers(numbers))

print(sp)
print(new_sp)