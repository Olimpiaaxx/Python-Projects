import random

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']
player_score = 0
computer_score = 0

while True: 
    player_move = input("Your move: ")
    computer_move = random.choice(moves)


    print("You: ", player_move)
    if player_move == "q":
        break
    print("Me: ", computer_move)
    if player_move == computer_move:
        print("Tie")
    elif player_move + computer_move in player_wins:
        print("You win!")
        player_score = player_score +1
    else:
        print("You lose!")
        computer_score = computer_score +1

def printScore(player, computer):
    print("Player Score: ", player)
    print("Computer Score: ", computer)
    
if player_score < computer_score:
    print("You lose")
elif player_score == computer_score:
    print("It's a tie")
else:
    print("You won!")
    
printScore(player_score, computer_score)
