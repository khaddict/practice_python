'''
Exercise 1

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras :

1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

from datetime import datetime

def exercise_1():
    '''
    Exercise 1 method
    '''
    name = str(input("Enter your name : "))
    age = int(input("Enter your age : "))
    year = datetime.now().year
    print(f"Hello {name} ! You will be 100 in {year + (100 - age)}.")

def extra_1():
    '''
    Extra 1 method
    '''
    name = str(input("Enter your name : "))
    age = int(input("Enter your age : "))
    number = int(input("How many times you want me to print the final message ? : "))
    year = datetime.now().year
    print(f"Hello {name} ! You will be 100 in {year + (100 - age)}." * number)

def extra_2():
    '''
    Extra 2 method
    '''
    name = str(input("Enter your name : "))
    age = int(input("Enter your age : "))
    number = int(input("How many times you want me to print the final message ? : "))
    year = datetime.now().year
    for _ in range(number):
        print(f"Hello {name} ! You will be 100 in {year + (100 - age)}.")

def main():
    '''
    Main method
    '''
    print("Exercise 1 :\n")
    exercise_1()
    print("\nExtra 1 :\n")
    extra_1()
    print("\nExtra 2 :\n")
    extra_2()

if __name__ == "__main__":
    main()
