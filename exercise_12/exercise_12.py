'''
Exercise 12

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def exercise_12():
    '''
    Exercise 12 method
    '''
    a = [5, 10, 15, 20, 25]
    b = [a[0], a[-1]]
    print(b)

def main():
    '''
    Main method
    '''
    print("Exercise 12 :\n")
    exercise_12()

if __name__ == "__main__":
    main()
