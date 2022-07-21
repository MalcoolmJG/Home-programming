# Rock Paper Scissors
import random
import json
jsonFile = open("score.json", "w")
def game():
    x = {
        "Player": "Rock",
        "Computer": "Scissors",
        "Outcome": "lose"
    }
    opt = ["rock", "paper", "scissors"]
    computer = random.choice(opt)
    player = input("Rock, Paper, or Scissors?")
    again = False
    print(computer)
    # finding winner
    # draws
    if player[0].lower() == computer[0]:
        print("Draw!, Play again? Yes/No")
        if input()[0].lower() == "y":
            game()
        else:
            return
    # win
    elif (player[0].lower() == "r" and computer == "scissors") or (player[0].lower() == "p" and computer == "rock") or (player[0].lower() == "s" and computer == "paper"):
        print("You Win!, Play again? Yes/No")
        if input()[0].lower() == "y":
            game()
        else:
            return
    # loss
    else:
        print("You Lose!, Play again? Yes/No")
        if input()[0].lower() == "y":
            game()
        else:
            return

if __name__ == '__main__':
    game()
