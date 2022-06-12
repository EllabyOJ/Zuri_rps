import random


def rock_paper_scissors():
 while True:

    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = input("R, P, or S?: ")

    while player not in choices:
       print("Invalid input")

    if player == computer:
       print("Player: ", player)
       print("Computer: ", computer)
       print("It is a tie!")
       rock_paper_scissors()
    
    elif player == "R":
        if computer == "P":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You lose, computer wins!")
           break

        if computer == "S":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You win, computer loses!")
           break        

    elif player == "S":
        if computer == "R":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You lose, computer wins!")
           break 

        if computer == "P":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You win, computer loses!")
           break

    elif player == "P":
        if computer == "S":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You lose, computer wins!")
           break

        if computer == "R":
           print("Player: ", player)
           print("Computer: ", computer)
           print("You win, computer loses!")
           break           

 print("Thank you for playing!")

rock_paper_scissors()