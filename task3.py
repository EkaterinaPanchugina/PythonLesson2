#3. Задайте список из n чисел последовательности (1+1/𝑛)𝑛 выведите на экран их сумму.
# Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37} сумма 6,62


def sequence_of_numbers(n,x={},summa=0):
    for i in range(1,n+1):
        x[i]=round((1 + (1/i))**i ,2)
    print(x)
    for i in x.values():
        summa+=i
    print(summa)

pos = sequence_of_numbers(n:=int(input("Введите число: ")))