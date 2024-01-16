'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras :

1) If the number is a multiple of 4, print out a different message.
2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def exercise_2():
    '''
    Exercise 2 method
    '''
    number = int(input("Enter a number : "))
    if number % 2 == 0:
        print("Even.")
    else:
        print("Odd.")

def extra_1():
    '''
    Extra 1 method
    '''
    number = int(input("Enter a number : "))
    if number % 4 == 0:
        print("Even & multiple of 4")
    elif number % 2 == 0:
        print("Even.")
    else:
        print("Odd.")

def extra_2():
    '''
    Extra 2 method
    '''
    num = int(input("Enter a number : "))
    check = int(input("Enter another number to divide the first one : "))
    if num % check == 0:
        print(f"{num} can be divided by {check}.")
    else:
        print(f"{num} can't be divided by {check}.")

def main():
    '''
    Main method
    '''
    print("Exercise 2 :\n")
    exercise_2()
    print("\nExtra 1 :\n")
    extra_1()
    print("\nExtra 2 :\n")
    extra_2()

if __name__ == "__main__":
    main()
