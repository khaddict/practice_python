'''
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras :

1) Keep the game going until the user types “exit”
2) Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
import sys

def exercise_9():
    '''
    Exercise 9 method
    '''
    random_number = random.randint(1, 9)
    number = int(input("Enter a number between 1 and 9 : "))
    if not 1 <= number <= 9:
        print("The number has to be between 1 and 9.")
        sys.exit()
    if number == random_number:
        print("Win !")
    elif number < random_number:
        print("Too low !")
    else:
        print("Too high !")

def extra_1():
    '''
    Extra 1 method
    '''
    random_number = random.randint(1, 9)
    while True:
        number = str(input("Enter a number between 1 and 9 : "))
        if number == 'exit':
            print("Bye !")
            break
        if not 1 <= int(number) <= 9:
            print("The number has to be between 1 and 9.")
            break
        if int(number) == random_number:
            print("Won !")
            break
        if int(number) < random_number:
            print("Too low !")
        else:
            print("Too high !")

def extra_2():
    '''
    Extra 2 method
    '''
    random_number = random.randint(1, 9)
    counter = 1
    while True:
        number = str(input("Enter a number between 1 and 9 : "))
        if number == 'exit':
            print("Bye !")
            break
        if not 1 <= int(number) <= 9:
            print("The number has to be between 1 and 9.")
            break
        if int(number) == random_number:
            print(f"Won in {counter} tries !")
            break
        if int(number) < random_number:
            print("Too low !")
            counter += 1
        else:
            print("Too high !")
            counter += 1

def main():
    '''
    Main method
    '''
    print("Exercise 9 :\n")
    exercise_9()
    print("\nExtra 1 :\n")
    extra_1()
    print("\nExtra 2 :\n")
    extra_2()

if __name__ == "__main__":
    main()
