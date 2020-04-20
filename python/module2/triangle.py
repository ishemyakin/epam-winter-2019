from sys import argv
from math import sqrt
a, b, c = int(argv[1]), int(argv[2]), int(argv[3])
# print(a, b, c)
if (a, b, c > 0) and (a+b>c and a+c>b and b+c>a):
    p = (a + b + c)/2
    s = sqrt(p*(p - a)*(p - b)*(p - c))
    print(s)
else:
    print("Такой треугольник не существует")
