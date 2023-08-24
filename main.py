from Task2625SumMultiples import *
from Task217ContainsDuplicate import*

# 2625 Sum Multiples
print ('Введите число')
n = int(input())
res = SumMultiples(n)
print(res)

# 217 Contains Duplicates
print('Задайте желаемую длину массива для проверки дубликатов')          # задаем входные данные
length = int(input())                # 1)задаем длину массива пользователя
mylist = []
print(f'Введите {length} чисел')
for i in range (0,length):
    mylist.append(int(input()))      # 2)наполняем массив
print(containsDuplicate(mylist))     # решение задачи
