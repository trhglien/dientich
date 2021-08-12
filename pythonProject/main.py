import math
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of the triangle is: ", area)
