'''
Exercise 14

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras :

1) Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2) Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

import random

def exercise_14():
    '''
    Exercise 14 method
    '''
    a = [1, 3, 4, 5, 1, 2, 1, 5, 7, 4, 7, 9, 10]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(f"a = {a}")
    print(f"a without duplicates = {b}")

def extra_1():
    '''
    Extra 1 method
    '''
    a = []
    for _ in range(1, 10):
        random_number = random.randint(1, 10)
        a.append(random_number)
    b = list(set(a))
    print(f"a = {a}")
    print(f"a without duplicates = {b}")

def extra_2():
    '''
    Extra 2 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in a:
        if i in b:
            c.append(i)
    print(set(c))

def main():
    '''
    Main method
    '''
    print("Exercise 14 :\n")
    exercise_14()
    print("\nExtra 1 :\n")
    extra_1()
    print("\nExtra 2 :\n")
    extra_2()

if __name__ == "__main__":
    main()
