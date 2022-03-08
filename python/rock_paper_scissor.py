import random
comp_score = 0
usr_score = 0
choice = ["r","p","s"]
while(1):
    comp_input = random.choice(choice)
    usr_input = input("Enter your choice(r,p,s) : ")
    if(usr_input==comp_input):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Match draw")
    elif(usr_input=='r' and comp_input=='s'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Player wins")
        usr_score += 10
    elif(usr_input=='r' and comp_input=='p'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Computer wins")
        comp_score += 10
    elif(usr_input=='s' and comp_input=='p'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Player wins")
        usr_score += 10
    elif(usr_input=='s' and comp_input=='r'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Computer wins")
        comp_score += 10
    elif(usr_input=='p' and comp_input=='r'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Player wins")
        usr_score += 10
    elif(usr_input=='p' and comp_input=='s'):
        print("Computer input :",comp_input)
        print("Your input :",usr_input)
        print("Computer wins")
        comp_score += 10
    else:
        print("Not a valid input")
    a = input("Do you want to continue(y/n) : ")
    if(a=='n'):
        break
print("Computer Score : ",comp_score)
print("Your Score :",usr_score)
if(comp_score==usr_score):
    print("Match drawn")
elif(comp_score>usr_score):
    print("Computer Wins")
else:
    print("User Wins")
    
