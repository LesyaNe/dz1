#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n=int(input("Введите номер четверти от 1 до 4: "))

if n==0 or n>4:
    print("Такой плоскости нет ")
elif n==1:
    print("x>0 and y>0 ")
elif n==2:
    print("x<0 and y>0 ")
elif n==3:
    print("x<0 and y<0 ")
elif n==4:
    print("x>0 and y<0 ")