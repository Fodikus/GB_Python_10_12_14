# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов: "))
while n < 3:
    dictionary = input("Вы ошиблись! Количество кустов не должно быть меньше 3-х! \nВведите количество кустов: ")

numbers = list()
for i in range(n):
    numbers.append(int(input(f"Введите количество ягод на кусту {i + 1}: ")))

numbers_count = list()
for i in range(len(numbers) - 1):
    numbers_count.append(numbers[i - 1] + numbers[i] + numbers[i + 1])
numbers_count.append(numbers[-2] + numbers[-1] + numbers[0])

print(f"Максимального числа ягод, которое может собрать за один заход собирающий модуль: {max(numbers_count)}")