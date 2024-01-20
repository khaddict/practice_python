'''
Exercise 5

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extra :

Randomly generate two lists to test this
'''

import random

def exercise_5():
    '''
    Exercise 5 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in a:
        if i in b and i not in c:
            c.append(i)
    print(c)

def extra_1():
    '''
    Extra 1 method
    '''
    a = []
    b = []
    c = []
    for _ in range(1, 20):
        random_number = random.randint(1, 100)
        a.append(random_number)
    for _ in range(1, 20):
        random_number = random.randint(1, 100)
        b.append(random_number)
    for i in a:
        if i in b and i not in c:
            c.append(i)
    print(f"a = {a}\nb = {b}\nc = {c}")

def main():
    '''
    Main method
    '''
    print("Exercise 5 :\n")
    exercise_5()
    print("\nExtra 1 :\n")
    extra_1()

if __name__ == "__main__":
    main()
