from random import randint
from warnings import filterwarnings

pos = ['rock','paper','scissors']

a= 0

i = 0

print("Let's play rock, paper, scissors! ( ͡° ͜ʖ ͡°)")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("\n")

while a < 3:
    com = pos[randint(0,2)]

    plyr = input("Enter: ").strip()

    if any(char.isdigit() for char in plyr):
        print("Enter a valid answer!\n")
    
    a += 1

    if plyr == com:
        print ("tie\n")
    elif plyr == 'rock':
        if com == 'scissors':
            print("You Lose\n")
        else:
            print("You Won!\n")
            i += 1

    elif plyr == 'paper':
        if com == 'rock':
            print("You Win!\n")
            i += 1
        else:
            print("You Won!\n")

    elif plyr == 'scissors':
        if com == 'rock':
            print("You Lose\n")
        else:
            print("You Won!\n")
            i += 1

print("You scored "+str(i)+" out of 3 rounds!")
