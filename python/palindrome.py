n = int(input("Enter the no. : "))
temp = n
rev = 0
while(n>0):
    rem = n%10
    rev = rev*10 + rem
    n=n//10
if(rev == temp):
    print("Yes! This no. is Palindrome")
else:
    print("No! This no. is not Palindrome")

