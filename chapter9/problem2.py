
import random

def game():
    print("game started")
    
    myScore = random.randint(1,60)
    
    print(f"my score is {myScore}")

    with open("./highscore.txt") as f:
        highscore = f.read()

        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0


    if(myScore>highscore):
        with open("./highscore.txt","w") as f:
            f.write(str(myScore)) 
        return myScore
game()



     
            
