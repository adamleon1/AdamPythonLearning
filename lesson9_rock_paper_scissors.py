import random
options = ['rock','paper','scissors']
computer = random.choice(options)
adam = input(f'Please choose from {options}') 

if adam == computer:
    print('DRAW')
elif adam == "rock" and computer =="scissors" or adam == "scissors" and computer == "paper" or adam=="paper" and computer=="rock":
    print ("adam won!")
elif adam == "paper" and computer =="scissors" or adam == "scissors" and computer == "rock" or adam=="rock" and computer=="paper":
    print ("computer won")
else:
    print(f'something wrong entered please choose from {options}')


print(computer,adam)