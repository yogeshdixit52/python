a,b = input("Enter range : ").split()
a,b = int(a),int(b)
for n in range(a,(b+1)):
    temp = n
    digit = len(str(n))
    sum = 0
    while(n!=0):
        rem = n%10
        sum = sum + rem**digit
        n = n//10
    if(sum==temp):
        print(sum)
