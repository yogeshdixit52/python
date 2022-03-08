import random
choice = ["r","p","s"]
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
elif(usr_input=='r' and comp_input=='p'):
    print("Computer input :",comp_input)
    print("Your input :",usr_input)
    print("Computer wins")
elif(usr_input=='s' and comp_input=='p'):
    print("Computer input :",comp_input)
    print("Your input :",usr_input)
    print("Player wins")
elif(usr_input=='s' and comp_input=='r'):
    print("Computer input :",comp_input)
    print("Your input :",usr_input)
    print("Computer wins")
elif(usr_input=='p' and comp_input=='r'):
    print("Computer input :",comp_input)
    print("Your input :",usr_input)
    print("Player wins")
elif(usr_input=='p' and comp_input=='s'):
    print("Computer input :",comp_input)
    print("Your input :",usr_input)
    print("Computer wins")
else:
    print("Not a valid input")
