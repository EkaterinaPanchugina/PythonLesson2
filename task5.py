#Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

sp = [1, 2, 3, 4]
sp[1], sp[2]= sp[2], sp [1]
sp[-1], sp[-2]= sp[-2], sp [-1]
print(sp)
