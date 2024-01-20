'''
Exercise 4

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def exercise_4():
    '''
    Exercise 4 method
    '''
    divisors = []
    number = int(input("Enter a number : "))
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)

def main():
    '''
    Main function
    '''
    print("Exercise 4 :\n")
    exercise_4()

if __name__ == "__main__":
    main()
