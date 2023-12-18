from multiprocessing import Value
from random import randint


print("Welcome to the number guessing game. The computer will generate a number between 0 and 100. You will start with a fixed score of 100, which will decrease with each guess.")
points = 100
target = randint(0,100)
guessed = False
print(str(target))


while guessed == False and points>0:
    guess = int(input("Please enter your guess: "))
    if guess > target:
        print("\nNice try, but your guess is too large; you've lost 10 points due to an incorrect guess..")
        points -= 10
    elif guess < target:
        print("\nCmon, you can guess a little bigger than that.. You've lost 10 points due to your trash guess.")
        points -=10
    else: 
        print("\nYou've hit our target! ")
        guessed = True
    print("You have", points, "points.")
