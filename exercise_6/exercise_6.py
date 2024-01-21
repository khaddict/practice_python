'''
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

def exercise_6():
    '''
    Exercise 6 method
    '''
    word = list(str(input("Enter a word : ")))
    reverse_word = list(word)[::-1]
    if word == reverse_word:
        print(f"{"".join(str(i) for i in word)} is a palindrome.")
    else:
        print(f"{"".join(str(i) for i in word)} is not a palindrome.")

def main():
    '''
    Main method
    '''
    print("Exercise 6 :\n")
    exercise_6()

if __name__ == "__main__":
    main()
