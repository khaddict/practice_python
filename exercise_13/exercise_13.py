'''
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def exercise_13():
    '''
    Exercise 13 method
    '''
    number = int(input("How many Fibonnaci numbers do you want to generate ? : "))
    if number < 0:
        print("The number must be greater than 0.")
    elif number == 0:
        a = []
        print(a)
    elif number == 1:
        a = [0]
        print(a)
    elif number == 2:
        a = [0, 1]
        print(a)
    else:
        a = [0, 1]
        i = 2
        while i < number:
            a.append(a[i-1] + a[i-2])
            i += 1
        print(a)

def main():
    '''
    Main method
    '''
    print("Exercise 13 :\n")
    exercise_13()

if __name__ == "__main__":
    main()
