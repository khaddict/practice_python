'''
Exercise 8

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

def exercise_8():
    '''
    Exercise 8 method
    '''
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        new_game = str(input("Do you want to start a new game ? (yes/no) : "))
        if new_game == 'no':
            print("Ok, bye !")
            break
        if new_game == 'yes':
            player_1 = str(input("Hello player 1, rock/paper/scissors : "))
            player_2 = str(input("Hello player 2, rock/paper/scissors : "))
            if player_1 in valid_choices and player_2 in valid_choices:
                if player_1 == player_2:
                    print("Draw !\n")
                elif (player_1 == 'rock' and player_2 == 'paper') or (player_1 == 'paper' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'rock'):
                    print("Player 2 wins.\n")
                else:
                    print("Player 1 wins.\n")
            else:
                print("Not a valid choice. (rock/paper/scissors required)\n")
        else:
            print("Not a valid choice. (yes/no required)\n")

def main():
    '''
    Main method
    '''
    print("Exercise 8 :\n")
    exercise_8()

if __name__ == "__main__":
    main()
