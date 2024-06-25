# Project : Blackjack game

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
card_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]

again='y'
while again=='y':
    print(logo)
    num1=random.choice(card_list)
    num2=random.choice(card_list)
    numlist=[]
    numlist.append(num1)
    numlist.append(num2)

    print(f"Your cards : {numlist}, Current score : {num1+num2}")

    comp_num1=random.choice(card_list)
    comp_num2=random.choice(card_list)
    comp_final=comp_num1+comp_num2
    comp_list=[]
    comp_list.append(comp_num1)
    comp_list.append(comp_num2)

    while comp_final<17:
        comp_new_num=random.choice(card_list)
        comp_list.append(comp_new_num)
        comp_final+=comp_new_num
        if 11 in comp_list and comp_final>21:
            comp_list.remove(11)
            comp_list.append(1)
            final-=10
    print(f"Computer's first card : {comp_num1}")

    other_num='y'
    final=num1+num2

    while other_num=='y' and final<22:
        other_num=input("Type 'y' to get another card , type 'n' to pass : ").lower()
        if other_num=='y':
            new_num=random.choice(card_list)
            numlist.append(new_num)
            final=final+new_num
            if 11 in numlist and final>21:
                numlist.remove(11)
                numlist.append(1)
                final-=10
            print(f"Your cards: {numlist}, current score : {final}")

    print(f"Your final hand : {numlist}, final score : {final}")
    print(f"Computer's final hand : {comp_list}, final score : {comp_final}")

    if final>21:
        print("You went over. You lose!")
    elif comp_final > 21:
        print("You Win!")
    elif final==comp_final:
        print("Draw!")
    elif final>comp_final:
        print("You win!")
    else:
        print("You lose!")

    again=input("Do you want to play another game of Blackjack? Type 'y' or 'n' : ").lower()
