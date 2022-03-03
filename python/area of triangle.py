print('\t\t\t************************')
print('\t\t   Program to find Area of a triangle')
print('\t\t\t************************')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('Area = ',area)
