"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players 
want to start a new game)"""

# define variables
r = 'rock'
p = 'paper'
s = 'scissor'

# initialize the game
while True:
    start_new_game = input('start new game?  If yes press any key, if no press n: ')
    if start_new_game == 'n':
        print('game over!')
        break
    else: # request player inputs and set game rules
        player1 = input('player 1 make your move(enter r, p or s): ')
        player2 = input('player 2 make your move(enter r, p or s): ')
        if player1 == player2:
            print('Its a draw')
        elif player1 == r and player2 == s or player1 == s and player2 == p or player1 == p and player2 == r:
            print('Player 1 is the winner, congratulations!')
        else:
            print('Player 2 is the winner, congratulations!')