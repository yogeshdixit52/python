n = int(input("Enter the no. : "))
temp = n
digit = len(str(n))
sum = 0
while(n!=0):
    rem = n%10
    sum = sum + rem**digit
    n = n//10
if(sum==temp):
    print("No. is armstrong")
else:
    print("No. is not armstrong")
