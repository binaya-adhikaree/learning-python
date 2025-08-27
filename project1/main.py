

# rock = 1
# paper = 2
# scisor = 3
import random

computer = random.choice([1,2,3])
dictlist = {1:"rock",2:"paper", 3:"scisor"}

you = int(input("enter your choise: "))
print(f"computer choose {dictlist[computer]} you choose {dictlist[you]}")


if(computer == 1 and you == 1):
    print("tie")
elif(computer == 1 and you == 2):
    print("you win")    
elif(computer == 1 and you == 3):
    print("you lose")
elif(computer == 2 and you == 1):
    print("you lose")
elif(computer == 2 and you == 2):
    print("tie")       
elif(computer == 2 and you == 3):
    print("you win")     
elif(computer == 3 and you == 1):
    print("you win")
elif(computer == 3 and you == 2):
    print("you lose")   
elif(computer == 3 and you == 3):
    print("tie")     