import random

a = random.randrange(1,4)

for i in range(1,10):
 computer = random.choice(['rock','se','pepar'])
 user = input("enter any one from rock, se, pepar")
if computer==user:
    print("tai")
elif(user=="rock" and computer == "se") or \
(user=="rock" and computer=="perpar") or \
(user=="perpar" and computer=="rock"):
  print("you win")
elif (user=="perpar" and computer=="se") or \
(user=="se" and computer=="rock") or \
(user=="se" and computer=="perpar"):
    print("you lose")
else:
    print("invalid input")