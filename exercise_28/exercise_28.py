'''
Exercise 28

Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
'''

def exercise_28(number_1, number_2, number_3):
    '''
    Exercise 28 method
    '''
    if number_1 > number_2 and number_1 > number_3:
        print(number_1)
    elif number_2 > number_1 and number_2 > number_3:
        print(number_2)
    else:
        print(number_3)

def main():
    '''
    Main method
    '''
    print("Exercise 28 :\n")
    number_1 = int(input("Enter the first number : "))
    number_2 = int(input("Enter the second number : "))
    number_3 = int(input("Enter the third number : "))
    exercise_28(number_1, number_2, number_3)

if __name__ == "__main__":
    main()
