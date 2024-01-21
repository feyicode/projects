import random

password = "password123"
dice = [1,2,3,4,5,6]
playerOnePoints = 0
playerTwoPoints = 0
count = 0

print("Hello, welcome to the dice game! Before we begin, each player must authenticate themselves.")
playerOneName = input("Please enter your name, Player 1. " )
playerOnePassword = input("Please enter the associated password. " )
#Asks the user to enter their name and authenticates using a password.

while playerOnePassword != password:
    print("Invalid password.")
    playerOnePassword = input("Please enter the associated password. " )

playerTwoName = input("Please enter your name, Player 2. " )
playerTwoPassword = input("Please enter the associated password. " )

while playerTwoPassword != password:
    print("Invalid password.")
    playerTwoPassword = input("Please enter the associated password. " )

#The user is asked to input their password forever, until they get it right.
#They are unable to continue, if it's incorrect.

print("\nThe game may now begin, best of luck to everyone!\n")
cont = input("Enter y to continue and roll both dices: ")

while count < 5 and cont == "y":
    count += 1
    playerOneDiceRoll = random.choice(dice)
    playerOneDiceRollTwo = random.choice(dice)
    playerTwoDiceRoll = random.choice(dice)
    playerTwoDiceRollTwo = random.choice(dice)
    print("Player 1 has rolled a " + str(playerOneDiceRoll) + " and a " + str(playerOneDiceRollTwo) + ". Player 2 has rolled a " + str(playerTwoDiceRoll) + " and a " + str(playerTwoDiceRollTwo) + ".")
    playerOnePoints += playerOneDiceRoll + playerOneDiceRollTwo
    playerTwoPoints += playerTwoDiceRoll + playerTwoDiceRollTwo

#A loop runs 5 times, rolling the dice and adding that number to each layer's total.
#Then, each individual if statement is checked to add/remove points depending on whether the condition is met.

    if playerOneDiceRoll == playerOneDiceRollTwo:
        print("Player 1 gets another chance to roll, as they have rolled a double.")
        playerOneExtra = random.choice(dice)
        print("Player 1 has rolled a " + str(playerOneExtra) + ". This has been added to their score." )
        playerOnePoints += playerOneExtra
       
    if playerTwoDiceRoll == playerTwoDiceRollTwo:
        print("Player 2 gets another chance to roll, as they have rolled a double.")
        playerTwoExtra = random.choice(dice)
        print("Player 2 has rolled a " + str(playerTwoExtra) + ". This has been added to their score.")
        playerTwoPoints += playerTwoExtra
       
    if (playerOneDiceRoll + playerOneDiceRollTwo) % 2 == 0:
        print("10 points have been added to Player 1's score, as they rolled have an even total.")
        playerOnePoints += 10
       
    if (playerTwoDiceRoll + playerTwoDiceRollTwo) % 2 == 0:
        print("10 points have been added to Player 2's score, as they rolled have an even total.")
        playerTwoPoints += 10
       
    if (playerOneDiceRoll + playerOneDiceRollTwo) % 2 == 1:
        print("5 points have been removed from Player 1's score, as they have rolled an odd total.")
        playerOnePoints -= 5

    if (playerTwoDiceRoll + playerTwoDiceRollTwo) % 2 == 1:
        print("5 points have been removed from Player 2's score, as they have rolled an odd total.")
        playerTwoPoints -=5

    if playerOnePoints < 0:
        print("\nPlayer 1's points have reached below 0, therefore their points have been reset.")
        playerOnePoints = 0

    if playerTwoPoints < 0:
        print("\nPlayer 2's points have reached below 0, therefore their points have been reset.")
        playerTwoPoints = 0

    print("\nPlayer 1 has " + str(playerOnePoints) + " points and Player 2 has " + str(playerTwoPoints) + " points.\n")
    cont=input("Enter y to continue: ")
   #At the end of each loop, the player's current running score of points is displayed.

if playerOnePoints == playerTwoPoints:
    print("The scores are currently tied, therefore there will be a tiebreaker roll.")
    print("Player 1 has rolled a " + str(random.choice(dice)) + " and Player 2 has rolled a " + str(random.choice(dice)) + ".")
    if playerOnePoints > playerTwoPoints:
        print("Player 1 has won!")
        winner = playerOneName
        winnerPoints = playerOnePoints
    else:
        print("Player 2 has won!")
        winner = playerTwoName
        winnerPoints = playerTwoPoints
elif playerOnePoints > playerTwoPoints:
    print("Player 1 has won!")
    winner = playerOneName
    winnerPoints = playerOnePoints
else:
    print("Player 2 has won!")
    winner = playerTwoName
    winnerPoints = playerTwoPoints
 #Checks to determine who is the winner or whether a tiebreaker is needed.

f = open("leaderboard.txt", "a+")
f.write(winner + ", " + str(winnerPoints) + "\n")
f.seek(0)
lines = f.readlines()

db2=[]

f=open("leaderboard.txt","r")
text="a"
while text!="":
    
    text=f.readline()
    if text=="":
        break
    data=text.split(",")
    data[1]=int(data[1].replace("\n",""))
    db2.append(data)
f.close()
db2.sort(key=lambda x:int(x[1]), reverse = True)

leaderboard = str(db2[0:5])

print("\nThe leaderboard is as follows: " + leaderboard)

#Creates a file with the leaderboard, which stores the winner's score and name in an external file
