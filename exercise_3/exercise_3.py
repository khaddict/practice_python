'''
Exercise 3

Take a list, say for example this one : a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.

Extras :

1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2) Write this in one line of Python.
3) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

def exercise_3():
    '''
    Exercise 3 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i < 5:
            print(i)

def extra_1():
    '''
    Extra 1 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if i < 5:
            b.append(i)
    print(b)

def extra_2():
    '''
    Extra 2 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([i for i in a if i < 5])

def extra_3():
    '''
    Extra 3 method
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    number = int(input("Enter a number : "))
    for i in a:
        if i < number:
            b.append(i)
    print(b)

def main():
    '''
    Main method
    '''
    print("Exercise 3 :\n")
    exercise_3()
    print("\nExtra 1 :\n")
    extra_1()
    print("\nExtra 2 :\n")
    extra_2()
    print("\nExtra 3 :\n")
    extra_3()

if __name__ == "__main__":
    main()
