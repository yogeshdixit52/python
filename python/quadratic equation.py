print("Quadratic Euation : ax^2 + bx +c")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
D = (b*b-4*a*c)
if (D>0):
    x1 = (-b+D**0.5)/2*a
    x2 = (-b-D**0.5)/2*a
    print("The roots of the equation are :",x1,x2)
elif (D==0):
    x1 = -b/2*a
    x2 = -x1
elif (D<0):
    x1 = complex((-b+D**0.5)/2*a)
    x2 = complex((-b-D**0.5)/2*a)
