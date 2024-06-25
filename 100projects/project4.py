#Project: rock paper scissor
import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock,paper,scissor]
randomchoice=random.randint(0,2)
comp_chose=list[randomchoice]

choose=int(input("What do you choose? Type '0' for Rock , '1' for Paper and '2' for Scissor\n"))

if (choose==0):
    print("You chose:")
    print(rock)
    print("Computer chose:")
    print(comp_chose)

    if (randomchoice==0):
        print("Draw!")
    elif(randomchoice==1):
        print("You lose!")
    else:
        print("You win!")

elif (choose==1):
    print("You chose:")
    print(paper)
    print("Computer chose:")
    print(comp_chose)

    if (randomchoice==1):
        print("Draw!")
    elif(randomchoice==2):
        print("You lose!")
    else:
        print("You win!")

elif (choose==2):
    print("You chose:")
    print(scissor)
    print("Computer chose:")
    print(comp_chose)

    if (randomchoice==2):
        print("Draw!")
    elif(randomchoice==0):
        print("You lose!")
    else:
        print("You win!")

else:
    print("You entered invalid number, You lose!")
