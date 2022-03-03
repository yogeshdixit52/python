a,b,c = input("Enter values : ").split()
a,b,c = int(a),int(b),int(c)
if (a>b and a>c):
    print(a,"is greatest")
elif (b>a and b>c):
    print(b,"is greatest")
elif (c>a and c>b):
    print(c,"is greatest")
