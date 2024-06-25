# Project: Caeser Cipher

logo = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P`   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"` `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"`  88       88  `"Ybbd8"` 88          
              88                                             
              88           
'''

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encrypt text
def encrypt(message):
    cipher_text=""
    for letter in message:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position + entered_shift
            while (new_position > 25):
                new_position-=26
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=letter
    print(f"The encoded text : {cipher_text}")

# Function to decrypt text
def decrypt(message):
    cipher_text=""
    for letter in message:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position - entered_shift
            while (new_position < 0):
                new_position+=26
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=letter
    print(f"The decoded text : {cipher_text}")

go_again="yes"
while go_again=="yes":

    # Inputs
    cyber=input("Type 'encode' for encrypting text or type 'decode' for decrypting text:\n").lower()

    entered_text=input("Type your message:\n").lower()

    entered_shift=int(input("Type the shift number:\n"))

    if (cyber=="encode"):
        encrypt(entered_text)

    elif (cyber=="decode"):
        decrypt(entered_text)

    go_again=input("Type 'yes' is you want to continue , otherwise type 'no'.\n")
    if(go_again=="no"):
        print("Goodbye!")