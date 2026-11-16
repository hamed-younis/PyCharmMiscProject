import random

a = random.randrange(1,4)
a = random.choice(['rock','se','perpar'])
computer =0
user = 0
result = (computer+1,user+1)
for i in range (1,11): 
    computer = input("take one choice'rock','se','perpar'") 
    user = input("enter any one from rock, se, perpar")
    if computer > user :
        print("you lose")
        print(result)
    elif user > computer :
        print("you win")
        print(result)       
    else:
        print("tai")
        print(result)

    