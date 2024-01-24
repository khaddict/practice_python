'''
Exercise 11

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''

def exercise_11():
    '''
    Exercise 11 method
    '''
    number = int(input("Enter a number : "))
    if number == 1:
        print("1 is not a prime number.")
    for i in range(2, number + 1):
        if (number % i == 0) and (i != number):
            print(f"{number} is not a prime number.")
            break
        if i == number:
            print(f"{number} is a prime number.")

def main():
    '''
    Main method
    '''
    print("Exercise 11 :\n")
    exercise_11()

if __name__ == "__main__":
    main()
