#Project:Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sum_let=[]
for i in range (0,nr_letters):
    ran_let=random.choice(letters)
    sum_let.append(ran_let)

sum_sym=[]
for i in range (0,nr_symbols):
    ran_sym=random.choice(symbols)
    sum_sym.append(ran_sym)

sum_num=[]
for i in range (0,nr_numbers):
    ran_num=random.choice(numbers)
    sum_num.append(ran_num)

#pass1 is list of all numbers symbols and letters but in list
pass1 = sum_let + sum_num + sum_sym

random.shuffle(pass1)

#pass2 is password in string
pass2 = ''.join(pass1)

print(f"Here is your password: {pass2}")