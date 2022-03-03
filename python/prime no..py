n = int(input('Enter the number : '))
i=2
while (i<n):
    if(n%i==0):
        print('No. is not prime')
        break
    i+=1
if(i==n):
    print('No. is prime')
