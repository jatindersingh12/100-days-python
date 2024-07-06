# Project : Number guessing game

import random
logo="""
 $$$$$$\                                                  $$\     $$\                                                         $$\                           
$$  __$$\                                                 $$ |    $$ |                                                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
 """
print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number=random.randint(1,100)
level=input("Choose the difficulty. 'Easy' or 'Hard' : ").lower()
if level=="easy":
    print(f"You have {10} attempts to guess the number")
    for i in range (10):
        guess=int(input("Make a guess : "))
        if guess > number and i<9:
            print("Too high.")
            print("Guess again.")
            print(f"You have {9-i} guess remaining to guess the number.")
            print("")
        elif guess < number and i<9:
            print("Too low.")
            print("Guess again.")
            print(f"You have {9-i} guess remaining to guess the number.")
            print("")
        elif guess==number:
            print(f"You got it! The answer is {guess}.")
            break
        else:
            print("You lost!")

elif level=="hard":
    print(f"You have {5} attempts to guess the number")
    for i in range (5):
        guess=int(input("Make a guess : "))
        if guess > number and i<4:
            print("Too high.")
            print("Guess again.")
            print(f"You have {4-i} guess remaining to guess the number.")
            print("")
        elif guess < number and i<4:
            print("Too low.")
            print("Guess again.")
            print(f"You have {4-i} guess remaining to guess the number.")
            print("")
        elif guess==number:
            print(f"You got it! The answer is {guess}.")
            break
        else:
            print("You lost!")