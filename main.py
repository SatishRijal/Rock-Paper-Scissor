import random


choices = ['rock','paper','scissors']
computer = random.choice(choices)
name = input('Enter your name: ')

player = None
while player not in choices:
    player = input('Enter rock, paper or scissors: ').lower()

if player == computer:
    print("Computer : "+computer)
    print(f"{name} : "+player)
    print('Tie!!!!')
elif player == "rock":
    if computer =="paper":
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} loose!!!")
    else :
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} win!!!")
elif player == "paper":
    if computer == "rock":
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} win!!!")
    else:
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} loose!!!")
elif player == "scissors":
    if computer == "rock":
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} loose!!!")
    else:
        print("Computer : " + computer)
        print(f"{name} : " + player)
        print(f"{name} win!!!")
