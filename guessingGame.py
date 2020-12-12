import random
 
hidden = random.randrange(1, 9)

chances = 0

while chances < 5:
    guess = int(input("Please enter your guess between 1 and 9: "))

    if guess == hidden:
        print("Congrats You Won!!")
        break
    elif guess > hidden:
        print("Guess a lower number")
    else:
        print("Guess a higher number")
    chances = chances + 1

if not chances < 5:
    print("You Lose! the number is:", hidden)