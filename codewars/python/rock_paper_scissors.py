def rps(p1, p2):

    # First Solution
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

    # Second Solution

    # if p1 == p2:
    #     return "Draw!"
    #     exit()

    # match p1:
    #     case "scissors":
    #         if p2 == "paper":
    #             return "Player 1 won!"
    #         elif p2 == "rock":
    #             return "Player 2 won!"
    #     case "paper":
    #         if p2 == "rock":
    #             return "Player 1 won!"
    #         elif p2 == "scissors":
    #             return "Player 2 won!"
    #     case "rock":
    #         if p2 == "scissors":
    #             return "Player 1 won!"
    #         elif p2 == "paper":
    #             return "Player 2 won!"      
    #     case _:
    #         return "Error, try again"


print("Welcome to Rock, Paper, Scissors Game !")
print("To play just write rock, paper or scissors\n")
p1 = input("Player 1: ")
p2 = input("Player 2: ")

print(rps(p1, p2))