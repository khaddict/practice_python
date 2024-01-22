'''
Exercise 10

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extra :

Randomly generate two lists to test this
'''

import random

def exercise_10():
    '''
    Exercise 10 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in a:
        if (i in b) and (i not in c):
            c.append(i)
    print(c)

def extra_1():
    '''
    Extra 1 method
    '''
    a = random.sample(range(1,30), 10)
    b = random.sample(range(1,30), 20)
    c = []
    for i in a:
        if (i in b) and (i not in c):
            c.append(i)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"common elements = {c}")

def main():
    '''
    Main method
    '''
    print("Exercise 10 :\n")
    exercise_10()
    print("\nExtra 1 :\n")
    extra_1()

if __name__ == "__main__":
    main()
