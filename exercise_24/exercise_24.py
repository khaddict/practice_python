'''
Exercise 24

This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game boards that look like this:
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by : print("Thing to show on screen")
'''

def exercise_24():
    '''
    Exercise 24 method
    '''
    board_size = int(input("Board size : "))
    for _ in range(0, board_size):
        print(" ---" * board_size, end="\n")
        print("|   " * (board_size + 1), end="\n")
    print(" ---" * board_size, end="\n")

def main():
    '''
    Main method
    '''
    print("Exercise 24 :\n")
    exercise_24()

if __name__ == "__main__":
    main()
