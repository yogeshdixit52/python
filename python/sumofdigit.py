n = int(input("Enter the no. : "))
sm = 0
while(n==0):
    rem = n%10
    sm=sm+rem
    n=n//10
print('Sum of the digit :',sm)
