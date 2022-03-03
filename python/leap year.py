n = int(input("Enter year : "))
if((n%4==0) and (n%100!=0) or (n%400==0)):
    print("Its a leap year")
else:
    print("Its not a leap year")
