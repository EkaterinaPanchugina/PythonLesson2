#Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

s = 0
x = str(float(input('Введите вещественное число: ')))
x1 = int("".join(c for c in x if  c.isdecimal()))
#print(x1)
while (x1 != 0):
    s = s + x1 % 10
    x1 = x1 // 10
print("Сумма цифр числа равна: ", s)
