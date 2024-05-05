import random

def RPS_Game(comp,you):
    if comp == "rock":
        if you == "paper":
            print("You won...!!")
        elif you == "scissors":
            print("You lost...!!")
        elif comp == you:
            print("It's a tie...!!")
        else : 
            print("Computer : Dekh ke kr na bhai...!!")
    elif comp == "scissors":
        if you == "rock":
            print("You won...!!")
        elif you == "paper":
            print("You lost...!!")
        elif comp == you : 
            print("It's a tie...!!")
        else :
            print("Computer : Dekh ke kr na bhai...!!")
    elif comp == "paper":
        if you == "scissors":
            print("You won...!!")
        elif you == "rock":
            print("You lost...!!")
        elif comp == you : 
            print("It's a tie...!!")
        else :
            print("Computer : Dekh ke kr na bhai...!!")
    else:
        print("Dekh ke kr bhai...!!")
a = random.randint(1, 3)

if a == 1:
    comp = "rock"
elif a == 2:
    comp = "scissors"
else:
    comp = "paper"
        
you = input("Enter your choice rock, paper or scissors : ")
print(f"The Computer chose : {comp}")

RPS_Game(comp,you)