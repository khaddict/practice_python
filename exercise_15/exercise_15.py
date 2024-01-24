'''
Exercise 15

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

For example, say I type the string : My name is Michele
Then I would see the string : Michele is name My
'''

def exercise_15():
    '''
    Exercise 15 method
    '''
    long_string = str(input("Enter a long string containing multiple words : "))
    a = []
    for i in long_string.split():
        a.append(i)
    a = ' '.join(a[::-1])
    print(a)

def main():
    '''
    Main method
    '''
    print("Exercise 15 :\n")
    exercise_15()

if __name__ == "__main__":
    main()
