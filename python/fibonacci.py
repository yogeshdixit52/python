n=int(input('Enter the term till which you want to print Fibonacci : '))
a=0
b=1
i=3
print(a)
print(b)
while(i<=n):
    c=a+b
    a=b
    b=c
    print(c)
    i+=1
