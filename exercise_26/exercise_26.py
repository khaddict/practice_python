'''
Exercise 26

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''

def exercise_26():
    '''
    Exercise 26 method
    '''
    board = [[2, 2, 2],
             [2, 1, 0],
             [1, 1, 1]]

    if board[0][0] == board[1][0] == board[2][0]:
        print(f"Winner is player {board[0][0]}.")
    elif board[0][1] == board[1][1] == board[2][1]:
        print(f"Winner is player {board[0][1]}.")
    elif board[0][2] == board[1][2] == board[2][2]:
        print(f"Winner is player {board[0][2]}.")
    elif board[0][0] == board[0][1] == board[0][2]:
        print(f"Winner is player {board[0][0]}.")
    elif board[1][0] == board[1][1] == board[1][2]:
        print(f"Winner is player {board[1][0]}.")
    elif board[2][0] == board[2][1] == board[2][2]:
        print(f"Winner is player {board[2][0]}.")
    elif board[0][0] == board[1][1] == board[2][2]:
        print(f"Winner is player {board[0][0]}.")
    elif board[0][2] == board[1][2] == board[2][0]:
        print(f"Winner is player {board[0][2]}.")
    else:
        print("No winner.")

def main():
    '''
    Main method
    '''
    print("Exercise 26 :\n")
    exercise_26()

if __name__ == "__main__":
    main()
