a = int(input("Enter start : "))
b = int(input("Enter end : "))
for n in range(a,(b+1)):
    i = 2
    while(i<n):
        if(n%i==0):
            break
        i+=1
    if(i==n):
        print(n)
    
